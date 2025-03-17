n = int(input())

total_length = int(input())

for _ in range(n - 1):
    length = int(input())
    total_length += length - 1  # Fuse

print(total_length)
