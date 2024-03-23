# Screen Time Analysis
This README provides guidance on analyzing screen time using Python.

## Screen Time Analysis Overview

Screen Time Analysis involves analyzing and generating reports on which applications are used by the user and for how much time. Apple devices offer effective tools for creating screen time reports.  

For screen time analysis, an ideal dataset is available containing:  

- Date
- Usage of Applications
- Number of Notifications from Applications
- Number of times apps opened

You can download the dataset [here](https://www.kaggle.com/datasets/ruchi798/analyzing-screen-time).

## Screen Time Analysis using Python

Let’s start the task of screen time analysis by importing the necessary Python libraries and the dataset:

```python
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

data = pd.read_csv("Screentime - App Details.csv")
print(data.head())
