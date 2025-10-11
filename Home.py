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
    </style>
""", unsafe_allow_html = True)

st.markdown("<h3 style='text-align: center;color: white; font-size: 60px; font-family: Modern Sans-Serif;'>Gurgaon Real Estate Project</h3>", unsafe_allow_html=True)

st.markdown('<p class="sub-header">Prediction | Analysis | Recommendation</p>', unsafe_allow_html = True)

st.write("### Empowering Real Estate Insights through Machine Learning and Data Analytics")

st.markdown("""
Welcome to the **Gurgaon Real Estate Capstone Project**, a comprehensive data driven solution
designed to help users understand, analyze, and make informed property decisions in the Gurgaon housing market.

This project integrates **Machine Learning**, **Data Analysis**, and **Recommendation Algorithms**
to deliver actionable insights and predictions.
""")

st.markdown('---')

st.header("🚀 Overview")
st.markdown("""
This project is divided into three key modules:

1. **🏷️ Price Predictor**  
   - Predicts flat or house prices in Gurgaon based on features like location, area, furnishing, and more.  
   - Uses ML algorithm **Random Forest Regressor**.  

2. **📈 Data Analysis**  
   - Explores property trends, price distributions, and correlations using **Seaborn**, **Matplotlib**, and **Plotly**.  
   - Helps visualize key market insights such as area wise pricing, furnishing impact, and more.  

3. **🏘️ Recommender System**  
   - Suggests similar properties based on features, price range, and locality.  
   - Uses **cosine similarity** and **feature engineering** to find the best matches.
""")

st.markdown('---')

st.header("🧩 Project Workflow")
st.markdown("""
1. **Data Collection & Cleaning** – Handling missing values, and outlier detection.  
2. **Feature Engineering** – Creating new meaningful variables like price per sq.ft, area bins, etc.  
3. **Exploratory Data Analysis (EDA)** – Understanding the market dynamics visually.  
4. **Model Training & Evaluation** – Building and fine tuning ML models for prediction.  
5. **Deployment** – Interactive **Streamlit Web App** with Prediction, Analysis, and Recommendation modules.
""")

st.markdown('---')

st.header("🛠️ Tech Stack")
st.markdown("""
**Languages & Tools:**  
Python, Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn, Streamlit, Plotly

**ML Models Used:**  
Random Forest and Cosine Similarity for Recommendations
""")

st.markdown('---')

st.write("""
## 👨‍💻 Developer
**Shubham Bisht** 
""")
st.markdown("📧 [Mail](mailto:shubhambisht149@gmail.com)")
st.markdown("🪪 [LinkedIn](https://www.linkedin.com/in/shubhambisht7/)")
st.caption("© 2025 Gurgaon Real Estate Project | Built using Streamlit")


