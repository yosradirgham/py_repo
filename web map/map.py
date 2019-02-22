import folium
import pandas


df = pandas.read_csv("./Volcanoes.txt")

def getLatitudeList():
    return df["LAT"]

def getLongitudeList():
    return df["LON"]

def getElevationValues():
    return df["ELEV"]

def color_producer(elev):
    if elev < 1000:
        return "green"
    elif elev >= 1000 and elev <3000:
        return "orange"
    else:
        return "red"

map = folium.Map(location=[80,-100],zoom_start=6,tiles="Mapbox Bright",min_zoom=2)

fgv = folium.FeatureGroup(name="Volcanoes")
for lat,long,elev in zip(getLatitudeList(),getLongitudeList(),getElevationValues()):
    fgv.add_child(folium.Marker(location=[lat,long],popup=str(elev)+" m", icon=folium.Icon(color="red",icon_color="white")))

fgp = folium.FeatureGroup(name="Population")
fgp.add_child(folium.GeoJson(data = open('world.json', 'r',encoding='utf-8-sig').read(),
style_function = lambda x: {'fillColor' : 'green' if x['properties']['POP2005'] < 10000000
else 'orange' if 10000000<= x['properties']['POP2005']<20000000 else 'red'}))#Ps: we can add conditions inside of this dictionaries, for adding multiple colors for example...


map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())

map.save("index.html")
