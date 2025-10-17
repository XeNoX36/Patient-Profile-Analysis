import streamlit as st
import plotly.express as px
from extra import create_widgets

# Data Analysis 1
data, df1, df2, df3, df4, df5, df6, filtered_df, colours, colours2, tot_bill, tot_patient, rev_rate, tot_patient, patient_rate, avg_bill, avg_rate, avg_los, los_rate = create_widgets()
gender_dist = filtered_df.groupby(['Gender', "Medical Condition"]).size().reset_index(name='count')
age_dist = filtered_df.groupby(['Age_groups', "Medical Condition"]).size().reset_index(name='count')
blood_dist = filtered_df.groupby(['Blood Type', "Medical Condition"]).size().reset_index(name='count')

col1, col2 = st.columns([0.6, 0.4])
# Gender Distribution
with col1:
    fig = px.sunburst(gender_dist, path=["Gender", "Medical Condition"], values="count",  height=350, color="Gender", color_discrete_sequence=colours2)
    fig.update_traces(textinfo='label+value', insidetextorientation="horizontal")
    fig.update_layout(paper_bgcolor='#ebe9e5', plot_bgcolor="#ebe9e5",
                      title=dict(text="   Gender Distribution and Medical Conditions", font=dict(color="black")),
                      margin=dict(l=20, r=20, t=35, b=20))
    st.plotly_chart(fig, use_container_width=True)

# Metrics 1
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

col1, col2 = st.columns([0.6, 0.4])
# age_distribution
with col1:
    st.markdown("###### Age Distribution and Medical Conditions")
    fig = px.bar(age_dist, x="count", y="Age_groups", text="count", color="Medical Condition", color_discrete_sequence=colours)
    fig.update_traces(textposition="inside", textangle=0)
    fig.update_layout(paper_bgcolor="#ebe9e5", plot_bgcolor="#ebe9e5",
                      legend=dict(font=dict(color="#474545"), title=dict(font=dict(color="#474545"))),
                      xaxis=dict(tickfont=dict(color="#474545"), title=dict(font=dict(color="#474545"))),
                      yaxis=dict(tickfont=dict(color="#474545"), title=dict(font=dict(color="#474545"))))
    st.plotly_chart(fig, use_container_width=True)

# Blood Types and Medical Conditions
with col2:
    st.markdown("###### Blood Types and Medical Conditions")
    fig = px.bar(blood_dist, x="count", y="Blood Type", text="count", color="Medical Condition", color_discrete_sequence=colours)
    fig.update_traces(textposition="inside")
    fig.update_layout(paper_bgcolor='#ebe9e5', plot_bgcolor="#ebe9e5",
                      legend=dict(font=dict(color="#474545"), title=dict(font=dict(color="#474545"))),
                      xaxis=dict(tickfont=dict(color="#474545"), title=dict(font=dict(color="#474545"))),
                      yaxis=dict(tickfont=dict(color="#474545"), title=dict(font=dict(color="#474545"))), showlegend=False)
    st.plotly_chart(fig, use_container_width=True)
