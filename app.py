import streamlit as st
import pandas as pd
from sklearn.preprocessing import LabelEncoder, MinMaxScaler
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv('synthetic_data.csv')  # Replace 'insurance_data.csv' with your dataset filename

# Create a LabelEncoder object
le = LabelEncoder()

# Encode categorical features
categorical_features = ['Gender', 'Occupation', 'Location', 'Policy Type']
for feature in categorical_features:
    df[feature] = le.fit_transform(df[feature])

# Scale numeric features
scaler = MinMaxScaler()
numeric_features = ['Age', 'Premium Amount', 'Claim Amount', 'Page Views', 'Feature Usage']
df[numeric_features] = scaler.fit_transform(df[numeric_features])

# Function to make personalized recommendations
def make_personalized_recommendations(customer_id):
    # Retrieve customer data
    customer_data = df[df['Customer ID'] == customer_id].iloc[0]

    # Compute similarity scores between the selected customer and all other customers
    df['Similarity Score'] = df[numeric_features].apply(lambda x: sum((x - customer_data[numeric_features]) ** 2), axis=1)

    # Get top 5 similar customers based on similarity scores
    similar_customers = df[df['Customer ID'] != customer_id].nlargest(5, 'Similarity Score')

    return similar_customers

# Streamlit app
def main():
    st.set_page_config(page_title='Insurance Analytics Dashboard')

    st.title('Insurance Analytics Dashboard')

    # Display new insurance policies sold
    st.header('New Insurance Policies Sold')
    new_policies_sold = df['Policy Type'].value_counts()
    st.bar_chart(new_policies_sold)

     # Display average premium revenue per policy
    st.header('Average Premium Revenue per Policy')
    avg_premium_revenue = df.groupby('Policy Type')['Premium Amount'].mean()
    st.bar_chart(avg_premium_revenue)

    # Customer satisfaction analysis
    st.header('Customer Satisfaction Analysis')
    satisfaction_ratings = df['Satisfaction Rating'].value_counts()
    st.bar_chart(satisfaction_ratings)

    # Personalized recommendations
    st.header('Personalized Recommendations')
    customer_id = st.text_input('Enter Customer ID:')
    if st.button('Get Recommendations'):
        if customer_id in df['Customer ID'].values:
            recommendations = make_personalized_recommendations(customer_id)
            st.write(recommendations)
        else:
            st.write('Invalid Customer ID')

if __name__ == '__main__':
    main()

