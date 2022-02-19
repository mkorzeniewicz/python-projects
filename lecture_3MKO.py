### WISIELEC
import random

hangman = [
    "=========\n\
  +---+\n\
  |   |\n\
      |\n\
      |\n\
      |\n\
      |\n\
=========",
    "=========\n\
  +---+\n\
  |   |\n\
  O   |\n\
      |\n\
      |\n\
      |\n\
=========",
    "=========\n\
  +---+\n\
  |   |\n\
  O   |\n\
  |   |\n\
      |\n\
      |\n\
=========",
    "=========\n\
  +---+\n\
  |   |\n\
  O   |\n\
 /|   |\n\
      |\n\
      |\n\
=========",
    "=========\n\
  +---+\n\
  |   |\n\
  O   |\n\
 /|\  |\n\
      |\n\
      |\n\
=========",
    "=========\n\
  +---+\n\
  |   |\n\
  O   |\n\
 /|\  |\n\
 /    |\n\
      |\n\
=========",
    "=========\n\
  +---+\n\
  |   |\n\
  O   |\n\
 /|\  |\n\
 / \  |\n\
      |\n\
========="]

uknownCharacter = "*"
wordList = ["zestaw", "ruch", "zapomnieć", "Reklama", "włosy", "pozostawać", "zachowanie", "student", "brat",
            "republikański", "chłopak", "papier", "strategia", "prosty", "sami", "spadek", "cały", "zastosować",
            "kulturalny", "technologia", "krótki", "może", "zewnątrz", "gwiazda"]
wordToGuess = wordList[random.randint(0, len(wordList))]
wordToPrint = list(uknownCharacter * len(wordToGuess))
# len(wordToGuess)
print("siema ziomus gramy w wisielca. Dajemy ci liczbe liter a ty rzucasz literami tak zeby odgadnac slowo")
print("dajemy ci: ", len(wordToGuess), " liter")

noGuessedLetters = 0
noFailedGuesses = 0

while noGuessedLetters != len(wordToGuess):
    pickedLetter = input("podaj litere: ")

    i = 0
    isLetterCorrect=False;
    while i < len(wordToGuess):
        letter = wordToGuess[i]
        if wordToPrint[i] == uknownCharacter:
            if pickedLetter == letter:
                noGuessedLetters += 1
                wordToPrint[i] = wordToGuess[i]
                isLetterCorrect=True
        i += 1
    if not isLetterCorrect:
        noFailedGuesses += 1
    print(hangman[noFailedGuesses])
    for letter in wordToPrint:
        print(str(letter), end=" ")
    print()
print()
print("Brawo, Brawo, Brawissimo!")
