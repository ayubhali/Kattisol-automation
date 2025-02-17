# input consists of two lines

# first line integer -> N total number of windows covered by curtains
# second line integer -> M total number of window curtains that have been drawn open

window_covered = int(input())
window_opened = int(input())

window_curtain = window_covered - window_opened

print(window_curtain)