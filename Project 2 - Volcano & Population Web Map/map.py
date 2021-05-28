import folium
import pandas
map = folium.Map(location=[38.58,-99.09],zoom_start=6,titles = "Stamen Terrain")

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
long = list(data["LON"])
elev = list(data["ELEV"])

def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'
fgv = folium.FeatureGroup(name = "My Map")

for lt,ln,el in zip(lat,long,elev):
    fgv.add_child(folium.CircleMarker(location = [lt,ln],radius=6,fill_color = color_producer(el),color = 'grey',fill = True,fill_opacity = 0.7, popup=folium.Popup(str(el) + " m",parse_html=True)))

fgp = folium.FeatureGroup(name = "Population")
fgp.add_child(folium.GeoJson(data = (open('world.json','r',encoding='utf-8-sig').read()),
style_function=lambda x: {'fillColor': 'yellow' if x['properties']['POP2005'] < 10000000 else 'orange' if 10000000 <=x['properties']['POP2005'] < 20000000 else 'red'}))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())

map.save("MAP.html")


print(mydict) 