

def main():
  '''
    A = Rock | B = Paper | C = Scissors
    X = Lose | Y = Draw | Z = Win
  '''
  score = 0
  with open('input2.txt') as game_input:
    for game in game_input:
      outcome = game_outcome[game.strip()]
      score += (outcome["wl"] + outcome["ps"])

    print(f'total: {score}')


game_outcome = {
  'A X': { 'wl': 0, 'ps': 3,},
  'A Y': { 'wl': 3, 'ps': 1,},
  'A Z': { 'wl': 6, 'ps': 2,},
  'B X': { 'wl': 0, 'ps': 1,},
  'B Y': { 'wl': 3, 'ps': 2,},
  'B Z': { 'wl': 6, 'ps': 3,},
  'C X': { 'wl': 0, 'ps': 2,},
  'C Y': { 'wl': 3, 'ps': 3,},
  'C Z': { 'wl': 6, 'ps': 1,},
}

if __name__ == '__main__':
  main()