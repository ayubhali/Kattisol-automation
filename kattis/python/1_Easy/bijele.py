pieceset = [1, 1, 2, 2, 2, 8]

input_pieces = list(map(int, input().split()))

needed = []

for i in range(6):
    needed.append(pieceset[i] - input_pieces[i])

for i in range(6):
    print(needed[i], end=" ")
