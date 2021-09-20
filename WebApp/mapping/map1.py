import folium
map = folium.Map(location=[39.952489, -75.163519], zoom_start=6, tiles="Stamen Terrain")

fg = folium.FeatureGroup(name="My Map")
fg.add_child(folium.Marker(location=[39.80, -75.2], popup="Hi, I'm a marker!", icon=folium.Icon(color='green')))
map.add_child(fg)

map.save("Map1.html")