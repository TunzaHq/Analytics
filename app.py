!pip install streamlit
!pip install --upgrade streamlit seaborn

import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the data from CSV file
df = pd.read_csv('synthetic_data.csv')


# Display the scatter plot
st.subheader('Drop-off Points vs. App Login')
scatter_data = df[['Drop-off Points', 'App Login']]
sns.scatterplot(data=scatter_data, x='Drop-off Points', y='App Login')
st.pyplot()

# Bar Plot: Feature Usage vs. Experience Rating
st.subheader('Feature Usage vs. Experience Rating')
bar_data = df[['Feature Usage', 'Experience Rating']]
sns.barplot(data=bar_data)
st.pyplot()

# Line Plot: Feature Usage vs. Ease Rating
st.subheader('Feature Usage vs. Ease Rating')
line_data = df[['Feature Usage', 'Ease Rating']]
sns.lineplot(data=line_data)
st.pyplot()

# Violin Plot: Feature Usage vs. Responsiveness Rating
st.subheader('Feature Usage vs. Responsiveness Rating')
violin_data = df[['Feature Usage', 'Responsiveness Rating']]
sns.violinplot(data=violin_data)
st.pyplot(plt)

# Box Plot: Feature Usage vs. Accuracy Rating
st.subheader('Feature Usage vs. Accuracy Rating')
box_data = df[['Feature Usage', 'Accuracy Rating']]
sns.boxplot(data=box_data)
st.pyplot(plt)
