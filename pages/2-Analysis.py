import streamlit as st
import matplotlib.pyplot as plt
import plotly.express as px
import pandas as pd
from wordcloud import WordCloud
import pickle
import seaborn as sns
st.set_page_config(page_title = 'Analysis Module', 
                   layout = 'wide')

df = pd.read_csv(r'Datasets\gurgaon-data-viz.csv')
text = pickle.load(open(r'Datasets\feature_text.pkl', 'rb'))

st.markdown("<h3 style='text-align: center;color: white; font-size: 48px; font-family: Modern Sans-Serif;'>Gurgaon Real Estate Analysis</h3>", unsafe_allow_html=True)

grouped_df = df.groupby('sector')[['price', 'price_per_sqft', 'built_up_area', 'longitude', 'latitude']].mean()

st.markdown('---')

st.header('Sector Price per Sqft Geomap')
fig = px.scatter_map(grouped_df, lat = "latitude", lon = "longitude",
                     color = "price_per_sqft", 
                     size = "built_up_area", 
                     color_continuous_scale = px.colors.cyclical.IceFire, 
                     size_max = 15, zoom = 10, width = 1200, height = 700, hover_name = grouped_df.index)
st.plotly_chart(fig, use_container_width = True)

st.markdown('---')

st.header('Features Wordcloud')
wordcloud = WordCloud(
    width = 800, 
    height = 800, 
    background_color = 'black', 
    stopwords = set(['s']), 
    min_font_size = 10
).generate(text)

fig2, ax = plt.subplots(figsize=(8, 8), facecolor = 'black')
ax.imshow(wordcloud, interpolation = 'bilinear')
ax.axis("off")
plt.tight_layout(pad = 0)
st.pyplot(fig2)

st.markdown('---')

st.header('Area Vs Price')
property_type = st.selectbox('Select Property Type', ['Flat', 'House'], index = None, placeholder = 'Select an Option')

if property_type == 'House':
    fig3 = px.scatter(df[df['property_type'] == 'house'], x = 'built_up_area', y = 'price', color = 'bedRoom')
    st.plotly_chart(fig3, use_container_width = True)
elif property_type == 'Flat':
    fig4 = px.scatter(df[df['property_type'] == 'flat'], x = 'built_up_area', y = 'price', color = 'bedRoom')
    st.plotly_chart(fig4, use_container_width = True)
else:
    fig5 = px.scatter(df, x = 'built_up_area', y = 'price', color = 'bedRoom')
    st.plotly_chart(fig5, use_container_width = True)
    
st.markdown('---')

st.header('BHK Pie Chart')
option = sorted(df['sector'].unique().tolist())
selected_sector = st.selectbox('Select Sector', option, index = None, placeholder = 'Select an Option')

if selected_sector:
    fig6 = px.pie(df[df['sector'] == selected_sector], names = 'bedRoom')
    st.plotly_chart(fig6, use_container_width = True)
else:
    fig7 = px.pie(df, names = 'bedRoom')
    st.plotly_chart(fig7, use_container_width = True)
    
st.markdown('---')

st.header('Side by Side BHK price comparison')

fig8 = px.box(df[df['bedRoom'] <= 4], x = 'bedRoom', y = 'price', title = 'BHK Price Range')
st.plotly_chart(fig8, use_container_width = True)

st.markdown('---')

st.header('Side by Side Distplot for property type')

fig9 = plt.figure(figsize=(10, 4))
sns.histplot(df[df['property_type'] == 'house']['price'], label='House', kde=True, color='blue')
sns.histplot(df[df['property_type'] == 'flat']['price'], label='Flat', kde=True, color='orange')
plt.legend()
st.pyplot(fig9)
