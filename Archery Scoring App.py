# By Tomas Williams
# Archery Score Recorder
# Last Updated 7/11/20
from tabulate import tabulate


class Game:
    def __init__(self, numberOfRounds: int, arrowsPerRound: int):
        self.roundNums = numberOfRounds
        self.arrows = arrowsPerRound
        self.HEADER = ['ROUND'] + [f'Arrow {i}' for i in range(1, self.arrows + 1)] + ['Round Score',
                                                                                       'Running Total', 'No. of Xs']
        self.table = []
        self.round = 1
        self.roundScores = []
        self.runningScore = 0
        self.currentRound()
        self.formatTable()
        self.outputTable()

    def currentRound(self):
        for _ in range(self.roundNums):
            self.roundScores.append(self.collectArrows())

    def collectArrows(self) -> list:
        currentRoundScore = []
        currentRoundScore.insert(0, self.round)
        allowed = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'x', 'm']
        arrows = 1
        print(f'''
            [*] Scoring Round {self.round}
            
            If the arrow was a miss input "m"
            If the arrow was an X input "x"
            ''')
        while arrows != self.arrows + 1:
            hit = input(f'Arrow {arrows} Score: ')
            if hit == '' or hit not in allowed:
                print('''
            Error
            PLEASE ENTER A NUMBER
            YOUR INPUT HAS NOT BEEN ADDED
                ''')
                continue
            elif hit.lower() == 'm':
                currentRoundScore.append(str('M'))
                arrows += 1
            elif hit.lower() == 'x':
                currentRoundScore.append(str('X'))
                arrows += 1
            else:
                currentRoundScore.append(hit)
                arrows += 1
        self.round += 1
        return currentRoundScore

    def formatTable(self):
        print('rounscore 2' + str(self.roundScores))
        for i in range(len(self.roundScores[0:])):
            roundScore = 0
            for j in range(1, len(self.roundScores[i])):
                print(self.roundScores[i][j])
                if self.roundScores[i][j] == 'M':
                    pass
                elif self.roundScores[i][j] == 'X':
                    roundScore += 10
                else:
                    roundScore += int(self.roundScores[i][j])
            self.runningScore += roundScore
            self.roundScores[i].append(roundScore)
            self.roundScores[i].append(self.runningScore)

    def outputTable(self):
        for i in self.roundScores:
            self.table.append(i)
        print('\n')
        print(tabulate(self.table, self.HEADER, tablefmt='grid', stralign='right'))


if __name__ == '__main__':
    number_of_rounds = int(input('How many rounds are you shooting: '))
    arrows_per_round = int(input('How many arrows are you shooting each round: '))
    Game(number_of_rounds, arrows_per_round)
