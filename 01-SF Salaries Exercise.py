#!/usr/bin/env python
# coding: utf-8

# ___
# 
# <a href='http://www.pieriandata.com'> <img src='../../Pierian_Data_Logo.png' /></a>
# ___

# # SF Salaries Exercise 
# 
# Welcome to a quick exercise for you to practice your pandas skills! We will be using the [SF Salaries Dataset](https://www.kaggle.com/kaggle/sf-salaries) from Kaggle! Just follow along and complete the tasks outlined in bold below. The tasks will get harder and harder as you go along.

# ** Import pandas as pd.**

# In[1]:


import pandas as pd


# ** Read Salaries.csv as a dataframe called sal.**

# In[4]:


sal = pd.read_csv(r"/Users/krishnakanth/Downloads/Refactored_Py_DS_ML_Bootcamp-master/04-Pandas-Exercises/Salaries.csv")


# ** Check the head of the DataFrame. **

# In[14]:


sal


# ** Use the .info() method to find out how many entries there are.**

# In[6]:


sal.info()


# In[9]:





# In[7]:


sal.BasePay.mean()


# **What is the average BasePay ?**

# In[10]:





# ** What is the highest amount of OvertimePay in the dataset ? **

# In[8]:


sal.OvertimePay.max()


# In[11]:





# ** What is the job title of  JOSEPH DRISCOLL ? Note: Use all caps, otherwise you may get an answer that doesn't match up (there is also a lowercase Joseph Driscoll). **

# In[12]:


sal[sal.EmployeeName=='JOSEPH DRISCOLL']['JobTitle']


# In[12]:





# ** How much does JOSEPH DRISCOLL make (including benefits)? **

# In[13]:


sal[sal.EmployeeName=='JOSEPH DRISCOLL']['TotalPayBenefits']


# ** What is the name of highest paid person (including benefits)?**

# In[20]:


sal[sal['TotalPayBenefits']==sal['TotalPayBenefits'].max()]['EmployeeName']


# ** What is the name of lowest paid person (including benefits)? Do you notice something strange about how much he or she is paid?**

# In[21]:


sal[sal['TotalPayBenefits']==sal['TotalPayBenefits'].min()]['EmployeeName']


# ** What was the average (mean) BasePay of all employees per year? (2011-2014) ? **

# In[24]:


sal.groupby('Year').mean()['BasePay']


# ** How many unique job titles are there? **

# In[30]:


sal['JobTitle'].nunique()


# ** What are the top 5 most common jobs? **

# In[31]:


sal['JobTitle'].value_counts().head(5)


# ** How many Job Titles were represented by only one person in 2013? (e.g. Job Titles with only one occurence in 2013?) **

# In[34]:


sum(sal[sal['Year']==2013]['JobTitle'].value_counts()==1)


# ** How many people have the word Chief in their job title? (This is pretty tricky) **

# In[42]:


def cheif_string(title):
    if 'cheif' in title.lower().split():
        return True
    else:
        return False


# In[45]:


cheif_string('CHEIF MANAGER-METROPOLITAN TRANSIT AUTHORITY'
)


# In[50]:


sum(sal['JobTitle'].apply(lambda x: cheif_string(x)))


# ** Bonus: Is there a correlation between length of the Job Title string and Salary? **

# In[53]:


sal['title_len']=sal['JobTitle'].apply(len)
sal[['JobTitle','title_len']]


# In[55]:


sal[['TotalPayBenefits','title_len']].corr()


# # Great Job!
