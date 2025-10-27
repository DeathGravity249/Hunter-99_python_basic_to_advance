import streamlit as st
import pandas as pd
import numpy as np

## Title fof the application 
st.title("Hello this is begining of new era")

## Display a Simple text
st.write("this is a sample text")
df=({
    "first column ":[1,2,3,4],
    "second column " : [10,20,30,40]
    })

# Display the Dataframe
st.write("Here is the datframe")
st.write(df)

## create a line chart 
 
chart_data=pd.DataFrame(
    np.random.randn(20,3),columns=["a","b","c"]

)
st.line_chart(chart_data)