def getUniqueCharactersIndex(input: str, requiredUniqueCharacters: int):
  for i in range(requiredUniqueCharacters, len(input)):
    if len(set(input[i-requiredUniqueCharacters:i])) == requiredUniqueCharacters:
      return i

with open("./Day6/input.txt") as file:
  input = file.read()

startOfPacketIndex = getUniqueCharactersIndex(input, 4)
print(f"Start of packet: {startOfPacketIndex}")

# Part 2

startOfMessageIndex = getUniqueCharactersIndex(input, 14)
print(f"Start of message: {startOfMessageIndex}")