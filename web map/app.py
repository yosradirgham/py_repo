import folium
import pandas

df = pandas.read_csv("./Volcanoes.txt")

def getCoordinates(df):
    coordinates=[]
    for i in range(df.shape[0]):
        coordinates.append([df.LAT[i], df.LON[i]])
    return coordinates

def getColor(el):
    if el < 2000:
        return "green"
    elif el >= 2000 and el < 3000:
        return "orange"
    else:
        return "red"

# Create a map object
map = folium.Map(location = [48.866667,2.333333], zoom_start=6, tiles='CartoDB dark_matter')
# tiles = "MapBox bright")


# add markers to all the locations stored in our dataframe
fg = folium.FeatureGroup(name="My Map")

coordinates = getCoordinates(df)
elev = df["ELEV"]

# Color changes depending on the elevation: red(>3000m), orange(2000-3000), green(<2000)
for i,j in zip(coordinates, elev):
    marker = folium.Circle(location=i, radius =16, popup=str(j), color=getColor(j))
    fg.add_child(marker)

map.add_child(fg)

# Generate html page
map.save("index.html")
