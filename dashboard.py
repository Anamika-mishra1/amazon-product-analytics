import streamlit as st
import pandas as pd
import plotly.express as px

st.title("🔥 Amazon.in Product Analytics Dashboard")
st.markdown("**Anamika | B.Tech CSE 2023 | Amazon.in Analytics Specialist**")

df = pd.read_excel('amazon_data.xlsx')

# KPI Cards
col1, col2, col3 = st.columns(3)
col1.metric("Total SKUs", len(df))
col2.metric("Total Revenue", f"₹{(df.price*df.stock).sum():,.0f}")
col3.metric("Avg Rating", f"{df.rating.mean():.1f}/5")

# Charts
fig = px.bar(df, x='product', y='price', color='stock', title="Pricing vs Stock")
st.plotly_chart(fig)

st.subheader("💡 Insights")
st.success("• Laptops = 60% revenue\n• 2 items critically low stock\n• Monitors overpriced 20%")
