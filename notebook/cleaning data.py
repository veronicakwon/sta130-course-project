#!/usr/bin/env python
# coding: utf-8

# In[6]:


import os
print(os.getcwd())  # This shows the folder where your notebook is running


# In[16]:


import pandas as pd

# Replace 'your_dataset.csv' with the actual file name
df = pd.read_csv('CSCS_data_anon.csv')  
#print(df.head())  # Show the first few rows to confirm it's loaded

cleaned_df = df[['GEO_housing_live_with_dogs', 'LONELY_change_pre_covid']].dropna()
print(cleaned_df)



# In[17]:


# Save the cleaned data to a CSV file
cleaned_df.to_csv('cleaned_data.csv', index=False)


# In[18]:


from IPython.display import FileLink

# Generate a link to download the file
FileLink('cleaned_data.csv')


# In[2]:


import pandas as pd

# Load the dataset from a CSV file
url = "CSCS_data_anon.csv"  # Replace with your file's URL or path
data = pd.read_csv(url)


import matplotlib.pyplot as plt

# Replace 'your_column_name' with the actual column name
data['GEO_housing_live_with_dogs'].hist(bins=10, edgecolor='black', figsize=(8, 6))

# Customize the plot
plt.title('Histogram of variable GEO_housing_live_with_dogs', fontsize=14)
plt.xlabel('Number of dogs per household', fontsize=12)
plt.ylabel('Count', fontsize=12)

# Show the plot
plt.show()


# for 2nd variable 

import seaborn as sns
import matplotlib.pyplot as plt

# Assuming 'category_column' is your categorical variable



sns.countplot(data=data, y='LONELY_change_pre_covid', palette='viridis')  # Use y-axis for categories
plt.ylabel('Loneliness change', fontsize=12)
plt.xlabel('Count', fontsize=12)

plt.show()

# Count the number of responses for each unique value
dog_counts = data['GEO_housing_live_with_dogs'].value_counts()

# Display the counts
print(dog_counts)




# In[3]:


# Count the number of responses for each unique category
loneliness_counts = data['LONELY_change_pre_covid'].value_counts()

# Display the counts
print(loneliness_counts)

