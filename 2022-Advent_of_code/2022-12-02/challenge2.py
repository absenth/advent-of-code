

def main():
  # This should determine if the match was a win, draw, or loss
  # Winning score = 6, Tie = 3, Loss = 0
  # A beats Z | Z beats B
  # B beats X | X beats C
  # C beats Y | Y beats A
  # Ties = AX | BY | CZ
  score, wins, losses, ties = 0, 0, 0, 0
  with open('input2.txt') as game_input:
    for game in game_input:
      play = game.strip()[-1]
      outcome = game_outcome[game.strip()]
      if outcome == 0:
        losses += 1
      elif outcome == 3:
        ties += 1
      elif outcome == 6:
        wins += 1
      score += outcome

      if "X" in game:
        score += 1
      if "Y" in game:
        score += 2
      if "Z" in game:
        score += 3
      print(f"total: {score}, wins: {wins}, Losses: {losses}, Ties: {ties}")


game_outcome = {
  'A X': 3,
  'A Y': 6,
  'A Z': 0,
  'B X': 0,
  'B Y': 3,
  'B Z': 6,
  'C X': 6,
  'C Y': 0,
  'C Z': 3,
}


if __name__ == '__main__':
  main()