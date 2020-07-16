# --------------
#Importing header files
import pandas as pd
import scipy.stats as stats
import math
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.stats.weightstats import ztest
from statsmodels.stats.weightstats import ztest
from scipy.stats import chi2_contingency

import warnings

warnings.filterwarnings('ignore')
#Sample_Size
data=pd.read_csv(path)
sample_size=2000

#Z_Critical Score
z_critical = stats.norm.ppf(q = 0.95)  

data_sample = data.sample(n=sample_size, random_state=0)
#print(sample_data.shape)

sample_mean = data_sample['installment'].mean()
print("sample_mean: ",sample_mean)
sample_std = data_sample['installment'].std()

margin_of_error = z_critical * (sample_std / math.sqrt(sample_size))
print(margin_of_error)

confidence_interval = ((sample_mean-margin_of_error),(sample_mean+margin_of_error))
print("confidence_interval: ",confidence_interval)

true_mean = data['installment'].mean()
print("true_mean: ",true_mean)

#print(confidence_of_interval[0])
if confidence_interval[0] <= true_mean <=confidence_interval[1]:
    print('Yes')



sample_size=np.array([20,50,100])
fig, axes = plt.subplots(3, 1, figsize=(8, 4))
for i in range(len(sample_size)):
    m=[]
    for j in range(100):
        mean=data['installment'].sample(sample_size[i]).mean()
        m.append(mean)
        mean_series=pd.Series(m)
        axes[i].hist(mean_series)
plt.show()

data["int.rate"]=data["int.rate"].map(lambda x: str(x)[:-1])
data["int.rate"]
data["int.rate"]=data["int.rate"].astype(float)/100
data['int.rate']
z_statistic_1,p_value_1=ztest(x1=data[data["purpose"]=='small_business']["int.rate"],value=data["int.rate"].mean(),alternative='larger')
print(z_statistic_1)
print(p_value_1)


z_statistic_2,p_value_2=ztest(x1=data[data["paid.back.loan"]=='No']["installment"],x2=data[data["paid.back.loan"]=='Yes']["installment"])
print(z_statistic_2)
print(p_value_2)



critical_value=stats.chi2.ppf(q=0.95,df=6)
yes=data[data["paid.back.loan"]=='Yes']["purpose"].value_counts()
no=data[data["paid.back.loan"]=='No']["purpose"].value_counts()
observed=pd.concat([yes,no],1,keys=(['Yes','No']))
observed
chi2,p,dof,ex=stats.chi2_contingency(observed)
p














#Reading file


#Code starts here




