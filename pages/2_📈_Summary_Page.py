import pandas as pd
import altair as alt
import millify
import streamlit as st
from millify import millify



# @st.cache_data
# def data_df():
#     df= pd.read_csv('C:/Users/Techa/streamlitdemo/dash/concat.csv')
#     df['Date'] = pd.to_datetime(df['Date'])
#     df['Month']= df['Date'].dt.month
#     return df

#st.line_chart(data=data_df(), x='Date', y='streams')

#st.line_chart(data=data_df(), x='Month', y='streams')
#st.bar_chart(data=data_df(), x='ArtistName', y='streams')