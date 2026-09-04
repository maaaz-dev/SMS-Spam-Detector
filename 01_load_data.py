import pandas as pd

# Load dataset
df = pd.read_csv("data/SMSSpamCollection", sep="	", header=None)

# Add column names
df.columns = ["label", "message"]

# Convert labels
df["label"] = df["label"].map({"ham": 0, "spam": 1})

print(df.head())
print(df["label"].value_counts())
print(df.isnull().sum())
