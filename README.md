# STA130 Course Project

Dec 2024

Course project for STA130 (Introduction to Statistical Reasoning and Data Science) analyzing anonymized data from the Canadian Social Connection Survey (CSCS), which covers demographics, COVID-19 behaviours, wellness/burnout measures, and social connection activities.

## Repository structure

```
data/
  CSCS_data_anon.csv        Raw anonymized survey data (11,561 responses x 1,794 variables)
  cleaned_data (2).csv      Cleaned subset: housing with dogs vs. change in loneliness pre-COVID

notebook/
  cleaning data.py          Script that filters/cleans the raw data and produces exploratory plots

reports/
  Individual Project Proposals (1).ipynb   Analysis proposals with research questions and variables
  STA130 Course Project.pdf                Course project handout/instructions
```

## Data cleaning

[`notebook/cleaning data.py`](notebook/cleaning data.py) reads `CSCS_data_anon.csv`, selects the
`GEO_housing_live_with_dogs` and `LONELY_change_pre_covid` columns, drops missing values, and saves
the result to `cleaned_data.csv`. It also produces a histogram of dog ownership and a count plot of
loneliness change.

## Analysis proposals

[`reports/Individual Project Proposals (1).ipynb`](reports/Individual Project Proposals (1).ipynb)
outlines candidate research questions (e.g., the association between social media time and interest
in activities among people under 30) along with the predictor/outcome variables and planned
visualizations for each.

## Requirements

- Python 3
- pandas, matplotlib, seaborn
