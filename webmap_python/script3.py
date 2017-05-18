#! /usr/env/python3

import folium
import pandas


def color_by_elev(elev):
    color = 'green'
    if int(elev) < 1000:
        color = 'green'
    elif 1001 < int(elev) > 1500:
        color = 'orange'
    elif int(elev) > 1501:
        color = 'red'
    return color


df = pandas.read_csv('Volcanoes-USA.txt')

map = folium.Map(location=[df['LAT'].mean(), df['LON'].mean()], zoom_start=4)

for lat, lon, name, height in zip(df['LAT'], df['LON'], df['NAME'], df['ELEV']):
        folium.Marker([lat, lon], popup=name,
         icon=folium.Icon(color=color_by_elev(height))\
         ).add_to(map)

folium.GeoJson(data='world-geojson-from-ogr.json',
             name='Population 2005',
             style_function = lambda x: {'fillColor': 'green' if x['properties']['POP2005']<=100000 else 'orange'\
              if 100000 <=['properties']['POP2005']< 200000 else 'red'}).add_to(map)

folium.LayerControl().add_to(map)

folium.Html.save(map, outfile='test3.html')
