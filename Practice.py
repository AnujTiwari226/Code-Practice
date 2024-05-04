import pandas as pd

my_df = pd.DataFrame({
    'c1': [['ts1', 'ts2', 'ts3', 'ts_name', 'ts_date'],
           ['ts1', 'ts2', 'ts3', 'ts_name', 'ts_date'],
           ['ts1', 'ts2', 'ts3', 'ts_name', 'ts_date'],
           ['ts1', 'ts2', 'ts3', 'ts_name', 'ts_date']],
    'r1': [[1, 2, 3, 'ts_01_name', 'ts_01_date'],
           [11, 22, 33, 'ts_002_name', 'ts_002_date'],
           [111, 222, 333, 'ts_333_name', 'ts_333_date'],
           [1111, 2222, 3333, 'ts_4444_name', 'ts_4444_date']]
})

# Transpose the DataFrame
transposed_df = pd.DataFrame(my_df['r1'].to_list(), columns=my_df['c1'].iloc[0])

# Set the column names to the first row values of 'c1'
transposed_df.columns = transposed_df.iloc[0]

# Drop the first row since it is now the column names
transposed_df = transposed_df.drop(0)

# Reset index
transposed_df.reset_index(drop=True, inplace=True)

print(transposed_df.columns.to_list())

print(transposed_df)
