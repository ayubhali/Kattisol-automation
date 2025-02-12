# Input consists of one integer a -> percentage of switch points bet one options

# for each option display 

bet = float(input())

payoutone = 100 / bet # -> 100% of the bet 
payoutwo = 100 / (100 - bet) # -> Remaining Portion of the bet

print(f"{payoutone:.10f}")
print(f"{payoutwo:.10f}")
