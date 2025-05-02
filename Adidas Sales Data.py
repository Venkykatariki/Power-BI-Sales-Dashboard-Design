#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[5]:


df = pd.read_csv(r'C:\Users\venka\Downloads\Adidas Sales Data (2020-2021).csv')


# In[7]:


df.info()
df.head()


# In[9]:


print(df.columns.tolist())


# In[11]:


df['Invoice Date'] = pd.to_datetime(df['Invoice Date'], errors='coerce')
df['Month-Year'] = df['Invoice Date'].dt.to_period('M').astype(str)
df[['Invoice Date', 'Month-Year']].head()


# In[13]:


import pandas as pd

# Load data
df = pd.read_csv(r'C:\Users\venka\Downloads\Adidas Sales Data (2020-2021).csv')

# Handle null values
# Drop rows with nulls in critical columns
critical_columns = ['Retailer', 'Product', 'Total Sales', 'Invoice Date']
df = df.dropna(subset=critical_columns)

# Impute nulls in numerical columns with median
numerical_columns = ['Price per Unit', 'Units Sold', 'Total Sales', 'Operating Profit']
for col in numerical_columns:
    df[col] = df[col].fillna(df[col].median())

# Correct data formats
# Convert Invoice Date to datetime
df['Invoice Date'] = pd.to_datetime(df['Invoice Date'], errors='coerce')

# Ensure numerical columns are float
for col in numerical_columns:
    df[col] = df[col].astype(float)

# Ensure categorical columns are strings
categorical_columns = ['Retailer', 'Region', 'State', 'City', 'Product', 'Sales Method']
for col in categorical_columns:
    df[col] = df[col].astype(str)

# Save cleaned data
df.to_csv('Adidas_Sales_Data_Cleaned.csv', index=False)
print("Cleaned data saved to 'Adidas_Sales_Data_Cleaned.csv'")


# In[ ]:




