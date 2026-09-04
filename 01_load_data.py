import pandas as pd

# Load dataset
df = pd.read_csv("data/SMSSpamCollection", sep="	", header=None)

# Add column names
df.columns = ["label", "message"]

print(df.head())
print(df.shape)
print(df["label"].value_counts())
print(df.isnull().sum())
