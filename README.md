# 231021_case_study

## Requirements

- [Pre-commit](https://pre-commit.com/#install)
- Python 3.10 (e.g. using [pyenv](https://github.com/pyenv/pyenv) and [pyenv-virtualenv](https://github.com/pyenv/pyenv-virtualenv))

## Setup

- `pre-commit install`
- Create a virtual environment and install `requirements.txt`

## Notes

- The first (unnamed) column is not an id since there are duplicates but I also could not see a pattern in the data indicating its meaning.
- For some columns the decimal separator was unclear. Under normal circumstances I would talk to someone on the team sourcing the data to figure out what was wrong with the data collection.
- There seems to be some error happening in the data collection regularly on December 31st (only one data entry) and around end of March (138 instead of 144 data entries).
- For 42 Timestamps there are two data points. There should be some logic to decide which one to keep.

# Plotting

- Many features with seasonal effects (e.g. 5, 6 & 7)
- Features with increasing values over time: 0 & 34
- Outliers, e.g. Reactive Power (avg) (end of 2017)
- Gaps in data, e.g. Generator Speed (rpm) (2017/2018), 41 (Autumn 2018) or 39 (2020)
- Feature 62 seems to have a maximum value
- Feature 61 has several periods ist value 0

The visualisation of distributions for time series data makes less sense but still showed some interesting facts on the range of features:

- Feature 36: Very split distribution, either 0 or ~600.
- Feature 54, 57, 61: Nearly all 0 (~95%).
- Feature 62: Many values ~600 (~73%).
- Feature 13, 14 & 15: Nearly all ~400.
- Feature 20: Nearly all close to 0.
- Feature 23, 24 & 25: Very split distribution, either below 100 or ~360.
- Feature 28: Nearly all close to 50.
