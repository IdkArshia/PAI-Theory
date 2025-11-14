import pandas as pd

df=pd.read_csv("titanic_cleaned.csv")
fares=pd.read_csv("ticket_fares.csv")

df = df.merge(fares,on="Ticket",how="left")
df.columns = df.columns.str.strip()

if "Fare_y" in df.columns:
    df["Fare"] = df["Fare_y"]

bins=[0,12,19,59,120]; labels=['Child','Teen','Adult','Senior']
df['AgeGroup']=pd.cut(df['Age'],bins=bins,labels=labels, right=True)
survival_by_sex_age=df.pivot_table(values="Survived",index="Sex",
 columns="AgeGroup",aggfunc="mean")

print(survival_by_sex_age)
survival_by_sex_age.to_csv("survival_by_sex_age.csv")
class_survival=df.groupby("Pclass")["Survived"].mean()
print(class_survival)

class_survival.to_csv("class_survival.csv")
df["FareBin"]=pd.qcut(df["Fare"],q=4, labels=["Low","Medium","High","VeryHigh"])
fare_survival=df.groupby("FareBin")["Survived"].mean()
print(fare_survival)
fare_survival.to_csv("fare_survival.csv")

with open("report.txt","w") as f:
    f.write("Hypothesis 1: Women and children first.\n")
    f.write("Based on the survival rates grouped by sex and age group, women show a substantially higher survival rate than men across all age groups. Children, particularly female children, also show higher survival rates compared to adult males. These results support the hypothesis that 'women and children first' influenced survival outcomes.\n\n")
    f.write("Hypothesis 2: The wealthy had a higher survival rate.\n")
    f.write("Both methods used to approximate wealth—Passenger Class and Fare quantile bins—show that passengers in higher classes and those who paid higher fares had significantly higher survival rates. Therefore, the data supports the hypothesis that wealthier passengers were more likely to survive.\n")
