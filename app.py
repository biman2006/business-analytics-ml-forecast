import streamlit as st

st.set_page_config(
    page_title="Business Analytics & revenue prediction App",
    layout="wide"
)

st.title("Business Analytics & sales Forecasting")
st.sidebar.success("Select a page from left")

st.markdown("""
<div style="padding:20px;border-radius:10px;
background: linear-gradient(90deg,#1f4037,#99f2c8);
color:white">
<h1>📊 Business Analytics Dashboard</h1>
<h4>Revenue • Profit • Sales Trend • Forecasting</h4>
</div>
""", unsafe_allow_html=True)

st.markdown("## 🔑 Key Business Metrics")

c1, c2, c3 = st.columns(3)

c1.metric("💰 Total Revenue", "$11.37M")
c2.metric("📈 Total Profit", "$282.8K")
c3.metric("📊 Profit Margin", "2.49%")





col1,col2=st.columns([2,1])

with col1:
    st.markdown(
        """   
    ### 🚀 What Does This App Do?


    This application helps business to:
    -Analyze **Company Revenue, Profit, Sales Trends**
    -Identify **Business Pattern**
    -prediction **Future Revenue**

    ALL ANALYSIS IS DONE USING:
    -** "SQL" For data extraction**
    -**"Python & Pandas" For Analysis**
    -**"Streamlit" For interactive dashboard**

"""



    )

    with col2:
        st.success(
            """ 
        -- TECH STACK:
        1> PYTHON
        2> SQL(MySQL)
        3> PANDAS 
        4> STREAMLIT
        """
)
        
        st.divider()


        st.markdown(" APP SECTIONS")

        c1,c2=st.columns(2)


with c1:
    st.info( 
        """   
     -- BUSINESS OVERVIEW --
     - Total Revenue
     - Total Profit
     - Profit Margin
     - Sales Trend
     - Top 10 Products by (profit,revenue)
     - Top 10 products by loss
     - Top 10 customers
     - Best Season
  """



    )

    with c2:
        st.success(
            """ 

        ## ML Forecast
        - User input based prediction
        - Revenue forecasting model
        - Business decision support
  """
        )


st.divider()

st.markdown(   

"""   

### USE THE SIDEBAR TO EXPLORE:
1> Business OVERVIEW
2> ML Forecast


"""

)

st.balloons()
st.snow()

