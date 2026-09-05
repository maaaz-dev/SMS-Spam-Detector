import pandas as pd

df = pd.read_csv("data/SMSSpamCollection", sep="\t", header=None)

df.columns = ["label", "message"]

df["label"] = df["label"].map({"ham": 0, "spam": 1})

print(df.head())
print(df["label"].value_counts())
print(df.isnull().sum())