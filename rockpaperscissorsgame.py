import random
user_score = 0
computer_score = 0
choices = ["rock", "paper", "scissors"]
print("=" * 40)
print("    WELCOME TO ROCK, PAPER, SCISSORS")
print("=" * 40)
print("Rules:")
print("- Rock beats Scissors")
print("- Scissors beats Paper")
print("- Paper beats Rock")
print()
while True:
    user_choice = input("Enter rock, paper, or scissors: ").lower()
    if user_choice not in choices:
        print("Invalid choice! Please try again.\n")
        continue
    computer_choice = random.choice(choices)
    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    if user_choice == computer_choice:
        print("Result: It's a tie!")
    elif (
        (user_choice == "rock" and computer_choice == "scissors")
        or (user_choice == "paper" and computer_choice == "rock")
        or (user_choice == "scissors" and computer_choice == "paper")
    ):
        print("Result: You win!")
        user_score += 1
    else:
        print("Result: You lose!")
        computer_score += 1
    print("\nCurrent Scores:")
    print(f"User: {user_score}")
    print(f"Computer: {computer_score}")
    play_again = input("\nDo you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("\nFinal Scores:")
        print(f"User: {user_score}")
        print(f"Computer: {computer_score}")
        if user_score > computer_score:
            print("Congratulations! You are the overall winner!")
        elif computer_score > user_score:
            print("Computer is the overall winner!")
        else:
            print("The game ended in a tie!")
        print("\nThank you for playing!")
        break
    print("\n" + "-" * 40)