# one line input of integer of wind speed in ieland

# input of number of roads 

# Net n lines will consist a string -> Road and integer maximum safe wind speed + k the maximum safe windspeed

# print n lines for each road where is safe to travel 

# Read the wind speed
wind_speed = int(input())

# Read the number of roads
number_roads = int(input())

# Loop through each road
for _ in range(number_roads):
    road_data = input().split()  # Read input and split into words
    max_speed = int(road_data[-1])    # Convert last word to integer (safe wind speed)
    road_name = " ".join(road_data[:-1])   # Join everything before last word as road name

    if wind_speed > max_speed:
        print(road_name, "lokud")  
    else:
        print(road_name, "opin")  
