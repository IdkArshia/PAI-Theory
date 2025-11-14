import pandas as pd
df=pd.read_csv("Titanic-Dataset.csv")
report=[]
for col in df.columns:
    dtype=df[col].dtype
    missing=df[col].isnull().sum()
    percentage=(missing/len(df))*100
    report.append(f"{col}: dtype={dtype}, missing={missing}({percentage:.2f}%)")
with open("inspect_report.txt","w") as f:
    f.write("\n".join(report))

df['Age'] = df.groupby(['Pclass','Sex'])['Age'].transform(lambda x: x.fillna(x.median()))
embarked_mode=df['Embarked'].mode()[0]
df['Embarked']=df['Embarked'].fillna(embarked_mode)
df=df.drop(columns=['Cabin'])
df['FamilySize']=df['SibSp']+df['Parch']
df['IsAlone']=(df['FamilySize']==0).astype(int)
df['Age']=df['Age'].astype('int64')
df.to_csv("titanic_cleaned.csv",index=False)
