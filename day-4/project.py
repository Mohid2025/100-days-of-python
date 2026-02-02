import random

# ASCII Art for choices
ROCK = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

PAPER = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

SCISSORS = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

def get_player_choice():
    """Get player's choice input"""
    while True:
        print("\nEnter your choice:")
        print("1 = Rock")
        print("2 = Paper")
        print("3 = Scissors")
        
        choice = input("Your choice (1/2/3): ").strip()
        
        if choice in ['1', '2', '3']:
            return int(choice)
        else:
            print("Invalid input! Please enter 1, 2, or 3.")

def get_computer_choice():
    """Get random computer choice"""
    return random.randint(1, 3)

def get_choice_name(choice):
    """Convert choice number to name"""
    choices = {1: "Rock", 2: "Paper", 3: "Scissors"}
    return choices[choice]

def get_ascii_art(choice):
    """Return ASCII art for the choice"""
    art = {1: ROCK, 2: PAPER, 3: SCISSORS}
    return art[choice]

def determine_winner(player, computer):
    """Determine winner and return result"""
    if player == computer:
        return "tie"
    elif (player == 1 and computer == 3) or \
         (player == 2 and computer == 1) or \
         (player == 3 and computer == 2):
        return "player"
    else:
        return "computer"

def play_game():
    """Main game function"""
    print("=" * 40)
    print("   ROCK PAPER SCISSORS GAME")
    print("=" * 40)
    
    while True:
        # Get choices
        player_choice = get_player_choice()
        computer_choice = get_computer_choice()
        
        # Get names
        player_name = get_choice_name(player_choice)
        computer_name = get_choice_name(computer_choice)
        
        # Display choices with ASCII art
        print("\n" + "=" * 40)
        print("YOUR CHOICE: " + player_name)
        print(get_ascii_art(player_choice))
        
        print("=" * 40)
        print("COMPUTER'S CHOICE: " + computer_name)
        print(get_ascii_art(computer_choice))
        print("=" * 40)
        
        # Determine winner
        result = determine_winner(player_choice, computer_choice)
        
        if result == "tie":
            print("\n🤝 IT'S A TIE! 🤝")
        elif result == "player":
            print("\n🎉 YOU WIN! 🎉")
        else:
            print("\n💻 COMPUTER WINS! 💻")
        
        # Ask to play again
        play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
        if play_again not in ['yes', 'y']:
            print("\nThanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    play_game()
