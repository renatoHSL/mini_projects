import requests
import csv
import streamlit as st

# URL do feed GeoJSON de terremotos da última semana
url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.geojson"

# Requisitar os dados do feed
response = requests.get(url)
data = response.json()

# Extrair os dados dos terremotos
earthquakes = data["features"]
earthquake_data = []

for earthquake in earthquakes:
    magnitude = earthquake["properties"]["mag"]
    location = earthquake["properties"]["place"]
    longitude, latitude, depth = earthquake["geometry"]["coordinates"]

    earthquake_data.append([magnitude, location, latitude, longitude])

# Escrever os dados no arquivo CSV
with open('earthquakes.csv', 'w', newline='', encoding='UTF-8') as csvfile:
    csvwriter = csv.writer(csvfile)

    # Escrever o cabeçalho
    csvwriter.writerow(["Magnitude", "Location", "Latitude", "Longitude"])

    # Escrever as linhas de dados
    csvwriter.writerows(earthquake_data)

st.write(f"Arquivo CSV criado em {'earthquakes.csv'}")

# Exibir os dados no Streamlit (opcional)
st.write("Dados de Terremotos:")
st.dataframe(earthquake_data)