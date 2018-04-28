animals = ["cat", "dog", "rabbit", "horse", "giant_horrible_monster"]

cat_found = "cat" in animals
space_monster_found = "space_monster" in animals

new_weather = ['Sunny',
 'Sunny',
 'Sunny',
 'Sunny',
 'Sunny',
 'Sunny',
 'Sunny',
 'Sunny',
 'Fog',
 'Fog',
 'Fog',
 'Sunny',
 'Sunny',
 'Sunny',
 'Sunny',
 'Sunny',
 'Fog',
 'Fog',
 'Fog',
 'Sunny',
 'Sunny',
 'Sunny',
 'Sunny',
 'Fog',
 'Fog',
 'Sunny',
 'Fog',
 'Sunny',
 'Sunny',
 'Sunny',
 'Sunny',
 'Fog',
 'Rain',
 'Sunny',
 'Sunny',
 'Fog',
 'Fog',
 'Fog']

weather_types = ["Rain", "Sunny", "Fog", "Fog-Rain", "Thunderstorm", "Type of Weather"]
weather_type_found = []

for types in weather_types:
	weather_type_found.append(types in new_weather)

print(weather_type_found)