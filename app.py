import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the data from CSV file
df = pd.read_csv('synthetic_data.csv')

# Scatter Plot: Drop-off Points vs. App Login
st.subheader('Drop-off Points vs. App Login')
scatter_data = df[['Drop-off Points', 'App Login']]
st.scatter_chart(scatter_data)

# Bar Plot: Feature Usage vs. Experience Rating
st.subheader('Feature Usage vs. Experience Rating')
bar_data = df[['Feature Usage', 'Experience Rating']]
st.bar_chart(bar_data)

# Line Plot: Feature Usage vs. Ease Rating
st.subheader('Feature Usage vs. Ease Rating')
line_data = df[['Feature Usage', 'Ease Rating']]
st.line_chart(line_data)

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
