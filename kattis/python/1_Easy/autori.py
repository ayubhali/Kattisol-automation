message = input()
new_message = message.split("-")

result = ""

for word in new_message:
  result += word[0]

print(result)
