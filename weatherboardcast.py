import json

# Load the JSON data from the file
with open('weather.json', 'r') as file:
    data = json.load(file)

# Extract temperature data
temperature_data = data['temperature']['data']

# Print the temperature for each area
for entry in temperature_data:
    place = entry['place']
    temperature = entry['value']
    unit = entry['unit']
    print(f"Temperature in {place}: {temperature} {unit}")