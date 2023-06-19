# Analytics

The repository contains a Streamlit app that incorporates recommender systems and data visualization charts. 
The app provides recommendations for policy amounts and feature ease based on customer attributes and ratings.

### The main features of the app include:
1. Data Visualization Charts: The app displays various charts to visualize the data, including heatmap, scatter plots, and bar plots. These charts provide insights into the relationships between different features and ratings.

   
2. Policy Recommender System: Using the customer's age, occupation, and policy type, the app computes a cosine similarity matrix to identify similar customers. It then recommends premium amounts for the selected customer based on the top similar customers.

3. Feature Ease Recommender System: Using drop-off points, experience rating, and responsiveness rating, the app computes a cosine similarity matrix to find customers with similar ratings. It recommends feature ease based on the top similar customers.




The app's user interface allows you to select a customer ID and view the recommended policy amounts and feature ease in separate tables. The charts provide additional visualizations for better understanding the data relationships.

Feel free to explore the [app](https://dynasty-29-britam-analytics-app-py-6efxzp.streamlit.app/)
