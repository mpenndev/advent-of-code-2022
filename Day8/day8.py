from typing import List

def getEdgeCount(map: List[List[int]]):
  return len(map) * 2 + len(map[0]) * 2 - 4

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

map = []
with open('./Day8/input.txt') as file:
  for line in file:
    map.append(list(line.strip()))

innerCount = 0
for y in range(1, len(map) - 1):
  for x in range(1, len(map[0]) - 1):
    if isVisibleInPlane(map[y], x) or isVisibleInPlane([map[i][x] for i in range(0, len(map))], y):
      innerCount += 1

print(f"Visible trees: {getEdgeCount(map) + innerCount}")