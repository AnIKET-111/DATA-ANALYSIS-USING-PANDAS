import pandas as pd
from pandas_profiling import ProfileReport

# prompt user for file path
file_path = input("Enter path to CSV file: ")

# read CSV file into a Pandas DataFrame
df = pd.read_csv(file_path)

# print the DataFrame
print(df)

# generate a report
profile = ProfileReport(df)
profile.to_file(output_file="annual.html")
