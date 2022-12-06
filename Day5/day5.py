from typing import List

def parseStartingPosition(positionInput: List[str]) -> List[List[str]]:
  parsedPosition = []
  finalIndex = 4 * int(positionInput[-1].strip()[-1]) - 3 + 4
  for i in range(1, finalIndex, 4):
    parsedPosition.append([c[i] for c in positionInput[:-1] if c[i] != " "])
  return parsedPosition

def parseInstructions(instructionsInput: List[str]) -> List[List[int]]:
  parsedInstructions = []
  for instruction in instructionsInput:
    parsedInstructions.append([int(c) for c in instruction.split() if c.isdigit()])
  return parsedInstructions

def runInstructions(startingPosition: List[List[str]], instructions: List[List[int]]):
  position = startingPosition
  for instruction in instructions:
    stackToMoveFrom = startingPosition[instruction[1] - 1]
    stackToMoveTo = startingPosition[instruction[2] - 1]

    for _ in range(instruction[0]):
      crate = stackToMoveFrom.pop(0)
      stackToMoveTo.insert(0, crate)
  return position

with open("./Day5/input.txt") as file:
  input = file.readlines()

splitIndex = input.index("""\n""")
positionInput = input[:splitIndex]
instructionsInput = input[splitIndex + 1:]

startingPosition = parseStartingPosition(positionInput)
instructions = parseInstructions(instructionsInput)

outcome = runInstructions(startingPosition, instructions)
print(''.join([stack[0] for stack in outcome]))