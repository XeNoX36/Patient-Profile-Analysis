import streamlit as st
import plotly.express as px
from extra import create_widgets

# Data Analysis 2
data, df1, df2, df3, df4, df5, df6, filtered_df, colours, colours2, tot_bill, tot_patient, rev_rate, tot_patient, patient_rate, avg_bill, avg_rate, avg_los, los_rate = create_widgets()
med_bill = filtered_df.groupby('Medical Condition')["Billing Amount"].sum().reset_index(name='sum')
med_test = filtered_df.groupby('Medical Condition')["Test Results"].value_counts().reset_index(name='count')
med_duration = filtered_df.groupby('Medical Condition')["Admission_Duration"].sum().reset_index(name='count')
growth_trend = filtered_df.groupby('Year')["Medical Condition"].value_counts().reset_index(name='count')

col1, col2 = st.columns([0.6, 0.4])
# Medical Conditions and billing
with col1:
    fig = px.bar(med_bill, x="Medical Condition", y="sum",  height=350, color="Medical Condition", color_discrete_sequence=colours2,
                 text="sum")
    fig.update_traces(textposition="outside", textfont_color="black")
    fig.update_layout(paper_bgcolor="#ebe9e5", plot_bgcolor="#ebe9e5",
                      legend=dict(font=dict(color="#474545"), title=dict(font=dict(color="#474545"))),
                      xaxis=dict(tickfont=dict(color="#474545"), title=dict(font=dict(color="#474545"))),
                      yaxis=dict(tickfont=dict(color="#474545"), title=dict(font=dict(color="#474545"))), margin=dict(l=20, r=20, t=35, b=20),
                      title=dict(text="   Bills Generated from Medical Conditions", font=dict(color="black")), showlegend=False)
    st.plotly_chart(fig, use_container_width=True)

# Metrics 2
with col2:
    metric1, metric2 = st.columns(2)
    with metric1:
        st.metric("**Total Patients**", value=tot_patient, delta=patient_rate, height=167, help="Total Patients That Were Admitted")
    with metric2:
        st.metric("**Total Billing Amount**", value=tot_bill, delta=rev_rate, height=167, help="Total Billing Amount That Was Generated")
    metric3, metric4 = st.columns(2)
    with metric3:
        st.metric("**Avg Length of Stay**", value=avg_los, delta=los_rate, height=167, help="Average Length of Stay of Patients")
    with metric4:
        st.metric("**Avg Billing Amount**", value=avg_bill, delta=avg_rate, height=167, help="Average Billing Amount That Was Generated")

col1, col2 = st.columns([0.4, 0.6])
# Medical Conditions and Their Test Results
with col1:
    st.markdown("###### Medical Conditions and Their Test Results")
    fig = px.bar(med_test, x="Medical Condition", y="count", text="count", color="Test Results", color_discrete_sequence=colours)
    fig.update_traces(textposition="inside")
    fig.update_layout(paper_bgcolor="#ebe9e5", plot_bgcolor="#ebe9e5",
                      legend=dict(font=dict(color="#474545"), title=dict(font=dict(color="#474545"))),
                      xaxis=dict(tickfont=dict(color="#474545"), title=dict(font=dict(color="#474545"))),
                      yaxis=dict(tickfont=dict(color="#474545"), title=dict(font=dict(color="#474545"))))
    st.plotly_chart(fig, use_container_width=True)

# Growth Trend of Each Conditions Per Year
with col2:
    st.markdown("###### Growth Trend of Each Conditions Per Year")
    fig = px.line(growth_trend, x="Year", y="count", color="Medical Condition", color_discrete_sequence=px.colors.qualitative.Vivid_r,
                  line_shape="spline")
    fig.update_layout(paper_bgcolor="#ebe9e5", plot_bgcolor="#ebe9e5",
                      legend=dict(font=dict(color="#474545"), title=dict(font=dict(color="#474545"))),
                      xaxis=dict(tickfont=dict(color="#474545"), title=dict(font=dict(color="#474545"))),
                      yaxis=dict(tickfont=dict(color="#474545"), title=dict(font=dict(color="#474545"))))
    st.plotly_chart(fig, use_container_width=True)
