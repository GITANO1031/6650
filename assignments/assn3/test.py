import pandas as pd

df = pd.read_csv("sp_500.csv")
print(df.head())
# print(df["GICS Sector"].unique())
it_symbols = df[df["GICS Sector"].str.strip().eq("Financials")]["Symbol"].tolist()
print(it_symbols)