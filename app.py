import streamlit as st
st.title("📊 Sales Analytics Dashboard")

st.set_page_config(
    page_title="Sales Dashboard",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>

.main {
    background-color: #0E1117;
    color: white;
}

.stMetric {
    background: linear-gradient(135deg, #1f1c2c, #928dab);
    padding: 20px;
    border-radius: 20px;
    text-align: center;
    box-shadow: 0px 4px 20px rgba(0,0,0,0.3);
}

h1 {
    color: #ffffff;
    text-align: center;
    font-size: 50px;
}

</style>
""", unsafe_allow_html=True)

#st.title("📊 Sales Analytics Dashboard")import streamlit as st

st.set_page_config(
    page_title="Sales Dashboard",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>

.main {
    background-color: #0E1117;
    color: white;
}

.stMetric {
    background: linear-gradient(135deg, #1f1c2c, #928dab);
    padding: 20px;
    border-radius: 20px;
    text-align: center;
    box-shadow: 0px 4px 20px rgba(0,0,0,0.3);
}

h1 {
    color: #ffffff;
    text-align: center;
    font-size: 50px;
}

</style>
""", unsafe_allow_html=True)

st.title("📊 Sales Analytics Dashboard")#import pandas as pd

# Read CSV file
#sales = pd.read_csv("sales.csv")

# print(sales)


# sales = pd.read_csv("sales.csv")

# Total salesimp
# print("Total Sales:", sales['Sales'].sum())

# Total profit
# print("Total Profit:", sales['Profit'].sum())
# product_sales = sales.groupby('Product')['Sales'].sum()

# print(product_sales)

# import pandas as pd
# import matplotlib.pyplot as plt

# sales = pd.read_csv("sales.csv")

# Group data
# product_sales = sales.groupby('Product')['Sales'].sum()

# Create chart
# plt.bar(product_sales.index, product_sales.values)

# plt.xlabel("Products")
# plt.ylabel("Sales")
# plt.title("Product Sales Analysis")

# plt.show()



import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Read data
sales = pd.read_csv("sales.csv")

st.title("Sales Analytics Dashboard")

# Show dataset
st.subheader("Sales Data")
st.write(sales)

# KPIs
st.subheader("Key Metrics")

st.write("Total Sales:", sales['Sales'].sum())
st.write("Total Profit:", sales['Profit'].sum())

# Product analysis
product_sales = sales.groupby('Product')['Sales'].sum()

# Chart
fig, ax = plt.subplots()
ax.bar(product_sales.index, product_sales.values)

ax.set_xlabel("Products")
ax.set_ylabel("Sales")
ax.set_title("Product Sales")

st.pyplot(fig)

import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="salesdb"
)

#cursor = conn.cursor()

#cursor.execute("SELECT * FROM sales")

#for row in cursor.fetchall():
 #   print(row)
  #  total_sales = df["Sales"].sum()

#st.metric("Total Sales", f"₹{total_sales}")

