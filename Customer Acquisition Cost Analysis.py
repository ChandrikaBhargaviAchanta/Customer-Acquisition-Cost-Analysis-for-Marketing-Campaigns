#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import plotly.express as px
import plotly.io as pio
import plotly.graph_objects as go
pio.templates.default = "plotly_white"

data = pd.read_csv("downloads/customer_acquisition_cost_dataset.csv")
print(data.head())


# In[5]:


data.info()


# In[6]:


#calculate the customer acquistion cost
data['CAC'] = data['Marketing_Spend'] / data['New_Customers']
print(data['CAC'])


# In[7]:


#CAC by Marketing Channels 

fig1 = px.bar(data, x='Marketing_Channel', 
              y='CAC', title='CAC by Marketing Channel')
fig1.show()


# In[8]:


# Relationship between new customers acquired and CAC
fig2 = px.scatter(data, x='New_Customers', 
                  y='CAC', color='Marketing_Channel', 
                  title='New Customers vs. CAC', 
                  trendline='ols')
fig2.show()


# In[9]:


# Summary statistics of all the marketing channels
summary_stats = data.groupby('Marketing_Channel')['CAC'].describe()
print(summary_stats)


# In[15]:


#calculating conversion rate of the marketing campaign
data['Conversion_Rate'] = data['New_Customers'] / data['Marketing_Spend'] * 100
print(data['Conversion_Rate'])


# In[16]:


# Conversion Rates by Marketing Channel
fig = px.bar(data, x='Marketing_Channel', 
             y='Conversion_Rate', 
             title='Conversion Rates by Marketing Channel')
fig.show()


# In[17]:


# Calculate the break-even customers for this marketing campaign
data['Break_Even_Customers'] = data['Marketing_Spend'] / data['CAC']

fig = px.bar(data, x='Marketing_Channel', 
             y='Break_Even_Customers', 
             title='Break-Even Customers by Marketing Channel')
fig.show()


# In[18]:


# compare the actual customers acquired with the break-even customers for each marketing channel
fig = go.Figure()

# Actual Customers Acquired
fig.add_trace(go.Bar(x=data['Marketing_Channel'], y=data['New_Customers'],
                     name='Actual Customers Acquired', marker_color='royalblue'))

# Break-Even Customers
fig.add_trace(go.Bar(x=data['Marketing_Channel'], y=data['Break_Even_Customers'],
                     name='Break-Even Customers', marker_color='lightcoral'))

# Update the layout
fig.update_layout(barmode='group', title='Actual vs. Break-Even Customers by Marketing Channel',
                  xaxis_title='Marketing Channel', yaxis_title='Number of Customers')


# In[ ]:




