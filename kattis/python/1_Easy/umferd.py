# Traffict is divided into lanes and each lane has m cells

# Each cell can contain 1 car but a cell can be empty

# length of m lanes 

# number of lanes n 

# description of each sell -> # with car ., no car 

# Calculate the number of empty cells as a number between 0 and 1 (inclusive)



# input 1 -> intger m -> number cells per lane
# input 2 -> integer n -> number of lanes
# m letters each . or #.

# Output proportion of empty cells as a value 0-1

m = int(input())

n = int(input())

net_cells = n * m

empty_count = 0 # initialize it to zero the counter

for _ in range(n): 
  road_data = input()
  empty_count += road_data.count('.') # its not being accumulated i was reassigning 

proportion = empty_count / net_cells

print(proportion)



# proportion of empty cells -> 
# proportion of meaning -> Part/whole \
# proportion form  -> a : b :: c : d a/b = c/d 

# each cell contain at most 1 car 

# 2 cells -> 
# 1 lane -> 
# 1 car and no car 
# porportion is 1/2  the 1 car over the amount of cells

# 4 cells -> 
# 2 lanes -> 
# 5 cars -> fills up 1 , 2, 3, 4 -> new lane with 1 car 
# portportion is  -> 3 empty cells taking the proportion of that / total amount of cells 
