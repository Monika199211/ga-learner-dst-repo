# --------------
# import packages

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt 
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

# Load Offers
Offer=pd.read_excel(path,sheet_name=0)
# Load Transactions
Transactions=pd.read_excel(path,sheet_name=1)
Transactions['n']=1
# Merge dataframes
df=pd.merge(Transactions,Offer)
# Look at the first 5 rows
df.head()
# create pivot table
matrix=df.pivot_table(index='Customer Last Name',columns='Offer #',values='n')
# replace missing values with 0
matrix.fillna(0,inplace=True)
# reindex pivot table

matrix.reset_index(inplace=True)
# display first 5 rows
matrix.head()

# initialize KMeans object
cluster=KMeans(n_clusters=5,init='k-means++',max_iter=300,n_init=10,random_state=0)
# create 'cluster' column
matrix['cluster']=cluster.fit_predict(matrix[matrix.columns[1:]])

# initialize pca object with 2 components

pca=PCA(n_components=2,random_state=0)

# create 'x' and 'y' columns donoting observation locations in decomposed form

matrix['x']=pca.fit_transform(matrix[matrix.columns[1:]])[:,0]
matrix['y']=pca.fit_transform(matrix[matrix.columns[1:]])[:,1]

# dataframe to visualize clusters by customer names

clusters=matrix.iloc[:,[0,33,34,35]]
clusters
# visualize clusters
clusters.plot.scatter(x='x',y='y',c='cluster',colormap='viridis')


# merge 'clusters' and 'transactions'





# merge `data` and `offers`




# initialzie empty dictionary


# iterate over every cluster

    # observation falls in that cluster

    # sort cluster according to type of 'Varietal'

    # check if 'Champagne' is ordered mostly

        # add it to 'champagne'

data=pd.merge(clusters,Transactions,on='Customer Last Name')
data=pd.merge(data,Offer)
champagne={}
# get cluster with maximum orders of 'Champagne' 
# iterate over every cluster
for i in data['cluster'].unique():
    # observation falls in that cluster
    new_df = data[data['cluster'] == i]
    # sort cluster according to type of 'Varietal'
    counts = data['Varietal'].value_counts(ascending = False)
    #print("\n",counts)
    # check if 'Champagne' is ordered mostly
    if (counts.index[0] == 'Champagne'):
        # add it to 'champagne'
        champagne={i:counts[0]}
#print("cluster dict: ",champagne)

# get cluster with maximum orders of 'Champagne' 
cluster_champagne = max(champagne.keys()) 

# print out cluster number
print("cluster_champagne: ", cluster_champagne)
# print out cluster number
discount  = {}

# iterate over cluster numbers
for cluster in data['cluster'].unique():
    # dataframe for every cluster
    new_df = data[data['cluster'] == cluster]
    # average discount for cluster
    count = new_df['Discount (%)'].sum()/new_df['Discount (%)'].count()
    # adding cluster number as key and average discount as value 
    discount[cluster] = count

print("discount dict: ", discount)
# cluster with maximum average discount
cluster_discount  = max(discount, key = discount.get)
print("cluster_discount: ", cluster_discount)
# Code ends here


# empty dictionary


# iterate over cluster numbers



