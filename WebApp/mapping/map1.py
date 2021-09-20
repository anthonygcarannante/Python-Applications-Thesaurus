import folium
import pandas as pd

# Load in volcano data via pd
data = pd.read_csv('Volcanoes.txt')

# Create separate lists for latitudes and longitudes
lats = list(data['LAT'])    
lons = list(data['LON'])
elev = list(data['ELEV'])

# Starting point for Map
map = folium.Map(location=[lats[0], lons[0]], zoom_start=6, tiles="Stamen Terrain")

# Create layer for all markers
fg = folium.FeatureGroup(name="My Map")

# for coordinate in range(0,len(data)):
#     fg.add_child(folium.Marker(location=[lats[coordinate],lons[coordinate]], popup="Hi, I'm a marker!", icon=folium.Icon(color='green')))
#     map.add_child(fg)

for lt, ln, el in zip(lats, lons, elev):
    fg.add_child(folium.Marker(location=[lt,ln], popup=f"Elevation: {el}", icon=folium.Icon(color='green')))
    map.add_child(fg)

map.save("Map1.html")
