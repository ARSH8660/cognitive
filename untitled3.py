# -*- coding: utf-8 -*-
"""Untitled3.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/15dqNFr_QIspAoJZT6ilVMqX1tffQQVau
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

roll_number = 12345
np.random.seed(roll_number)

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
categories = ['Electronics', 'Clothing', 'Home & Kitchen', 'Sports']

sales_data = np.random.randint(1000, 5001, size=(12, 4))
df = pd.DataFrame(sales_data, columns=categories, index=months)
print(df.head())
print(df.describe())

total_sales_category = df.sum()
total_sales_month = df.sum(axis=1)
df['Total Sales'] = total_sales_month

growth_rates = df[categories].pct_change().mean()
print(growth_rates)

df['Growth Rate'] = df['Total Sales'].pct_change() * 100

def apply_discount(row):
    if roll_number % 2 == 0:
        row['Electronics'] *= 0.9
    else:
        row['Clothing'] *= 0.85
    return row

df = df.apply(apply_discount, axis=1)

plt.figure(figsize=(10, 5))
for category in categories:
    plt.plot(df.index, df[category], marker='o', linestyle='-', label=category)
plt.xlabel('Month')
plt.ylabel('Sales')
plt.title('Monthly Sales Trends')
plt.legend()
plt.grid()
plt.show()

plt.figure(figsize=(8, 6))
sns.boxplot(data=df[categories])
plt.title('Sales Distribution by Category')
plt.show()

array = np.array([[1, -2, 3],[-4, 5, -6]])
abs_values = np.abs(array)
percentiles = {
    "flattened": np.percentile(array, [25, 50, 75]),
    "columns": np.percentile(array, [25, 50, 75], axis=0),
    "rows": np.percentile(array, [25, 50, 75], axis=1)
}
mean_values = {
    "flattened": np.mean(array),
    "columns": np.mean(array, axis=0),
    "rows": np.mean(array, axis=1)
}
median_values = {
    "flattened": np.median(array),
    "columns": np.median(array, axis=0),
    "rows": np.median(array, axis=1)
}
std_values = {
    "flattened": np.std(array),
    "columns": np.std(array, axis=0),
    "rows": np.std(array, axis=1)
}

a = np.array([-1.8, -1.6, -0.5, 0.5,1.6, 1.8, 3.0])
floor_values = np.floor(a)
ceil_values = np.ceil(a)
trunc_values = np.trunc(a)
round_values = np.round(a)

def swap_elements_list(lst, pos1, pos2):
    temp = lst[pos1]
    lst[pos1] = lst[pos2]
    lst[pos2] = temp
    return lst

def swap_elements_set(s, elem1, elem2):
    s_list = list(s)
    idx1, idx2 = s_list.index(elem1), s_list.index(elem2)
    s_list[idx1], s_list[idx2] = s_list[idx2], s_list[idx1]
    return set(s_list)

import numpy as np

array = np.array([[1, -2, 3], [-4, 5, -6]])
abs_values = np.abs(array)
print("Absolute Values:", abs_values)

percentiles_flattened = np.percentile(array, [25, 50, 75])
percentiles_columns = np.percentile(array, [25, 50, 75], axis=0)
percentiles_rows = np.percentile(array, [25, 50, 75], axis=1)
print("Flattened Percentiles:", percentiles_flattened)
print("Column-wise Percentiles:", percentiles_columns)
print("Row-wise Percentiles:", percentiles_rows)

mean_flattened = np.mean(array)
mean_columns = np.mean(array, axis=0)
mean_rows = np.mean(array, axis=1)
median_flattened = np.median(array)
median_columns = np.median(array, axis=0)
median_rows = np.median(array, axis=1)
std_flattened = np.std(array)
std_columns = np.std(array, axis=0)
std_rows = np.std(array, axis=1)

print("Flattened Mean:", mean_flattened)
print("Column-wise Mean:", mean_columns)
print("Row-wise Mean:", mean_rows)
print("Flattened Median:", median_flattened)
print("Column-wise Median:", median_columns)
print("Row-wise Median:", median_rows)
print("Flattened Standard Deviation:", std_flattened)
print("Column-wise Standard Deviation:", std_columns)
print("Row-wise Standard Deviation:", std_rows)

import numpy as np

a = np.array([-1.8, -1.6, -0.5, 0.5, 1.6, 1.8, 3.0])
floor_values = np.floor(a)
ceil_values = np.ceil(a)
trunc_values = np.trunc(a)
round_values = np.round(a)

print("Floor Values:", floor_values)
print("Ceil Values:", ceil_values)
print("Truncated Values:", trunc_values)
print("Rounded Values:", round_values)

def swap_elements(lst, pos1, pos2):
    temp = lst[pos1]
    lst[pos1] = lst[pos2]
    lst[pos2] = temp
    return lst

lst = [10, 20, 30, 40, 50]
pos1, pos2 = 1, 3
swapped_list = swap_elements(lst, pos1, pos2)
print("Swapped List:", swapped_list)

def swap_elements_in_set(s, elem1, elem2):
    s_list = list(s)
    if elem1 in s_list and elem2 in s_list:
        idx1, idx2 = s_list.index(elem1), s_list.index(elem2)
        s_list[idx1], s_list[idx2] = s_list[idx2], s_list[idx1]
    return set(s_list)

s = {10, 20, 30, 40, 50}
elem1, elem2 = 20, 40
swapped_set = swap_elements_in_set(s, elem1, elem2)
print("Swapped Set:", swapped_set)