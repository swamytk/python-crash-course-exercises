from pathlib import Path
import json
import plotly.express as px

path = Path('eq_data_1_day_m1.geojson')
contents = path.read_text()

# convert to json dictionary format
json_data = json.loads(contents)
all_eq_dicts = json_data['features']
#print(all_eq_dicts[:4])
#print(len(all_eq_dicts)) # No. of records

# parsing the data
mags, lons, lats, eq_titles = [], [], [], []
for eq_dict in all_eq_dicts:
    mags.append(eq_dict['properties']['mag'])
    lons.append(eq_dict['geometry']['coordinates'][0])
    lats.append(eq_dict['geometry']['coordinates'][1])
    eq_titles.append(eq_dict['properties']['title'])

# Build world map chart
title = "Global Earthquakes"
fig = px.scatter_geo(
    lat = lats, lon=lons, size=mags, title=title,
    color=mags,
    color_continuous_scale='Viridis',
    labels={'color':'Magnitude'},
    projection='natural earth',
    hover_name=eq_titles)

# Save the Plot as image file
fig.write_html('earthquate_30days.html')

fig.show()



