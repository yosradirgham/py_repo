import folium
import pandas

df = pandas.read_csv("./Volcanoes.txt")

def getCoordinates(df):
    coordinates=[]
    for i in range(df.shape[0]):
        coordinates.append([df.LAT[i], df.LON[i]])
    return coordinates

# Create a map object
map = folium.Map(location = [48.866667,2.333333], tiles = "MapBox bright")


# add markers to all the locations stored in our dataframe
fg = folium.FeatureGroup(name="My Map")

coordinates = getCoordinates(df)
for i in coordinates:
    marker = folium.Marker(location=i, popup="Hello World", icon=folium.Icon(color="pink"))
    fg.add_child(marker)

map.add_child(fg)

# Generate html page
map.save("index.html")
