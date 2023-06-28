import pandas as pd
import altair as alt
import millify
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
from millify import millify
import time


st.write('Welcome to the Listener Page')

@st.cache_data
def data_df():
    df= pd.read_csv('streamlit_navbar-main\concat.csv')
    df['Date'] = pd.to_datetime(df['Date'])
    df['Month']= df['Date'].dt.month
    return df

df = data_df()


st.header("Number of Listeners Per Artist")
fig, ax = plt.subplots()
sns.barplot(data=df, y="ArtistName", x="listeners", ax=ax)
st.pyplot(fig)

