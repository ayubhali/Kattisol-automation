# read integers and print them reverse order

# first line # of integers
# list of n integers

n = int(input())

new_list = []

# read in n integers and store in a list
for _ in range(n):
  new_list.append(int(input()))

# print the list in reversed order
for num in reversed(new_list):
  print(num)
