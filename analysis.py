import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

# Load the data
data = pd.read_csv("Screentime-App-Details.csv")
print(data.head())

#Checking for null values
print(data.isnull().sum())

#checking for descriptive statistics
print(data.describe())

#analyzing the screen time of the apps
# creates a bar chart using the data DataFrame
# The x-axis represents the 'Date', the y-axis represents 'Usage'
fig = px.bar(data, x='Date', y='Usage', color="App", title='Screen Time of the Apps')
fig.show()

#analyzing number of notifications sent by the apps
fig = px.bar(data, x='Date', y='Notifications', color="App", title='Number of Notifications Sent by the Apps')
fig.show()

#analyzing the number of time the apps were opened
fig = px.bar(data, x='Date', y='Times opened', color="App", title='Number of Times the Apps were Opened')
fig.show()

#1. Correlation between the number of notifications and the screen time of the apps
# creates a scatter plot using the data DataFrame
# The x-axis represents the 'Notifications', the y-axis represents 'Usage'
fig = px.scatter(data, x='Notifications', y='Usage', size="Notifications", trendline="ols", title='Correlation between the number of notifications and the screen time of the apps')
fig.show()

#There’s a linear relationship between the number of notifications and the amount of usage. It means that more notifications result in more use of smartphones.

#2. Correlation between the number of times the apps were opened and the screen time of the apps   
# creates a scatter plot using the data DataFrame
# The x-axis represents the 'Times opened', the y-axis represents 'Usage'
fig = px.scatter(data, x='Times opened', y='Usage', size="Times opened", trendline="ols", title='Correlation between the number of times the apps were opened and the screen time of the apps')
fig.show()

#3. Daily Usage Analysis of the Apps
# creates a line chart using the data DataFrame
# The x-axis represents the 'Date', the y-axis represents 'Usage'
fig = px.line(data, x='Date', y='Usage', color="App", title='Daily Usage Analysis of the Apps')
fig.show()

#4. Notification Analysis of the Apps
# creates a line chart using the data DataFrame
# The x-axis represents the 'Date', the y-axis represents 'Notifications'
fig = px.line(data, x='Date', y='Notifications', color="App", title='Notification Analysis of the Apps')
fig.show()