import streamlit as st
import pickle
import pandas as pd
import numpy as np

st.set_page_config(page_title = 'Apartments Recommender', 
                   layout = 'wide')

st.markdown("<h3 style='text-align: center;color: white; font-size: 48px; font-family: Modern Sans-Serif;'>Apartment Recommendation</h3>", unsafe_allow_html=True)

@st.cache_resource
def load_data():
    location_df = pickle.load(open('Datasets/location_distance.pkl','rb'))
    cosine_sim1 = pickle.load(open('Datasets/cosine_sim1.pkl','rb'))
    cosine_sim2 = pickle.load(open('Datasets/cosine_sim2.pkl','rb'))
    cosine_sim3 = pickle.load(open('Datasets/cosine_sim3.pkl','rb'))
    return location_df, cosine_sim1, cosine_sim2, cosine_sim3
location_df, cosine_sim1, cosine_sim2, cosine_sim3 = load_data()

def recommend_properties_with_scores(property_name, top_n = 5):

    cosine_sim_matrix = 0.5 * cosine_sim1 + 0.8 * cosine_sim2 + 1 * cosine_sim3

    try:
        sim_scores = list(enumerate(cosine_sim_matrix[location_df.index.get_loc(property_name)]))

        sorted_scores = sorted(sim_scores, key=lambda x: x[1], reverse = True)

        top_indices = [i[0] for i in sorted_scores[1:top_n + 1]]
        top_scores = [i[1] for i in sorted_scores[1:top_n + 1]]

        top_properties = location_df.index[top_indices].tolist()

        recommendations_df = pd.DataFrame({
            'PropertyName': top_properties,
            'SimilarityScore': [round(score, 4) for score in top_scores]
        })
        return recommendations_df

    except KeyError:
        st.error(f"Property '{property_name}' not found in the dataset.")
        return pd.DataFrame()

st.markdown("Use the tools below to find nearby properties or get personalized recommendations.")

st.markdown('---')

st.header('2. Get Personalized Apartment Recommendations')
st.markdown("Select a property you like to get recommendations for similar apartments based on features like amenities, size, and pricing.")

with st.form("recommendation_form"):
    appartment_names = sorted(location_df.index.to_list())
    
    selected_appartment = st.selectbox(
        'Select an apartment to base recommendations on',
        [''] + appartment_names, 
        index = 0,
        format_func = lambda x: x if x else 'Select an apartment...',
        key = 'appartment_select'
    )
    
    top_n_recommendations = st.slider(
        'Number of Recommendations',
        min_value = 3,
        max_value = 10,
        value = 5,
        step = 1,
        key = 'top_n_slider'
    )

    recommend_button = st.form_submit_button('Recommend Similar Apartments')

if recommend_button:
    if not selected_appartment:
        st.error("🛑 Please **select an apartment** to get recommendations.")
    else:
        st.subheader(f'Top {top_n_recommendations} Recommendations for **{selected_appartment}**')

        recommendation_df = recommend_properties_with_scores(selected_appartment, top_n = top_n_recommendations)

        if not recommendation_df.empty:
            recom_df = st.dataframe(
                recommendation_df.set_index(pd.Index(range(1, len(recommendation_df) + 1))).rename_axis('Rank'), 
                width = 'stretch'
            )
            
            st.info("Similarity Score reflects how similar the property is to your selection.")
