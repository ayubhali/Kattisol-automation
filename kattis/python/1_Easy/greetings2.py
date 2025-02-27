# later -> Alligator 

# input consists 1 line of strings of  length of 3 

message = input()

count = message.count('e') # count the occurences of e 

e_char = 'e' * (count * 2) # repeat e , e times 

# first letter + elongated 2nd + last letter
new_message = message[0] + e_char + message[-1]

print(new_message)

