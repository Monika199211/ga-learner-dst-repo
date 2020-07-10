# --------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataframe
df = pd.read_csv(path)

#Code starts here

p_a=len(df[df.fico>700])/len(df.fico)
p_b=len(df[df.purpose == "debt_consolidation"])/len(df.purpose)
df1=df[df.purpose == "debt_consolidation"]
p_a_b=len(df1[df1.fico>700])/len(df1.fico)
result=p_a_b==p_a
print(result)

prob_lp=len(df[df['paid.back.loan'] == 'Yes'])/len(df['paid.back.loan'])
prob_cs=len(df[df['credit.policy'] == "Yes"])/len(df['credit.policy'])
new_df=df[df['paid.back.loan'] == 'Yes']
prob_pd_cs=len(new_df[new_df['credit.policy'] == 'Yes'])/len(new_df['credit.policy'])
bayes=(prob_pd_cs*prob_lp)/prob_cs
print(bayes)

df1=df[df['paid.back.loan'] == 'No']
df1['purpose'].value_counts().plot(kind='bar')
df1.shape

inst_median=df['installment'].median()
inst_mean=df['installment'].mean()
df['installment'].hist(bins=50)
plt.axvline(x=inst_median,color='r')
plt.axvline(x=inst_mean,color='g')
plt.show()


