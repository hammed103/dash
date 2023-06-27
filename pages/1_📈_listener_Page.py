import pandas as pd
import streamlit as st


st.write('Welcome to the Listener Page')

@st.cache_data
def data_df():
    df= pd.read_csv('C:/Users/Techa/streamlitdemo/dash/concat.csv')
    df['Date'] = pd.to_datetime(df['Date'])
    df['Month']= df['Date'].dt.month
    return df

df = data_df()
Total = df['listeners'].sum()

with st.expander("Total No of Listeners"):
    st.write(Total, 'listners')
    
#st.bar_chart(data=df, x='Month', y='listeners')
st.write(df)
