# Screen Time Analysis

Screen Time Analysis lets you know how much time you spend on what kind of applications and websites using your device. It provides a visual report of your screen time activities. This README provides guidance on analyzing screen time using Python.

## Screen Time Analysis Overview

Screen Time Analysis involves analyzing and generating reports on which applications and websites are used by the user and for how much time. Apple devices offer effective tools for creating screen time reports.

### Screen Time Analysis on iPhone

For screen time analysis, an ideal dataset is available containing:

- Date
- Usage of Applications
- Number of Notifications from Applications
- Number of times apps opened

You can download the dataset [here](link_to_dataset).

## Screen Time Analysis using Python

Let’s start the task of screen time analysis by importing the necessary Python libraries and the dataset:

```python
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

data = pd.read_csv("Screentime - App Details.csv")
print(data.head())
