import os

import pandas as pd
# 1. Use pandas dataframe to view the data
mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}

myvar = pd.DataFrame(mydataset)

# print(myvar)

#
# # 2. check the version of the pandas
# print(pd.__version__)

# 3. Series -> a column in a table
a = [1,7,2]
myvar = pd.Series(a)
# print(myvar)

# 4. Labels
# print(myvar[0])

# 5. Create labels
myvar = pd.Series(a, index = ['X', 'Y', 'Z'])
# print(myvar)

# 6. Key/value objects as Series
calories = {"day1": 420, "day2": 370, "day3": 250, "day4": 400}

myvar = pd.Series(calories)
# print(myvar)

# 7. Series
data = {"calories": [420,390,103], "duration": [40, 50, 15]}

myvar = pd.Series(data)
# print(myvar)

# 8.Dataframes
myvar = pd.DataFrame(data)
# print(myvar)

# 9. Locate Row
# print(myvar.loc[[0,1]])

# 10. Named Indexes
df = pd.DataFrame(data,index=["Day1","Day2","Day3"])
# print(df)

# 11. Locate Named indexes
# print(df.loc["Day2"])

# 12.Load Files into a Dataframe
df = pd.read_csv('data.csv')
# print(df)
# print(df.to_string())  # this let the whole content being displayed

# 13. max_rows
# print(pd.options.display.max_rows)

pd.options.display.max_rows = 60
df = pd.read_csv('data.csv')
# print(df)

# 14. Pandas read Json
df = pd.read_json('data.js')
# print(df.to_string())

# 15. Viewing the data
df = pd.read_csv('data.csv')
# print(df.to_string() + "\n")

# print(df.head(10) )
# print(df.tail(10))

# 16. Info About the data
# print(df.info())

# 17. Data cleaning
"""
Bad data could be:
- Empty cells
- Data in wrong format
- Wrong Data
- Duplicates
Now you will learn how to deal with them
"""

# 18. remove rows
df = pd.read_csv('data.csv')
new_df = df.dropna()
# print(new_df.to_string())

# 19. Replace empty values
df = pd.read_csv('data.csv')
df.fillna(130, inplace = True)
# print(df.to_string())

# 20. Replace only for specified Columns
df = pd.read_csv('data.csv')
df.fillna({"Calories": 130}, inplace = True)

# 21. Replace using mean, median, or mode
df = pd.read_csv('data.csv')
x = df["Calories"].mode()[0]

df.fillna({"Calories": x}, inplace = True)
# print(df.to_string())

# 22. Data of wrong format
# Convert into a correct format
# to_datetime()
# df = pd.read_csv('data.csv')
# df['Date'] = pd.to_datetime(df['Date'], format="mixed")
# print(df.to_string())

# 23. Removing Rows with the null value in the "date" column
# df.dropna(subset = ['Date'], inplace = True)

# 24. Replacing Values
df.loc[7,'Duration'] = 45
# print(df.to_string())

# 25. Removing Rows
for x in df.index:
  if df.loc[x, "Duration"] > 120:
    df.drop(x, inplace = True)

# print(df.to_string())

# 26. Discovering Duplicates
# print(df.duplicated().sum())
df.drop_duplicates(inplace = True)
# print(df.duplicated().sum())

# 27. correlation
df = pd.read_csv('data.csv')
print(df.corr())

# 28. Plotting
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('data.csv')

df.plot()

df.plot(kind = 'scatter', x = 'Duration', y = 'Calories' )

plt.show()



