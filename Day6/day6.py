with open("./Day6/input.txt") as file:
  input = file.read()

for i in range(4, len(input)):
  if len(set(input[i-4:i])) == 4:
    break

print(i)