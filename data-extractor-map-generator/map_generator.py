import folium
import streamlit as st
import pandas as pd

from streamlit_folium import st_folium

file_path = 'earthquakes.csv'

df = pd.read_csv(file_path)

average_latitude = df['Latitude'].mean()
average_longitude = df['Longitude'].mean()
m = folium.Map([average_latitude, average_longitude], zoom_start=12)


for _, row in df.iterrows():
    folium.Circle(
        location=[row['Latitude'], row['Longitude']],
        radius=row['Magnitude'] * 10000,
        color='red',
        fill=True,
        fill_color='red'
    ).add_child(folium.Popup(f"Loc: {row['Location']} \n Mag: {row['Magnitude']}")).add_to(m)

# call to render Folium map in Streamlit
st_data = st_folium(m, width=725)

# TODO rever mapa sendo recarregado o tempo todo
