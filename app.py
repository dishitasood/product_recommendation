import streamlit as st
import pandas as pd
from main import Product_Recommender, similarity_matrix, df  # import everything you need

st.set_page_config(page_title="🛍️ Product Recommender", layout="centered")

st.title("🛒 Product Recommendation System")
st.write("Find similar products based on description.")

descriptions = df['Description'].tolist()

# Dropdown to select a product
selected_product = st.selectbox("Choose a product:", descriptions)

if st.button("Show Recommendations"):
    product_index = df[df['Description'] == selected_product].index[0]
    recommendations = Product_Recommender(product_index)

    st.subheader("🔁 Similar Products:")
    for _, row in recommendations.iterrows():
        st.markdown(f"**{row['Description'].capitalize()}**  \n`StockCode: {row['StockCode']}`")
        st.write("---")
