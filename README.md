# Y-intercept Coding Test: composing stock index

Name: Galym Torebayev

Email: torebaevgalym@gmail.com

A custom stock market index composer and etc. Solution Notebook located at notebooks/

## P.S. 

I'm more of dev guy, therefore I've added a some tech related paradigms like unit testing, logging and etc. I've tried my best in processing the assignment from the perspective of finance and math. Indeed it was a challenging task since by reading JD of Quantitative Developer (Platform Engineer), I didn't expect test to be this way. Anyways, I did my best

## Folder Structure

    .
    ├── src
    │   ├── __init__.py                  # Init
    │   ├── logger.py                    # Logger
    │   └── main.py                      # Main solution file / Alternative 1
    │
    ├── notebooks
    │   └── main.ipynb                   # Solution notebook / Alternative 2
    │
    ├── tests
    │   └── unit                         # Unit tests
    │
    ├── data
    │   ├── data_last.csv                # Last price file
    │   ├── data_mkt_cap.csv             # Market Cap file
    │   ├── data_sector.csv              # Sector file
    │   └── data_volume.csv              # Volume file
    │
    └── logs                             
        └── main.log                     # Logs

## Requirements

- Python 3.11

## Installation

Install dependencies:

```
pip install -r requirements.txt
```

## Usage

To run use one of following commands:

```
jupyter notebook
```

OR
 
```
python src/main.py
```

## Automated Tests

To test the application run (wasn't configured):

```
pytest tests
```