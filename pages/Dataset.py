import streamlit as st
import plotly.express as px
import pandas as pd
from extra import create_widgets

# Data Analysis 1
data, df1, df2, df3, df4, df5, df6, filtered_df, colours, colours2, tot_bill, tot_patient, rev_rate, tot_patient, patient_rate, avg_bill, avg_rate, avg_los, los_rate = create_widgets()

st.markdown("###### Patient Health Profile Dataset")
filtered_df
st.markdown("Data count: ")
filtered_df.shape
