num_x = int(input())
num_y = int(input())

# Quadrant 1
if num_x > 0 and num_y > 0:
  print(1)

# Quadrant 2
elif num_x < 0 and num_y > 0:
  print(2)

# Quadrant 3
elif num_x < 0 and num_y <0:
  print(3)

# Quadrant 4
else:
  print(4)