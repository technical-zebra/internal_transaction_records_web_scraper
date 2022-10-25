# importing pandas as pd
import pandas as pd

# Creating the dataframe
df = pd.read_csv("data_table.csv")

# First grouping based on "Team"
# Within each team we are grouping based on "Position"

df['Trade Date'] = pd.to_datetime(df['Trade Date'])

df['min'] = df.groupby('Ticker')['Trade Date'].transform('min')

df = df.sort_values(["min","Trade Date"], ascending=False).drop('min', axis=1)

#if necessary sorting also by tracks column
#sub_df = sub_df.sort_values(["max","tracks","score"], ascending=False).drop('max', axis=1)
print(df)

# Print the first value in each group
df.head()

df.to_csv('data_table2.csv')