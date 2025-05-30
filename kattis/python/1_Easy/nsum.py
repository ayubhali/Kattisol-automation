n = int(input())

nums = input().split()

total = 0

for i in range(n):
  total = total + int(nums[i])

print(total)