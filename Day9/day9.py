from typing import List
from Instruction import Instruction

headCoord = [0, 0]
tailCoord = [0, 0]
tailCoordHistory = [(0, 0)]

with open('./Day9/input.txt') as file:
  for line in file:
    instruction = Instruction(line)

    for i in range(0, instruction.numberOfSteps):
      headCoord[instruction.coordinateIndex] += instruction.step
      xDiff = headCoord[0] - tailCoord[0]
      yDiff = headCoord[1] - tailCoord[1]

      if (instruction.coordinateIndex == 0 and abs(xDiff) > 1) or (instruction.coordinateIndex == 1 and abs(yDiff) > 1):
        if abs(xDiff) + abs(yDiff) > 2: # Diagonal
          tailCoord[0] += 1 if xDiff > 0 else -1
          tailCoord[1] += 1 if yDiff > 0 else -1
        else:
          tailCoord[instruction.coordinateIndex] += instruction.step
        tailCoordHistory.append(tuple(tailCoord))

print(f"Unique tail positions: {len(set(tailCoordHistory))}")
