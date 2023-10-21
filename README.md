# 231021_case_study

## Requirements

- [Pre-commit](https://pre-commit.com/#install)
- Python 3.10 (e.g. using [pyenv](https://github.com/pyenv/pyenv) and [pyenv-virtualenv](https://github.com/pyenv/pyenv-virtualenv))

## Setup

- `pre-commit install`
- Create a virtual environment and install `requirements.txt`

## Analysis

- The first (unnamed) column is not an id since there are duplicates but I also could not see a pattern in the data indicating its meaning.
- For some columns the decimal separator was unclear. Under normal circumstances I would talk to someone on the team sourcing the data to figure out what was wrong with the data collection.
- Distribution of integer columns:
  - Feature 36: Very split distribution, either 0 or ~600.
  - Feature 54: Nearly all 0 (~95%).
  - Feature 57: Nearly all 0 (~95%).
  - Feature 61: Nearly all 0 (~94%).
  - Feature 62: Many values ~600 (~73%).
- Distribution of float columns:
  - Feature 13, 14 & 15: Nearly all ~400.
  - Feature 20: Nearly all close to 0.
  - Feature 23, 24 & 25: Very split distribution, either below 100 or ~360.
  - Feature 28: Nearly all close to 50.
- There seems to be some error happening in the data collection regularly on December 31st (only one data entry) and around end of March (138 instead of 144 data entries).
- For 42 Timestamps there are two data points. There should be some logic to decide which one to keep.
