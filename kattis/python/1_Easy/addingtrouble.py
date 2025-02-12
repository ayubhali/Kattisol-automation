# Really bad adding numbers

# Given 3 integers A, B, C -> Make sure A + B = C

# Input line of 3 integers A B C 

# A + B = C  or A + B =! C

nums = list(map(int, input().split()))

if nums[0] + nums[1] == nums[2]:
  print("correct!")
else:
  print("wrong!")