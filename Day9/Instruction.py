directionToStepMap = {
  "U": 1,
  "D": -1,
  "R": 1,
  "L": -1
}
directionToCoordinateIndex = {
  "U": 1,
  "D": 1,
  "R": 0,
  "L": 0
}

class Instruction:
  def __init__(self, rawInstruction: str):
    instruction = rawInstruction.strip().split(" ")
    self.direction = instruction[0]
    self.numberOfSteps = int(instruction[1])
    self.step = directionToStepMap[self.direction]
    self.coordinateIndex = directionToCoordinateIndex[self.direction]