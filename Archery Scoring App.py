# By Tomas Williams
# Archery Score Recorder
# Last Updated 7/11/20
from tabulate import tabulate


class Game:
    def __init__(self, numberOfRounds: int, arrowsPerRound: int):
        self.roundNums = numberOfRounds
        self.arrows = arrowsPerRound
        self.HEADER = ['ROUND']+[f'Arrow {i}' for i in range(1,self.arrows+1)]+['Round Score', 'Running Total', 'Xs']
        self.table = []
        self.runningScore = 0
        self.roundScore = []
        self.outputTable()

    def currentRound(self) -> list:
        currentRoundScore = []
        for i in range(self.arrows):
            print('''
            [*] Scoring
            If the arrow was a miss input "m"
            If the arrow was an X input "x"
            ''')
            hit = input('Arrow Score: ')
            if hit.lower() == 'm':
                currentRoundScore.append(str('M'))
            elif hit.lower() == 'x':
                currentRoundScore.append(str('X'))
            else:
                currentRoundScore.append(int(hit))
        return currentRoundScore

    def outputTable(self):
        print(tabulate(self.table, self.HEADER, tablefmt='grid'))


if __name__ == '__main__':
    number_of_rounds = int(input('How many rounds are you shooting: '))
    arrows_per_round = int(input('How many arrows are you shooting each round: '))
    Game(number_of_rounds, arrows_per_round)
