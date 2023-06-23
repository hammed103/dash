import streamlit as st
import pandas as pd
import altair as alt

import streamlit as st

# Specify the path to the config file
st.set_option('config.file', 'config.toml')

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)


st.markdown('''# **Artist Overview**
''')
# Load market data from Binance API
df = pd.read_csv("concat.csv")


df["Date"] = pd.to_datetime(df.Date).dt.date
mini = df.Date.min()
maxi = df.Date.max()



year_range = st.slider(label="Compare With", min_value=mini, max_value=maxi, value=(mini, maxi))

st.header('**Selected Artists**')

df = df[df.Date.isin(year_range)]

#df = df.iloc[:,1:]
#df = df.set_index("Date")
# Create a dictionary to store the series
series_dict = {}
# Custom function for rounding values
def round_value(input_value):
    if input_value.values > 1:
        a = float(round(input_value, 2))
    else:
        a = float(round(input_value, 2))
    return a

col1, col2, col3,col4,col5,col6,col7,col8 = st.columns(8)


with st.sidebar:
    #st.write("## Task")
    source = st.selectbox(
        "Country :", df.Country.unique(),list(df.Country.unique()).index("World") )
    
    variable_filter = st.multiselect(label= 'Select The Artist',
                                options=list(set(df.ArtistName)),
                                default=list(set(df.ArtistName))[:4])
    year_range = st.slider(label="Start Date", min_value=mini, max_value=maxi, value=(mini, maxi))
    st.write("Compare with")
    sourcey = st.selectbox(
        "Country2 :", df.Country.unique(),list(df.Country.unique()).index("World") )
    
    variable_filtery = st.multiselect(label= 'Select The Artist2',
                                options=list(set(df.ArtistName)),
                                default=list(set(df.ArtistName))[:4])

df = df[df.Country == source]
df = df.groupby(['Date','ArtistName',"Country"]).sum().sort_values(['Date',"ArtistName","Country"],ascending=False)
df = df.rename_axis(["Date","ArtistName","Country"])
variable_dict = {}


# Calculate latest price change and price change percentage for each selected series
for i, column in enumerate(df.columns[1:-2]):
    latest_price = round(df[column].sum(),0)
    prev_price = df[column].iloc[0]
    price_change = latest_price - prev_price
    prev_price = round((price_change / prev_price) * 100,2)

    # Create a metrics price box
    if i%8 == 0 :
      col1.metric(column, latest_price,prev_price)
    elif i%8 == 1 :
      col2.metric(column, latest_price,prev_price)
    elif i%8 == 2 :
      col3.metric(column, latest_price,prev_price)
    elif i%8 == 3 :
      col4.metric(column, latest_price,prev_price)
    elif i%8 == 4 :
      col5.metric(column, latest_price,prev_price)
    elif i%8 == 5 :
      col6.metric(column, latest_price,prev_price)
    elif i%8 == 6 :
      col7.metric(column, latest_price,prev_price)
    elif i%8 == 7 :
      col8.metric(column, latest_price,prev_price)


st.header('**ARTIST VIEW**')
st.dataframe(df)

st.markdown("""
<script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
""", unsafe_allow_html=True)
