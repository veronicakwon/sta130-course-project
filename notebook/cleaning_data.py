#!/usr/bin/env python
# coding: utf-8

import os

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data")
RAW_PATH = os.path.join(DATA_DIR, "CSCS_data_anon.csv")
CLEANED_PATH = os.path.join(DATA_DIR, "cleaned_data.csv")

data = pd.read_csv(RAW_PATH)

# Keep only the two variables of interest, dropping incomplete responses
cleaned_df = data[["GEO_housing_live_with_dogs", "LONELY_change_pre_covid"]].dropna()
cleaned_df.to_csv(CLEANED_PATH, index=False)

# Histogram: number of dogs per household
cleaned_df["GEO_housing_live_with_dogs"].hist(bins=10, edgecolor="black", figsize=(8, 6))
plt.title("Histogram of variable GEO_housing_live_with_dogs", fontsize=14)
plt.xlabel("Number of dogs per household", fontsize=12)
plt.ylabel("Count", fontsize=12)
plt.show()

# Count plot: change in loneliness pre-COVID
sns.countplot(data=cleaned_df, y="LONELY_change_pre_covid", palette="viridis")
plt.ylabel("Loneliness change", fontsize=12)
plt.xlabel("Count", fontsize=12)
plt.show()

print(cleaned_df["GEO_housing_live_with_dogs"].value_counts())
print(cleaned_df["LONELY_change_pre_covid"].value_counts())
