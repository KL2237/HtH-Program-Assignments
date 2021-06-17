# STEP 2
city_names = ["Oakland", 
              "Atlanta", 
              "New York City", 
              "Seattle", 
              "Memphis", 
              "Miami", 
              "Boston", 
              "Los Angeles", 
              "Denver", 
              "New Orleans"]
print(city_names[0])
print(city_names[2])
print(city_names[5])

# STEP 3
song_genres = ["Reggaeton", 
               "Rock", 
               "RnB", 
               "Soul", 
               "Hip Hip/Rap", 
               "Indie", 
               "Pop", 
               "Drill", 
               "EDM", 
               "Funk"]
print(song_genres[2])

# STEP 4
two_cities = city_names[0:2]
print(two_cities)

two_genres = song_genres[1:4]
print(two_genres)

# STEP 5
city_names[0] = "San Francisco"
city_names[2] = "Brooklyn"
city_names[7] = "Hollywood"
city_names[5] = "Tampa"
print(city_names)

city_names.append("New Jersey")
city_names.extend(["Santa Cruz", "Selma", "Chicago"])
city_names.insert(7, "Washington, D.C.")
print(city_names)

# STEP 6
city_names.append("Oakland")
city_names.extend(["Miami", "Los Angeles"])
city_names.insert(0, "Miami")

del city_names[3]
city_names.pop[6]
city_names.remove("New York City")