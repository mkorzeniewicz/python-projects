### WISIELEC
import random

wordList = ["zestaw", "ruch", "zapomnieć", "Reklama", "włosy", "pozostawać", "zachowanie", "student", "brat", "republikański", "chłopak", "papier", "strategia", "prosty", "sami", "spadek", "cały", "zastosować", "kulturalny", "technologia", "krótki", "może", "zewnątrz", "gwiazda"]

def wordLottery ():
    return wordList[random.randint(0,len(wordList))]

selectedWord = wordLottery()
howManyCharacters = len(selectedWord)

print("siema ziomus gramy w wisielca. Dajemy ci liczbe liter a ty rzucasz literami tak zeby odgadnac slowo")
print(selectedWord, "dajemy ci: ", howManyCharacters, " liter")

noGuessedLetters = 0

while(noGuessedLetters != howManyCharacters):
    pickedLetter = input("podaj litere: ")

    if pickedLetter in selectedWord:
        #print("osu")
        noGuessedLetters = noGuessedLetters + 1
    #else:
        #print("probuj dalej")

    countLetters = 0

    while howManyCharacters > countLetters:
        if pickedLetter == selectedWord[countLetters]:
            print(pickedLetter, end=" ")
        else:
            print("*", end=" ")
        countLetters = countLetters + 1

    print()



