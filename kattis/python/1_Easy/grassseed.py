cost = float(input())

lawns = int(input())

total = 0

for i in range(lawns):
    width, length = map(float, input().split())
    total += width * length

print(total * cost)
