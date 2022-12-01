elfSums = []
currentElfCalories = 0

with open('./Day1/input.txt') as file:
  input = file.readlines()
  
  for line in input:
    if line == "\n":
      elfSums.append(currentElfCalories)
      currentElfCalories = 0
    else:
      currentElfCalories += int(line)

highestCalories = max(elfSums)
index = elfSums.index(highestCalories)
print(f"Elf #{index + 1} (index {index}) is carrying the most calories @ {highestCalories}")