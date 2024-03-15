import numpy as np
import pandas as pd
import seaborn as sns
from functools import reduce
import matplotlib.pyplot as plt

from logger import get_logger

logger = get_logger('logs/main.log')

def main():
    logger.info(f'Main starting')

    input_data_path = "data/"
    logger.info(f'Loading Data')
    last = pd.read_csv(input_data_path + "data_last.csv")
    sector = pd.read_csv(input_data_path + "data_sector.csv")
    volume = pd.read_csv(input_data_path + "data_volume.csv")
    mkt_cap = pd.read_csv(input_data_path + "data_mkt_cap.csv")

    daily_info = [last, mkt_cap, volume]

    logger.info(f'Merging Data')
    stock_info = reduce(lambda left, right: pd.merge(left, right, left_on=['date', 'ticker'], right_on=['date', 'ticker'], how='inner'), daily_info)
    stock_info = stock_info.merge(sector, left_on=['ticker'], right_on=['ticker'], how='inner')
    stock_info["weight"] = stock_info["mkt_cap"] / stock_info.groupby("date")["mkt_cap"].transform("sum")

    logger.info(f'Grouping Data by date')
    stock_index = stock_info.groupby("date").apply(lambda x: np.sum(x["last"]*x["weight"]))
    stock_index = pd.DataFrame(stock_index, columns=["last"])
    stock_index["date"] = stock_index.index
    stock_index.index = range(len(stock_index))

    one_day_last = float(stock_index[stock_index["date"] == "2020-01-06"]["last"])
    stock_index["last"] = stock_index["last"] / one_day_last * 1000
    stock_index["date"] = pd.to_datetime(stock_index["date"], format='%Y-%m-%d')
    
    fig, ax = plt.subplots()
    ax.plot(stock_index["date"], stock_index["last"])
    # plt.show()

    stock_info["difference"] = stock_info.groupby("ticker")["last"].diff()
    stock_info_one_month = stock_info[stock_info["date"] >= "2021-01-01"]
    stock_info_one_month = stock_info_one_month[stock_info_one_month["date"] <= "2021-01-31"]

    stock_info_one_month["contrib"] = stock_info_one_month["weight"] * stock_info_one_month["difference"]
    positive_5_of_each_day = stock_info_one_month.groupby("date").apply(lambda x: x.nlargest(5, "contrib"))["ticker"]
    negative_5_of_each_day = stock_info_one_month.groupby("date").apply(lambda x: x.nsmallest(5, "contrib"))["ticker"]
    logger.info(f'Positive 5: {positive_5_of_each_day}')
    print("Positive 5: \n", positive_5_of_each_day)
    logger.info(f'Negative 5: {negative_5_of_each_day}')
    print("Negative 5: \n", negative_5_of_each_day)

    stock_info_one_year = stock_info[stock_info["date"] >= "2022-01-01"]
    stock_info_one_year = stock_info_one_year[stock_info_one_year["date"] <= "2022-12-31"]

    stock_info_one_year_groupBy_sector = stock_info_one_year.groupby("bics_sector")
    fig, axs = plt.subplots(3, 3, figsize=(15, 15))

    for (name, group), ax in zip(stock_info_one_year_groupBy_sector, axs.flatten()):
        mean = group["difference"].sum() / int(group["difference"].count())
        sns.kdeplot(group["difference"], shade=True, ax=ax)
        ax.set_title(f'Density Plot of Daily Return for {name} Sector')
        ax.set_xlabel('Daily Return')
        ax.set_ylabel('Density')

    plt.tight_layout()
    # plt.show()
    logger.info(f'Main finishing')

if __name__ == "__main__":
    main()