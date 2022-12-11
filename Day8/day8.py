from typing import List

def getVerticalPlane(map: List[List[int]], x: int):
  return [map[i][x] for i in range(0, len(map))]

def isVisibleInPlane(planeSection: List[int], currentPos: int):
  height = planeSection[currentPos]

  visibleBefore = True
  for i in range(0, len(planeSection)):
    if i == currentPos and visibleBefore:
      return True
    elif planeSection[i] >= height:
      if i < currentPos:
        visibleBefore = False
      elif i > currentPos:
        return False

  return True

def getEdgeCount(map: List[List[int]]):
  return len(map) * 2 + len(map[0]) * 2 - 4

map = []
with open('./Day8/input.txt') as file:
  for line in file:
    map.append(list(line.strip()))

innerCount = 0
for y in range(1, len(map) - 1):
  for x in range(1, len(map[0]) - 1):
    if isVisibleInPlane(map[y], x) or isVisibleInPlane(getVerticalPlane(map, x), y):
      innerCount += 1

print(f"Visible trees: {getEdgeCount(map) + innerCount}")

# Part 2

def getDirectionScenicScore(planeSection: List[int], currentPos: int, step: int, condition):
  height = planeSection[currentPos]
  count = 0
  i = currentPos + step
  blocked = False
  
  while not blocked and condition(i):
    count += 1
    if (planeSection[i] >= height):
      blocked = True
    i += step

  return count

def calculateScenicScore(map: List[List[int]], x: int, y: int):
  horizontalPlane = map[y]
  verticalPlane = getVerticalPlane(map, x)
  negativeCondition = lambda i: i >= 0

  xMinusScore = getDirectionScenicScore(horizontalPlane, x, -1, negativeCondition)
  xPlusScore = getDirectionScenicScore(horizontalPlane, x, 1, lambda i: i < len(horizontalPlane))
  yMinusScore = getDirectionScenicScore(verticalPlane, y, -1, negativeCondition)
  yPlusScore = getDirectionScenicScore(verticalPlane, y, 1, lambda i: i < len(verticalPlane))
  
  return xMinusScore * xPlusScore * yMinusScore * yPlusScore

highestScore = 0
for y in range(1, len(map) - 1):
  for x in range(1, len(map[0]) - 1):
    score = calculateScenicScore(map, x, y)
    if score > highestScore:
      highestScore = score
  
print(f"Highest scenic score: {highestScore}")