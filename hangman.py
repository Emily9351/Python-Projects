import random

words = ['python', 'watch', 'flowers', 'skateboard', 'stuffed']

#Randomly choose a word
chosenWord = random.choice(words)
wordDisplay = ['_' for _ in chosenWord]
attempts = 8

print("Welcome to Hangman")

while attempts > 0 and '_' in wordDisplay:
    print("\n" + ' '.join(wordDisplay))
    guess = input("Guess a letter: ").lower()
    if guess in chosenWord:
        for index, letter in enumerate(chosenWord):
            if letter == guess:
                wordDisplay[index] = guess
    else:
        print("Letter does not appear in word")
        attempts -= 1

if '_' not in wordDisplay:
    print("Congrats you won! You correctly guessed the word: " + chosenWord)

else:
    print("You ran out of attempts. The correct word was: " + chosenWord)