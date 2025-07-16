import random

def play_game():
    lucky_number = random.randint(1, 100)
    rounds = 0

    def lottery_ticket(x):
        nonlocal rounds
        if x == 50:
            rounds = 1
        elif x == 100:
            rounds = 3
        elif x == 200:
            rounds = 10
        else:
            print("❌ Invalid ticket amount. Choose 50, 100, or 200.")

    # Get ticket input
    try:
        ticket = int(input("🎟️ Enter your ticket amount (50 / 100 / 200): "))
        lottery_ticket(ticket)
    except ValueError:
        print("❌ Please enter a valid number for ticket.")
        return

    if rounds == 0:
        print("⚠️ Game cannot continue without a valid ticket.")
        return
    else:
        print(f"✅ You've got {rounds} chance(s) to guess the lucky number!\n")

    i = 0
    while i < rounds:
        try:
            guess = int(input(f"🔢 Guess #{i+1}: Enter a number between 1 and 100: "))
        except ValueError:
            print("❌ Invalid input. Please enter a number only!")
            continue  # Don't count this as an attempt

        if not (1 <= guess <= 100):
            print("🚫 Guess out of range! Enter a number between 1 and 100.")
            continue  # Don't count this as an attempt

        if guess == lucky_number:
            print(f"🎉 Congratulations! {guess} is the lucky number. You Won! 🎊")
            break
        else:
            if guess > lucky_number:
                print(f"{guess} is not the lucky number.\nHint: Try a smaller number ⬇️\n")
            else:
                print(f"{guess} is not the lucky number.\nHint: Try a larger number ⬆️\n")
            i += 1  # Only count valid guesses

    else:
        print(f"😢 Out of chances! The lucky number was {lucky_number}. Better luck next time.")

# 🔁 Main game loop
while True:
    play_game()
    again = input("\n🔁 Do you want to play again? (yes/no): ").strip().lower()
    if again != "yes":
        print("👋 Thanks for playing! Goodbye!")
        break
