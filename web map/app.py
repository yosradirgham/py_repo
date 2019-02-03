import folium

map = folium.Map(location = [48.866667,2.333333], tiles = "MapBox bright")

fg = folium.FeatureGroup(name="My Map")

coordinates = [[48.866667,2.333333],[40.866667,2.333333]]
for i in coordinates:
    marker = folium.Marker(location=i, popup="Hello World", icon=folium.Icon(color="pink"))
    fg.add_child(marker)

map.add_child(fg)

map.save("index.html")
