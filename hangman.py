import random
words = ["python", "java", "computer", "hacker", "painter"]

# Player decides if he wants to use his own word or a random word from a list
if input("Do you want to use your own word? (y/n) ") == "y":
    word = input("Enter your word: ")
else:
    print("Random word will be chosen.")
    word = random.choice(words)

# The word to be guessed is represented by a list of underscores
guessed_word = ["_"] * len(word)
attempts = 6
while (attempts > 0):
    print("".join(guessed_word))
    letter = input("Enter a letter: ")
    if letter in word:
        for i in range(len(word)):
            if word[i] == letter:
                guessed_word[i] = letter
        if "_" not in guessed_word:
            print("You won!")
            break
    else:
        print("Letter not in word.")
        attempts -= 1
        print(f"Attempts left: {attempts}")
        continue

print(f"The word was {word}.")
