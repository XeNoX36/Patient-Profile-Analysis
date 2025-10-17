import pandas as pd
import streamlit as st
import json
import os


@st.cache_data
def read_data():
    data = pd.read_csv(
        r"Cleaned_healthcare.csv"
    )
    return data


# --- Load Data ---
data = read_data()

# --- Persistent Filter Storage File ---
FILTER_FILE = "session_filters.json"


# --- Load Previously Saved Filters ---
def load_saved_filters():
    if os.path.exists(FILTER_FILE):
        try:
            with open(FILTER_FILE, "r") as f:
                saved = json.load(f)
            return saved
        except Exception:
            return {}
    return {}


# --- Save Current Filters ---
def save_current_filters():
    filter_keys = ["gender", "age", "year", "month", "insurance", "admission_type"]
    with open(FILTER_FILE, "w") as f:
        json.dump({k: st.session_state.get(k, []) for k in filter_keys}, f)


# --- Main Sidebar Function ---
def create_widgets():
    st.sidebar.header(':material/house: Patients Profile Analysis')

    # Initialize session state and load saved filters
    filter_keys = ["gender", "age", "year", "month", "insurance", "admission_type"]
    saved_filters = load_saved_filters()

    for key in filter_keys:
        if key not in st.session_state:
            # Use saved filters as initial values if available
            st.session_state[key] = saved_filters.get(key, [])

    # --- Sidebar Filters ---
    gender = st.sidebar.multiselect("**Choose Gender:**", data["Gender"].unique(), default=st.session_state.gender, key="gender", placeholder="Options...")
    df1 = data[data["Gender"].isin(gender)] if gender else data.copy()

    age = st.sidebar.multiselect("**Choose Age Group:**", df1["Age_groups"].unique(), default=st.session_state.age, key="age", placeholder="Options...")
    df2 = df1[df1["Age_groups"].isin(age)] if age else df1.copy()

    col1, col2 = st.sidebar.columns((0.45, 0.55))
    with col1:
        year = st.multiselect("**Pick Year**", df2["Year"].unique(), default=st.session_state.year, key="year", placeholder="Options...")
        df3 = df2[df2["Year"].isin(year)] if year else df2.copy()

    with col2:
        month = st.multiselect("**Pick Month**", df3["Month"].unique(), default=st.session_state.month, key="month", placeholder="Options...")
        df4 = df3[df3["Month"].isin(month)] if month else df3.copy()

    insurance = st.sidebar.multiselect("**Choose Insurance Provider:**", df4["Insurance Provider"].unique(), default=st.session_state.insurance, key="insurance", placeholder="Options...")
    df5 = df4[df4["Insurance Provider"].isin(insurance)] if insurance else df4.copy()

    admission_type = st.sidebar.multiselect("**Choose Admission Type:**", df5["Admission Type"].unique(), default=st.session_state.admission_type, key="admission_type", placeholder="Options...")
    df6 = df5[df5["Admission Type"].isin(admission_type)] if admission_type else df5.copy()

    # --- Buttons ---
    col1, col2 = st.sidebar.columns(2)
    with col1:
        if st.button("**Save Filters**"):
            save_current_filters()

    # with col2:
        # if st.button("**Reset Filters**"):
        #    for key in filter_keys:
        #        st.session_state[key] = []
        #    if os.path.exists(FILTER_FILE):
        #        os.remove(FILTER_FILE)
        #    st.rerun()

    # --- Final Filtered Data ---
    filtered_df = df6.copy()

    # --- Helper Functions ---
    def format_number(x):
        return f"{x:,}"

    def approx_val(x):
        if abs(x) >= 1_000_000_000:
            return f"${(x/1_000_000_000):.1f}B"
        elif abs(x) >= 1_000_000:
            return f"${(x/1_000_000):.1f}M"
        else:
            return f"${x:,.2f}"

    # --- KPI Metrics ---
    tot_patient = format_number(filtered_df.shape[0])
    tot_patient_rate = ((1 - (filtered_df.shape[0] / data.shape[0])) * 100)
    patient_rate = f"{-round(tot_patient_rate, 1)}%" if tot_patient_rate > 0 else "0"

    avg_los = f"{round(filtered_df['Admission_Duration'].mean(), 1)} days"
    avg_los_rate = ((1 - (filtered_df['Admission_Duration'].count() / data['Admission_Duration'].count())) * 100).round(1)
    los_rate = f"{-avg_los_rate}%" if avg_los_rate > 0 else "0"

    tot_bill = approx_val(filtered_df['Billing Amount'].sum())
    tot_bill_rate = ((1 - (filtered_df['Billing Amount'].sum() / data['Billing Amount'].sum())) * 100).round(1)
    rev_rate = f"{-tot_bill_rate}%" if tot_bill_rate > 0 else "0"

    avg_bill = approx_val(filtered_df['Billing Amount'].mean())
    avg_bill_rate = ((1 - (filtered_df['Billing Amount'].mean() / data['Billing Amount'].mean())) * 100).round(1)
    avg_rate = f"{-avg_bill_rate}%" if avg_bill_rate > 0 else "0"

    # --- Color Palettes ---
    colours = ["#053829", "#1a5d3a", "#4ebc7c", "#69d69d", "#8bf0bf", "#cfffe6", "#ffffff"]
    colours2 = ["#053829", "#69d69d"]

    return (
        data, df1, df2, df3, df4, df5, df6, filtered_df,
        colours, colours2, tot_bill, tot_patient, rev_rate, approx_val,
        tot_patient, patient_rate, avg_bill, avg_rate, avg_los, los_rate
    )



