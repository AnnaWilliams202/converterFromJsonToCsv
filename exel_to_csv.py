import pandas as pd

df = pd.read_excel('europe.xlsx') # Save the DataFrame as a CSV file
df.to_csv('europe_test.csv', index=False)