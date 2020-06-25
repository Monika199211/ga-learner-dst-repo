# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#Reading the file
data=pd.read_csv(path)

#Code starts here

# Step 1 
#Reading the file


#Creating a new variable to store the value counts
loan_status=data['Loan_Status'].value_counts()
loan_status
loan_status.plot(kind='bar')


#Plotting bar plot



# Step 2
#Plotting an unstacked bar plot

property_and_loan=data.groupby(['Property_Area','Loan_Status']).size().unstack().plot(kind='bar',stacked=False)
plt.xlabel("Property Area")
plt.ylabel("Loan Status")
plt.xticks(rotation=45)


#Changing the x-axis label


#Changing the y-axis label


#Rotating the ticks of X-axis


# Step 3
#Plotting a stacked bar plot

education_and_loan=data.groupby(["Education","Loan_Status"]).size().unstack().plot(kind='bar',stacked=True)
plt.xlabel("Education Status")
plt.ylabel("Loan Status")
plt.xticks(rotation=45)


#Changing the x-axis label


#Changing the y-axis label


#Rotating the ticks of X-axis


# Step 4 
#Subsetting the dataframe based on 'Education' column
graduate=data[data['Education'] == 'Graduate']
not_graduate=data[data['Education'] == 'Not Graduate']
data['LoanAmount'].plot(kind='density',label='Graduate')
data['LoanAmount'].plot(kind='density',label='Npt Graduate')
#Subsetting the dataframe based on 'Education' column


#Plotting density plot for 'Graduate'


#Plotting density plot for 'Graduate'


#For automatic legend display


# Step 5
#Setting up the subplots
fig ,(ax_1,ax_2,ax_3)=plt.subplots(3,1,figsize=(20,10))
ax_1.scatter(data['ApplicantIncome'],data['LoanAmount'])
ax_2.scatter(data['CoapplicantIncome'],data['LoanAmount'])
data['TotalIncome']=data['ApplicantIncome']+data["CoapplicantIncome"]
ax_3.scatter(data['TotalIncome'],data['LoanAmount'])


#Plotting scatter plot


#Setting the subplot axis title


#Plotting scatter plot


#Setting the subplot axis title


#Creating a new column 'TotalIncome'


#Plotting scatter plot



#Setting the subplot axis title



