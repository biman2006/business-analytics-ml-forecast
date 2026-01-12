import streamlit as st
import pandas as pd
import pickle

model=pickle.load(open("business_forecast_pipeline.pkl", "rb"))

st.header("Sales Forecast:")

year=st.number_input(
    "Enter Year",
    min_value=2020,
    max_value=2035,
    value=2025
)

month_name=st.selectbox(
    "Select Month",
    ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
)

prev_month_revenue=st.number_input(
    "Previous Month Revenue",
    min_value=0.0,
    value=100000.0
)


month_map={
    "January": 1, "February":2, "March":3, "April":4, "May":5, "June": 6, "July": 7, "August": 8, "September": 9, "October": 10, "November": 11, "December":12
}

if st.button("Predict Revenue"):
    test_input=pd.DataFrame(
        {
            "year": [year],
            "month_name":[month_name],
            "month":[month_map[month_name]],
            "prev_month_revenue": [prev_month_revenue]
        }
    )

    prediction=model.predict(test_input)[0]


    st.success(f"Predicted Revenue:{prediction:,.0f}")