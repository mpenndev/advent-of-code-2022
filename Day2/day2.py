shapeScore = {
  "R": 1,
  "P": 2,
  "S": 3
}

encryptionKey = {
  "A": "R",
  "B": "P",
  "C": "S",
  "X": "R",
  "Y": "P",
  "Z": "S"
}

def decode(encodedShape):
  return encryptionKey[encodedShape]

def getShapeValue(shape):
  return shapeScore[shape]

def decodeToValue(encodedShape):
  return getShapeValue(decode(encodedShape))

def determineOutcomeScore(opponentValue, strategyValue):
  absoluteDiff = abs(opponentValue - strategyValue)
  if (opponentValue == strategyValue):
    return 3
  elif (opponentValue > strategyValue and absoluteDiff == 1 or opponentValue < strategyValue and absoluteDiff > 1):
    return 0
  else:
    return 6

with open("./Day2/input.txt") as file:
  totalScore = 0
  for line in file:
    characters = line.split(" ")
    opponentEncoded = characters[0]
    strategyEncoded = characters[1].strip()

    opponentValue = decodeToValue(opponentEncoded)
    strategyValue = decodeToValue(strategyEncoded)
    
    outcomeScore = determineOutcomeScore(opponentValue, strategyValue)

    roundScore = strategyValue + outcomeScore
    totalScore += roundScore
    print(f"Round score: {roundScore}")

  print(f"Total score: {totalScore}")

# Part 2
print("Part 2")

outcomeScore = {
  "X": 0,
  "Y": 3,
  "Z": 6
}

def getOutcomeValue(outcome):
  return outcomeScore[outcome]

def determineRequiredShapeValue(outcomeValue, opponentValue):
  if (outcomeValue == 3):
    return opponentValue
  elif (outcomeValue == 0):
    strategyValue = opponentValue + 2
    strategyModulus = strategyValue % 3
    return strategyValue if strategyModulus == 0 else strategyModulus
  else:
    strategyValue = opponentValue - 2
    return strategyValue if strategyValue > 0 else strategyValue + 3

with open("./Day2/input.txt") as file:
  totalScore = 0
  for line in file:
    characters = line.split(" ")
    opponentEncoded = characters[0]
    outcome = characters[1].strip()

    opponentValue = decodeToValue(opponentEncoded)
    outcomeValue = getOutcomeValue(outcome)

    requiredShapeValue = determineRequiredShapeValue(outcomeValue, opponentValue)
    roundScore = outcomeValue + requiredShapeValue
    totalScore += roundScore
    print(f"Round score: {roundScore}")
  
  print(f"Total score: {totalScore}")