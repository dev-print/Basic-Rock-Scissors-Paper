import random

def check_result(bot_choice, player_choice):
  if bot_choice == player_choice:
    return "draw"  
  elif (
      (bot_choice == "rock" and player_choice == "paper")
      or (bot_choice == "paper" and player_choice == "scissors")
      or (bot_choice == "scissors" and player_choice == "rock")
  ):
    return "player"  
  else:
    return "bot"  


def print_result(bot_choice, player_choice, result, win_streak):
  """Gibt das Ergebnis aus."""
  print(f"Enemy Choosed: {bot_choice}")
  if result == "draw":
    print("You both got the Same.")
  elif result == "player":
    print("You Win!")
    print("Added +1 to win Streak!")
  elif result == "bot":
    print("You loose!")
    if win_streak >= 1:
      print("Removed Winstreak.")
    else:
      print("No winstreak to remove")
  
def main():
  bot_options = ["rock", "paper", "scissors"]
  win_streak = 0

  start_message = input("Do you want to Play Rock, Paper, Scissors? (y/n): ")

  if start_message.lower() == "y":
      while True:
          bot_choice = random.choice(bot_options)
          player_choice = input(
              "Rock, Paper, Scissors? (say 'winstreak' to see your winstreak or 'exit' to quit.) "
          ).lower()

          if player_choice == "winstreak":
              if win_streak >= 1:
                print(f"You got an Winstreak of: {win_streak}")
              else:
                print("You got no active winstreak.")
              continue
          if player_choice == "exit":
            print("Thank you for playing.")
            break
          
          if player_choice not in bot_options:
            print("Invalid choice, please chose: rock, paper, scissors, winstreak or exit")
            continue

          result = check_result(bot_choice, player_choice)
          print_result(bot_choice,player_choice,result, win_streak)

          if result == "player":
            win_streak +=1
          elif result == "bot":
            win_streak = 0
  else:
    print("Maybe next time.")

if __name__ == "__main__":
  main()
