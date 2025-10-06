import streamlit as st
import pickle
import pandas as pd
import numpy as np
import os
import requests

MODEL_URL = "https://drive.google.com/uc?id=1abcXYZ12345"
MODEL_PATH = "pipeline.pkl"
        
@st.cache_resource
def load_model():
    if not os.path.exists(MODEL_PATH):
            r = requests.get(MODEL_URL)
            open(MODEL_PATH, 'wb').write(r.content)
    with open(MODEL_PATH, 'rb') as f:
        pipeline = pickle.load(f)
    return pipeline

pipeline = load_model()

st.set_page_config(page_title = 'Price Predictor', 
                   layout = 'wide')

with open('df.pkl', 'rb') as file:
    df = pickle.load(file)

@st.dialog("⚠️ Missing Input")
def show_warning():
    st.write("Please fill in all the required fields before predicting the price.")
    if st.button('OK'):
        st.rerun()

st.markdown("<h3 style='text-align: center;color: white; font-size: 48px; font-family: Modern Sans-Serif;'>Gurgaon Real Estate Price Predictor</h3>", unsafe_allow_html=True)

st.markdown('Enter the details of the property')

with st.form('prediction_form'):
    st.header('Property Features')
    
    col1, col2 = st.columns(2)
    
    with col1:
        property_type = st.selectbox('Property Type', ['Flat', 'House'], index = None, placeholder = 'Select property type')
        
        sector = st.selectbox('Sector', sorted(df['sector'].unique().tolist()), index = None, placeholder = "Select sector")
        
        bedroom = st.selectbox('Number of Bedrooms', sorted(df['bedRoom'].unique().tolist()), index = None, placeholder = "Select bedrooms")
        
        bathroom = st.selectbox('Number of Bathrooms', sorted(df['bathroom'].unique().tolist()), index = None, placeholder = "Select bathrooms")
        
        balcony = st.selectbox('Number of Balconies', sorted(df['balcony'].unique().tolist()), index = None, placeholder = "Select balconies")
        
        agePossession = st.selectbox('Property Age', sorted(df['agePossession'].unique().tolist()), index = None, placeholder = "Select property age")

    with col2:
        servant_room = st.selectbox('Servant Room', [0.0, 1.0], format_func = lambda x: "Yes" if x == 1.0 else "No", index = None, placeholder = "Has servant room?")
        
        study_room = st.selectbox('Study Room', [0.0, 1.0], format_func = lambda x: "Yes" if x == 1.0 else "No", index = None, placeholder = "Has study room?")
        
        store_room = st.selectbox('Store Room', [0.0, 1.0], format_func = lambda x: "Yes" if x == 1.0 else "No", index = None, placeholder = "Has store room?")
        
        furnished_type = st.selectbox('Furnishing Type', sorted(df['furnished_type'].unique().tolist()), index = None, placeholder = "Select furnishing type")
        
        luxury_category = st.selectbox('Luxury Category', sorted(df['luxury_category'].unique().tolist()), index = None, placeholder = "Select luxury category")
        
        floor_category = st.selectbox('Floor Category', sorted(df['floor_category'].unique().tolist()), index = None, placeholder = "Select floor category")

    built_up_area = st.number_input('Built-Up Area (in Sq. Ft.)', min_value = 0.0, step = 50.0, placeholder = "Enter area in sq. ft.")
    
    st.markdown("---")
    
    submitted = st.form_submit_button('Predict Price')

if submitted:
    inputs = [
        property_type, sector, bedroom, bathroom, balcony, agePossession,
        built_up_area, servant_room, study_room, store_room, furnished_type,
        luxury_category, floor_category
    ]

    if any(val is None for val in inputs) or built_up_area == 0.0:
        show_warning()
    else:
        data = [[
            property_type, sector, int(bedroom), int(bathroom), balcony, agePossession,
            built_up_area, int(servant_room), int(study_room), int(store_room), furnished_type,
            luxury_category, floor_category
        ]]
        
        columns = [
            'property_type', 'sector', 'bedRoom', 'bathroom', 'balcony',
            'agePossession', 'built_up_area', 'servant room', 'study room', 'store room',
            'furnished_type', 'luxury_category', 'floor_category'
        ]

        one_df = pd.DataFrame(data, columns = columns)
            
        prediction = np.expm1(pipeline.predict(one_df))[0]
        
        low_prediction = prediction - 0.255
        high_prediction = prediction + 0.255
         
        st.subheader(f"Predicted Price Between: ₹ {np.round(low_prediction, 2)} And {np.round(high_prediction, 2)} Crores")
        

