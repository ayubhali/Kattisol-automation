# Input is two lines ->
# single integer n -> number of slices
# single integer m -> number of people

slices = int(input())
people = int(input())

leftover = slices % people

print(leftover)