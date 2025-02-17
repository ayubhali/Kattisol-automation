# given an input string s garunteed letter a 

# output the remaining starting from a 

# banana  -> anana

# find the position of the string -> slicing to get the suffix and print result 


input_string = input()

index_of_a = input_string.find('a')

print(input_string[index_of_a:])


