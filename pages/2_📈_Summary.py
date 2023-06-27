import pandas as pd
import altair as alt
import millify
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
from millify import millify
import time



@st.cache_data
def data_df():
    df= pd.read_csv('C:/Users/Techa/streamlitdemo/dash/concat.csv')
    df['Date'] = pd.to_datetime(df['Date'])
    df['Month']= df['Date'].dt.month
    return df


#st.write('Monthly Streaming Per Year')



df = data_df()
#----------------------------
st.header("Streams Overview in the last one year")
fig, ax = plt.subplots()
sns.lineplot(x='Date', y='streams', data=df, ax=ax)
st.pyplot(fig)
#-------------------------------------
st.header('Yearly Pattern of the listeners and Streams ')
st.line_chart(
    df,
    x='Date',
    y= ["streams","listeners"]
)
#--------------------------------------
st.header("Overall Monthly Stream")
st.bar_chart(data=df, x='Month', y='streams')

#---------------------------------------
st.header("Number of Listeners Per Artist")
fig, ax = plt.subplots()
sns.barplot(data=df, y="ArtistName", x="listeners", ax=ax)
st.pyplot(fig)
#-------------------------------------------




