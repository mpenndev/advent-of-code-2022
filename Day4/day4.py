def isFullyContainingPair(ranges):
  ranges.sort(key=lambda r: r[0] - r[1])
  return ranges[0][0] <= ranges[1][0] and ranges[0][1] >= ranges[1][1]

containingPairs = 0
with open('./Day4/input.txt') as file:
  for line in file:
    assignments = line.strip().split(",")

    ranges = [[int(r) for r in a.split("-")] for a in assignments]
    isContainingPair = isFullyContainingPair(ranges)
    containingPairs = containingPairs + 1 if isContainingPair else containingPairs
    
print(f"There are {containingPairs} pairs that are fully containing")

# Part 2

def hasOverlap(ranges):
  ranges.sort(key=lambda r: r[0])
  return ranges[0][1] >= ranges[1][0] or ranges[1][1] <= ranges[0][0]

overlappingPairs = 0
with open('./Day4/input.txt') as file:
  for line in file:
    assignments = line.strip().split(",")

    ranges = [[int(r) for r in a.split("-")] for a in assignments]
    isOverlappingPair = hasOverlap(ranges)
    overlappingPairs = overlappingPairs + 1 if isOverlappingPair else overlappingPairs
    print(f"{ranges}: {isOverlappingPair}")
    
print(f"There are {overlappingPairs} overlapping pairs")