temp_num = int(input())
temp_nums = list(map(int, input().split())) # -> Taking input multiple 

count = 0

for temps in temp_nums:
  if temps < 0:
    count += 1

print(count)

