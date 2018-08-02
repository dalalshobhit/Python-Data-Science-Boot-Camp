
# coding: utf-8

# ___
# 
# <a href='http://www.pieriandata.com'> <img src='../Pierian_Data_Logo.png' /></a>
# ___
# # Seaborn Exercises
# 
# Time to practice your new seaborn skills! Try to recreate the plots below (don't worry about color schemes, just the plot itself.

# ## The Data
# 
# We will be working with a famous titanic data set for these exercises. Later on in the Machine Learning section of the course, we will revisit this data, and use it to predict survival rates of passengers. For now, we'll just focus on the visualization of the data with seaborn:

# In[1]:


import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats
get_ipython().magic('matplotlib inline')


# In[2]:


sns.set_style('whitegrid')


# In[3]:


titanic = sns.load_dataset('titanic')


# In[4]:


titanic.head()


# # Exercises
# 
# ** Recreate the plots below using the titanic dataframe. There are very few hints since most of the plots can be done with just one or two lines of code and a hint would basically give away the solution. Keep careful attention to the x and y labels for hints.**
# 
# ** *Note! In order to not lose the plot image, make sure you don't code in the cell that is directly above the plot, there is an extra cell above that one which won't overwrite that plot!* **

# In[5]:


age_vs_fare = sns.JointGrid(x='fare',y='age',data=titanic, xlim=[-100,600], ylim=[-10,90])
age_vs_fare = age_vs_fare.plot_joint(plt.scatter)
age_vs_fare = age_vs_fare.plot_marginals(sns.distplot, kde=False, hist_kws=dict(edgecolor='gray'))
age_vs_fare = age_vs_fare.annotate(stats.pearsonr)
#age_vs_fare = age_vs_fare.ax_joint.xaxis.set_major_locator(ticker.)
#age_vs_fare = age_vs_fare.ax_marg_x.set_xlim(0,600)


# In[41]:





# In[6]:


fare = sns.distplot(titanic['fare'],bins=30,kde=False,hist_kws=dict(edgecolor='red',color='red'))


# In[44]:





# In[7]:


class_vs_age = sns.boxplot(x='class',y='age',data=titanic)


# In[45]:





# In[8]:


class_vs_age2 = sns.swarmplot(x='class',y='age',data=titanic)


# In[46]:





# In[9]:


sex_vs_count = sns.countplot(x='sex',data=titanic)


# In[47]:





# In[21]:


corr = titanic.corr()
titanic_heatmap = sns.heatmap(corr, cmap='coolwarm', vmin=-1, vmax=1)
titanic_heatmap.set_title('titanic.corr()')
plt.xticks(rotation=0)


# In[48]:





# In[29]:


age_vs_count_sex = sns.FacetGrid(titanic,col='sex')
age_vs_count_sex = age_vs_count_sex.map(plt.hist,'age',edgecolor='black')


# In[49]:





# # Great Job!
# 
# ### That is it for now! We'll see a lot more of seaborn practice problems in the machine learning section!
