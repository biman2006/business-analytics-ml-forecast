import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt



st.title("Business Analysis Of The Company")
st.write("Data Analysis Project")

Total_revenue=pd.read_csv("Company_Revenue.csv")
st.subheader("Total Revenue Of The Company:")
st.dataframe(round(Total_revenue,2))


Total_Profit=pd.read_csv("Total_Profit.csv")
st.subheader("Total Profit Of The Company:")
st.dataframe(round(Total_Profit,2))


Profit_Margin=pd.read_csv("Profit_margin.csv")
st.subheader("Profit Margin Of the Company:")
st.dataframe(round(Profit_Margin,2))


Sales_trend=pd.read_csv("Sales_Trend.csv")
st.subheader("Sales Trend Of The Company:")
st.dataframe(round(Sales_trend,2))


st.bar_chart(Sales_trend.set_index("year")[["Total_Revenue"]])
st.bar_chart(Sales_trend.set_index("month")[["Total_Revenue"]])



Top_10_sales_product=pd.read_csv("ToP_sales_product.csv")
st.subheader("Top 10 Product By Sales:")
st.dataframe(round(Top_10_sales_product,2))

st.bar_chart(Top_10_sales_product.set_index("Category")[["Total_Sales"]])


Top_Profit_Product=pd.read_csv("Top_Profit_Product.csv")
st.subheader("Top 10 Product By profit:")
st.dataframe(round(Top_Profit_Product,2))
st.bar_chart(Top_Profit_Product.set_index("Category")["profit"])



Top_10_product_revenue_profit=pd.read_csv("Top_product_revenue_profit.csv")
st.subheader("Top 10 product By Revenue With Profit")
st.dataframe(round(Top_10_product_revenue_profit,2))

st.bar_chart(Top_10_product_revenue_profit.set_index("Category")[["Total_Revenue"]])


Top_10_product_loss=pd.read_csv("Loss_product.csv")
st.subheader("TOP 10 PRODUCT BY LOSS, WITH REVENUE:")
st.dataframe(round(Top_10_product_loss,2))
st.bar_chart(Top_10_product_loss.set_index("Product Name")[["Total_loss"]].abs())


Top_customers_revvenue=pd.read_csv("top_customer_revvenue.csv")
st.subheader("TOP 10 CUSTOMER WHO GENERATE HIGHEST REVENUE WITH CITY")
st.dataframe(round(Top_customers_revvenue,2))
st.bar_chart(Top_customers_revvenue.set_index("Customer Name")[["Total_Revenue"]])


Top_customer_profit=pd.read_csv("Top_customer_profit.csv")
st.subheader("TOP 10 CUSTOMER WHO GENERATE HIGHEST REVENUE WITH CITY")

st.dataframe(round(Top_customer_profit,2))
st.bar_chart(Top_customer_profit.set_index("Customer Name")[["Total_Profit"]])


Best_season=pd.read_csv("Best_season.csv")
st.subheader(" BEST AND WORST MONTH BASED ON REVENUE")
st.dataframe(round(Best_season,2))

st.bar_chart(Best_season.sort_values("Total_Revenue", ascending=False).set_index("month_name")[["Total_Revenue"]])