shapeScore = {
  "R": 1,
  "P": 2,
  "S": 3
}
outcomeScore = {
  "L": 0,
  "D": 3,
  "W": 6
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
  input = file.readlines()

  totalScore = 0
  for line in input:
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