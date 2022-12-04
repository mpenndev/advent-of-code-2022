def getCommonCharacter(a, b):
  commonCharacters = set(a).intersection(set(b))
  return next(iter(commonCharacters))

def getPriorityValue(character):
  offset = 96 if character.islower() else 38
  return ord(character) - offset

with open('./Day3/input.txt') as file:
  sum = 0
  for line in file:
    firstCompartment = line[:len(line)//2]
    secondCompartment = line[len(line)//2:]

    commonCharacter = getCommonCharacter(firstCompartment, secondCompartment)
    value = getPriorityValue(commonCharacter)
    sum += value
  
  print(f"Total priority value: {sum}")

print("Part 2")

def getCommonCharacter(*args):
  commonCharacters = set(args[0])
  for text in args[1:]:
    commonCharacters = commonCharacters.intersection(set(text))

  return next(iter(commonCharacters))

with open('./Day3/input.txt') as file:
  input = file.readlines()

  sum = 0
  for i in range(0, len(input), 3):
    commonCharacter = getCommonCharacter(input[i].strip(), input[i + 1].strip(), input[i + 2].strip())
    value = getPriorityValue(commonCharacter)
    sum += value

print(f"Total priority in group: {sum}")