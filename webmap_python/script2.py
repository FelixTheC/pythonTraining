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

map = folium.Map(location=[df['LAT'].mean(), df['LON'].mean()], zoom_start=4, tiles='Stamen Terrain')

for lat, lon, name, height in zip(df['LAT'], df['LON'], df['NAME'], df['ELEV']):
        folium.Marker([lat, lon], popup=name,
         icon=folium.Icon(color=color_by_elev(height))\
         ).add_to(map)

folium.Html.save(map, outfile='test2.html')
