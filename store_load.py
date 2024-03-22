from pathlib import Path
import json

path = Path("my_file.json")
cities = ['chennai', 'mumbai', 'pune', 'madurai', 'coimbatore']
# convert data to json format
json_content = json.dumps(cities)
print(json_content)

# writing content to json file
path.write_text(json_content)

# read content from json file
json_read_content = path.read_text()
print(json_read_content)

# convert json read content to data 
cities_read_list = json.loads(json_read_content)
print(cities_read_list)





