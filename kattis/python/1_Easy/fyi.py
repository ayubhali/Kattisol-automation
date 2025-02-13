# Number 7 digits
# 555 number provide directory information


# Input Single line integer 
# rout to information operator or not 

# https://www.geeksforgeeks.org/python-convert-number-to-list-of-integers/

number = input()

caller = list(map(int, number)) 

# dealing with list -> [5, 5, 5]
# if the array has 5, 5, 5 at the beginning
# no need to iterate 

if caller[:3] == [5, 5, 5]:
    print(1)
else:
    print(0)