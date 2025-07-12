import random

def get_word():
    words = ["python", "hangman", "challenge", "programming", "developer", "keyboard", "function"]
    return random.choice(words).upper()

def display_hangman(tries):
    stages = [
        """
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          /    |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
          /|   |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
           |   |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
               |
               |
               |
        =========
        """,
        """
           -----
           |   |
               |
               |
               |
               |
        =========
        """
    ]
    return stages[6 - tries]

def play():
    word = get_word()
    word_letters = set(word)
    guessed_letters = set()
    tries = 6

    print("🎮 Welcome to Hangman!")
    print(display_hangman(tries))
    print("_ " * len(word))

    while tries > 0 and word_letters:
        guess = input("🔤 Guess a letter: ").upper()

        if not guess.isalpha() or len(guess) != 1:
            print("❌ Invalid input. Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("⚠️ You already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in word_letters:
            word_letters.remove(guess)
            print("✅ Good guess!")
        else:
            tries -= 1
            print("❌ Wrong guess.")

        word_display = [letter if letter in guessed_letters else "_" for letter in word]
        print(display_hangman(tries))
        print(" ".join(word_display))

    if not word_letters:
        print(f"🎉 Congratulations! You guessed the word: {word}")
    else:
        print(f"💀 Game Over! The word was: {word}")

if __name__ == "__main__":
    play()




