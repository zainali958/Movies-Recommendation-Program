# -*- coding: utf-8 -*-
"""Untitled11.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ANbIJLoisGzx2ffHTQxp8VzNf1XmNa9D
"""

import json
import pandas as pd

with open('movies.json', 'r') as file:
  data = json.load(file)

df = pd.DataFrame(data)

user_genre = input("Enter your favorite genre: ")
filtered_df = df[df['genre'].apply(lambda x: user_genre in x)]
print("Recommended movies based on your favorite genre:")
for index, row in filtered_df.iterrows():
  print(row['title'])