# --------------
#Header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#Reading of the file
data=pd.read_csv(path)
data.replace(to_replace="-",value="Agender",inplace=True)
sns.countplot(x=data['Gender'])
sns.countplot(x=data['Alignment'])
newdf = data[['Combat','Strength']].copy()
covariance=newdf.cov().iloc[0,1]
std_Combat=newdf['Combat'].std()
std_Strength=newdf['Strength'].std()
pearson=covariance/(std_Combat*std_Strength)
print(pearson)
super_best_list_1=data['Total'].quantile(q=0.99)
df=data[data['Total']> super_best_list_1]
super_best_names=list(df['Name'])
# Code starts here



