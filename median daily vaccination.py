#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
#from pandasql import sqldf

df=pd.read_csv('https://raw.githubusercontent.com/tarikkranda/pi_datasets/main/country_vaccination_stats.csv')


maxvac=df.groupby(['country']).median()[['daily_vaccinations']]
maxvac['daily_vaccinations'].nlargest(3)
#pop_vaccines = data.groupby(["vaccines"])['total_vaccinations'].max()




# In[ ]:





# In[ ]:




