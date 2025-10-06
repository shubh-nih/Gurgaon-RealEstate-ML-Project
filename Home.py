import streamlit as st
st.set_page_config(page_title = 'Gurgaon Estate Project', 
                   layout = 'wide')

st.markdown("""
    <style>
    .sub-header {
        font-size: 1.2rem;
        color: #6b7280;
        text-align: center;
        margin-bottom: 2rem;
    }
    .module-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1.5rem;
        border-radius: 10px;
        color: white;
        margin: 1rem 0;
    }
    .feature-box {
        background-color: #f3f4f6;
        padding: 1.5rem;
        border-radius: 8px;
        border-left: 4px solid #3b82f6;
        margin: 0.5rem 0;
    }
    .stat-box {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 10px;
        text-align: center;
        color: white;
    }
    .pipeline-step {
        background-color: #eff6ff;
        padding: 1rem;
        border-radius: 8px;
        margin: 0.5rem 0;
        border-left: 4px solid #3b82f6;
    }
    </style>
""", unsafe_allow_html = True)


st.markdown("<h3 style='text-align: center;color: white; font-size: 48px; font-family: Modern Sans-Serif;'>Gurgaon Real Estate Project</h3>", unsafe_allow_html=True)

st.markdown('<p class="sub-header">Predictive Module | Analysis Module | Recommendation Module</p>', unsafe_allow_html = True)

st.markdown("""

    This is an end-to-end Data Science Capstone Project focused on the Gurgaon real estate market.
    The goal is to analyze, visualize, and predict property prices using advanced analytics and machine learning.

        🧹Data Cleaning & Preprocessing — handled missing values, removed duplicates.
        📊EDA — visualized price trends and sector-level property insights.
        ⚙️Feature Engineering — enhanced data quality and predictive power.
        🚫Outlier Detection — treated extreme values for model accuracy.
        🌲Model Creation (Random Forest) — built and tuned for high accuracy.

""")

