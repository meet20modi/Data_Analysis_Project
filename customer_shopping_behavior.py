import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("C:\\Users\Meet Modi\\OneDrive\\Desktop\\Data Analysis Project\\customer_shopping_behavior.csv")
#print(df.head())
print(df.info())
print(df.describe())

print(df.isnull().sum())

#Data Cleaning
df["Review Rating"] = df.groupby("Category")["Review Rating"].transform(lambda x: x.fillna(x.median()))
print(df.isnull().sum())
"""
All Columns name into lower case
df.columns = df.columns.str.lower()
df.columns = df.columns.str.replace(' ','_')

#replace column Name
df = df.rename(columns={'purchase_amount_(usd)': 'purchase_amount'})
print(df.columns)

labels = ["Young Adult","Adult","Middle-aged","Senior"]
df["age_group"] = pd.qcut(df["age"],q=4,labels=labels)

print(df[["age","age_group"]])

#create column purchase_frequency_days

frequency_mapping = {
    
   "Fortnightly" : 14, 
   "Weekly" :7, 
    "Monthly" : 30, 
    "Quarterly" :90, 
    "Bi-Weekly" : 14,
    "Annually" : 365,
    "Every 3 Months" : 90
}

fm = df["purchase_frequency_days"] = df["frequency_of_purchases"].map(frequency_mapping)
print(fm)

fp = df[["purchase_frequency_days","frequency_of_purchases"]].head(10)
print(fp)

discount_applied = df[["discount_applied","promo_code_used"]].head(10)
print(discount_applied)

promo = (df["discount_applied"]==df["promo_code_used"]).all()
print(promo)

#drop Promo_code_used Column
df = df.drop("promo_code_used",axis=1)
print(df.columns)

df.to_csv("C:\\Users\Meet Modi\\OneDrive\\Desktop\\Data Analysis Project\\Result.csv")
print("File Saved Successfully.....")"""


