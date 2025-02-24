# one line input of integer of wind speed in ieland

# input of number of roads 

# Net n lines will consist a string -> Road and integer maximum safe wind speed + k the maximum safe windspeed

# print n lines for each road where is safe to travel 

wind_speed = int(input())

number_roads = int(input())

for _ in range(number_roads):
  road_data = input().split()
  road_name = road_data[0]
  max_speed = road_data[1]


  if wind_speed > max_speed:
    print(road_name, "lokud")
  else:
    print(road_name, "opin")