import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

import os
df = pd.read_csv(r"C:\Users\Lenovo\OneDrive\Documents\My_Projects\E-commerce_Customer_Review_Analyzer_Using_LP_&_Dashboard\cleaned_reviews.csv")

st.title("🛒 E-commerce Customer Review Analyzer")

if st.checkbox("Show Data"):
    st.write(df.head())

st.subheader("Sentiment Distribution")
sentiment_count = df['sentiment'].value_counts()

fig1, ax1 = plt.subplots()
sns.barplot(x=sentiment_count.index, y=sentiment_count.values, palette="Set2", ax=ax1)
st.pyplot(fig1)

st.subheader("Average Rating by Sentiment")
avg_rating = df.groupby('sentiment')['reviews.rating'].mean().reset_index()

fig2, ax2 = plt.subplots()
sns.barplot(data=avg_rating, x='sentiment', y='reviews.rating', palette="Pastel1", ax=ax2)
st.pyplot(fig2)
