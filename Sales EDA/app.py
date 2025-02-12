import streamlit as st
import pickle
import matplotlib.pyplot as plt
import seaborn as sns

with open("sales_analysis.pkl", "rb") as file:
    data_dict = pickle.load(file)

monthly_sales = data_dict["monthly_sales"]
top_product = data_dict["top_product"]
total_revenue = data_dict["total_revenue"]



st.title("📊 Sales Data Analysis Dashboard")


st.write("## 💰 Total Revenue: ", f"${total_revenue:,.2f}")


if st.button("📈 Show Monthly Sales Trend"):
    plt.figure(figsize=(12, 6))
    sns.lineplot(x=monthly_sales.index.astype(str), y=monthly_sales.values, marker="o", color="orange")
    plt.title("Monthly Sales Trend", fontsize=14, fontweight='bold', color='darkred')
    plt.xlabel("Month", fontsize=12)
    plt.ylabel("Revenue ($)", fontsize=12)
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    st.pyplot(plt)


if st.button("🏆 Show Best-Selling Product Lines"):
    plt.figure(figsize=(12, 6))
    sns.barplot(x=top_product.head(10).index, y=top_product.head(10).values, palette="viridis")
    plt.xticks(rotation=45)
    plt.title("Top 10 Best-Selling Product Lines", fontsize=14, fontweight='bold', color='purple')
    plt.xlabel("Product Line", fontsize=12)
    plt.ylabel("Revenue ($)", fontsize=12)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    st.pyplot(plt)

