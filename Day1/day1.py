elfCalorieTotals = []
currentElfCalories = 0

with open('./Day1/input.txt') as file:
  for line in file:
    if line == "\n":
      elfCalorieTotals.append(currentElfCalories)
      currentElfCalories = 0
    else:
      currentElfCalories += int(line)

highestCalories = max(elfCalorieTotals)
index = elfCalorieTotals.index(highestCalories)
print(f"Elf #{index + 1} (index {index}) is carrying the most calories @ {highestCalories}")

# Part 2

sortedCalorieTotals = elfCalorieTotals
sortedCalorieTotals.sort(reverse=True)

top3Sum = sum(sortedCalorieTotals[:3])
print(f"The top 3 elves are carrying {top3Sum} calories in total")