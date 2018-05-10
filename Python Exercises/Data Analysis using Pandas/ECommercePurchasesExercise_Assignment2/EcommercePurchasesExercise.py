
# coding: utf-8

# ___
# 
# <a href='http://www.pieriandata.com'> <img src='../../Pierian_Data_Logo.png' /></a>
# ___
# # Ecommerce Purchases Exercise
# 
# In this Exercise you will be given some Fake Data about some purchases done through Amazon! Just go ahead and follow the directions and try your best to answer the questions and complete the tasks. Feel free to reference the solutions. Most of the tasks can be solved in different ways. For the most part, the questions get progressively harder.
# 
# Please excuse anything that doesn't make "Real-World" sense in the dataframe, all the data is fake and made-up.
# 
# Also note that all of these questions can be answered with one line of code.
# ____
# ** Import pandas and read in the Ecommerce Purchases csv file and set it to a DataFrame called ecom. **

# In[1]:


import pandas as pd


# In[2]:


ecom = pd.read_csv("EcommercePurchases")
print(ecom)


# **Check the head of the DataFrame.**

# In[26]:


ecom.head(3)


# ** How many rows and columns are there? **

# In[13]:


ecom.shape


# ** What is the average Purchase Price? **

# In[14]:


ecom["Purchase Price"].mean()


# ** What were the highest and lowest purchase prices? **

# In[15]:


ecom["Purchase Price"].max()


# In[16]:


ecom["Purchase Price"].min()


# ** How many people have English 'en' as their Language of choice on the website? **

# In[18]:


ecom[ecom["Language"]=="en"].count()


# ** How many people have the job title of "Lawyer" ? **
# 

# In[19]:


ecom[ecom["Job"]=="Lawyer"].count()


# ** How many people made the purchase during the AM and how many people made the purchase during PM ? **
# 
# **(Hint: Check out [value_counts()](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.Series.value_counts.html) ) **

# In[20]:


ecom["AM or PM"].value_counts()


# ** What are the 5 most common Job Titles? **

# In[27]:


ecom["Job"].value_counts().nlargest(5)
#jobs = ecom.groupby("Job").value_counts()
#print(jobs.nlargest(5))


# ** Someone made a purchase that came from Lot: "90 WT" , what was the Purchase Price for this transaction? **

# In[51]:


ecom[ecom["Lot"]=="90 WT"]["Purchase Price"]


# ** What is the email of the person with the following Credit Card Number: 4926535242672853 **

# In[53]:


ecom[ecom["Credit Card"]==4926535242672853]["Email"]


# ** How many people have American Express as their Credit Card Provider *and* made a purchase above $95 ?**

# In[10]:


total = ecom["Address"][(ecom["CC Provider"]=="American Express") & (ecom["Purchase Price"]>95)]
print(total.count())


# ** Hard: How many people have a credit card that expires in 2025? **

# In[15]:


ecom["CC Exp Year"] = ecom["CC Exp Date"].str[3:]

exp_in_2025 = ecom[ecom["CC Exp Year"]=='25']
print(exp_in_2025.count())


# ** Hard: What are the top 5 most popular email providers/hosts (e.g. gmail.com, yahoo.com, etc...) **

# In[25]:


ecom["Providers"] = ecom["Email"].str.split("@").str[1]

print(ecom["Providers"].value_counts().nlargest(5))


# # Great Job!
