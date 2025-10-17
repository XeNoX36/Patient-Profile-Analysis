import streamlit as st

with open(r"Streamlit\healthcare_app\healthcare_Style.css", "r") as f:
    st.markdown(f"""<style>{f.read()}</style>""", unsafe_allow_html=True)

st.set_page_config(page_title="Healthcare Analysis",
                   initial_sidebar_state="expanded",
                   page_icon=":hospital:",
                   layout="wide")
st.markdown('<style>div.block-container{padding:1.8rem;}</style>', unsafe_allow_html=True)

# Nav bars
home_page = st.Page("pages/Home.py", title="Patient Demography")
about_page = st.Page("pages/About.py", title="Medicals")
contact_page = st.Page("pages/Contact.py", title="Finance and Insurance")
dataset_page = st.Page("pages/Dataset.py", title="Data")
pg = st.navigation([home_page, about_page, contact_page, dataset_page], position="top")
pg.run()
