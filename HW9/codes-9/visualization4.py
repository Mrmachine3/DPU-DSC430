import folium


m = folium.Map(location=[45.5236, -122.6750])
m.save('index.html')



#The default tiles are set to OpenStreetMap, 
#but Stamen Terrain, Stamen Toner, Mapbox Bright, 
#and Mapbox Control Room, and many others tiles are built in.
m1 = folium.Map(
    location=[45.5236, -122.6750],
    tiles='Stamen Toner',
    zoom_start=13
)
m1.save('index1.html')
