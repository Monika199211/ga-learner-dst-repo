# --------------
#Importing header files
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler, LabelEncoder




#Loading the data
data=pd.read_csv(path)
data['Rating'].plot(kind='hist')
plt.show()
#Code starts here
data=data[data['Rating']<=5]
data['Rating'].plot(kind='hist')
plt.show()

nulls=data.isnull().sum()
data.dropna(inplace=True)


plt.figure(figsize=(10,10))
cat=sns.catplot(x='Category',y='Rating',kind='box',data=data,height=8)
cat.set_xticklabels(rotation=90)
plt.title("Rating vs Category boxplot",size=20)

data['Genres']=data['Genres'].str.split(";",expand = True) [0]

mean_rating=data.groupby('Genres')['Rating'].mean()
max_rating=data.groupby('Genres')['Rating'].max()
min_rating=data.groupby('Genres')['Rating'].min()
rating_data={
        'mean_rating': mean_rating,
        'max_rating': max_rating,
        'min_rating': min_rating}
rating_data_df = pd.DataFrame(rating_data, columns = ['mean_rating', 'max_rating', 'min_rating'])
rating_data_df
data['Installs'].value_counts()
data['Installs']=data['Installs'].str.replace(",","") 
data['Installs']=data['Installs'].str.replace("+","") 
data['Installs'].value_counts()
data['Installs'].astype(int)
data['Price']=data['Price'].str.replace("$","") 
data['Price']=data['Price'].astype(float)
le=LabelEncoder()
le.fit(data['Installs'])
data['Installs']=le.transform(data['Installs'])
sns.regplot(x=data['Installs'],y=data['Rating'],color='teal')
sns.regplot(x=data['Price'],y=data['Rating'],color='teal')
data['Last Updated'] = pd.to_datetime(data["Last Updated"])
plt.figure(figsize=(15,15))
plt.plot(data['Last Updated'],data['Rating'])




