import random

def roll_dice(num_dice):
    total_score = 0
    for _ in range(num_dice):
        result = random.randint(1, 6)
        print(f"You rolled a {result}")
        total_score += result
    return total_score

def main():
    print("Welcome to the Dice Simulator!")

    while True:
        try:
            num_dice = int(input("Enter the number of dice to roll: "))
            if num_dice <= 0:
                print("Please enter a valid number of dice.")
                continue

            total_score = roll_dice(num_dice)
            print(f"Total score: {total_score}")

            play_again = input("Roll again? (yes/no): ").lower()
            if play_again != "yes":
                break
        except ValueError:
            print("Please enter a valid number.")

    print("Thanks for using the Dice Simulator!")

if __name__ == "__main__":
    main()
