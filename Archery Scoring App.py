#Archery Scoring APP

def CurrentRoundScoring(ArrowNumber,NumberOfXs,NumberOfMisses):
  score = list(map(str, input("\nEnter the scores separated by space : ").strip().split()))
  list(score)

  for i in range (len(score)):
    if score[i] == 'x':
      NumberOfXs = NumberOfXs + 1
      score[i] = int(10)

  for i in range (len(score)):
    if score[i] == 'm':
      score[i] = int(0)
      NumberOfMisses = NumberOfMisses + 1
    
  if len(score) > ArrowNumber:
    print("\nThere is an ERROR with the score please redo this rounds scores!!!")
    CurrentRoundScoring(ArrowNumber,NumberOfXs,NumberOfMisses)

  else:
    return score, NumberOfXs, NumberOfMisses

def CurrentScore(RoundScore,Score):
  for i in range (len(RoundScore)):
      Score = Score + int(RoundScore[i])

  return Score

def __main__():
    ArrowNumber = int(input("How many ARROWS are you shooting?:  "))
    RoundNumber  = int(input("\nHow many ROUNDS are you shooting?:  "))
    NumberOfXs = 0
    NumberOfMisses = 0
    Score = 0
    for i in range (RoundNumber):
      RoundScore,NumberOfXs,NumberOfMisses = CurrentRoundScoring(ArrowNumber,NumberOfXs,NumberOfMisses)
      Score = CurrentScore(RoundScore,Score)
      print("Your score so far is",Score)
      print("you've missed",NumberOfMisses,"times")
      print("You've hit the X",NumberOfXs,"times")
    

__main__()
