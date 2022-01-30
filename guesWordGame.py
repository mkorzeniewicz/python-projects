import random

#5 prób żeby zgadnąć słowo
#słowo jest 5 literowe
#jeżeli w poprzedniej próbie litera była na własciwym miejscu to jest zaznaczona
#jeżeli w poprzedniej próbie litera istnieje w słowie ale nei była na dobrym miejscu to zaznaczona
from locale import str


class bcolors:
    OKGREEN = '\033[92m'
    WRONG_PLACE = '\033[93m'
    ENDC = '\033[0m'

#Funkcja do sprawdzania czy przekazane słowo ma taką długość jaką przekażemy
def checkIfCorrectNoCharacters(word, noCharacters):
    wordLength = len(word)
    if noCharacters == wordLength:
        return True;
    else:
        return False;

def compareAndPrint(firstWord, secondWord):
    i = 0
    isStillSame = True
    while i < len(firstWord):
        if firstWord[i] == secondWord[i]:
            print(bcolors.OKGREEN + secondWord[i] + bcolors.ENDC, end=" ")
        elif firstWord[i] in secondWord:
            print(bcolors.WRONG_PLACE + secondWord[i] + bcolors.ENDC, end=" ")
            isStillSame = False
        else:
            print(secondWord[i], end=" ")
            isStillSame = False
        i += 1
    return isStillSame

#print(bcolors.OKGREEN + "Warning: No active frommets remain. Continue?" + bcolors.ENDC)

wordList = ["zestaw", "ruch", "zapomnieć", "Reklama", "włosy", "pozostawać", "zachowanie", "student", "brat", "republikański", "chłopak", "papier", "strategia", "prosty", "sami", "spadek", "cały", "zastosować", "kulturalny", "technologia", "krótki", "może", "zewnątrz", "gwiazda"]
currentTryNumber = 1;
maxNoTries = 5
noWords = len(wordList)
#print(noWords)
randomIndexOfWord = random.randint(0,noWords)-1
#print(randomIndexOfWord)
wordToGuess = wordList[randomIndexOfWord]
#print(wordToGuess)
lengthOfWordToGues = len(wordToGuess)
print("Witaj w grze. Twoim zadaniem jest odgadnąć " + str(len(wordToGuess)) + " literowe słowo. Masz " + str(maxNoTries) + " prób. Powodzenia")

#print(containCorrectNoLetters)

while currentTryNumber < maxNoTries:
    enteredWord = input(str(currentTryNumber) + " próba. Dawaj: ")
    currentTryNumber += 1
    containCorrectNoLetters = checkIfCorrectNoCharacters(enteredWord, len(wordToGuess))
    if containCorrectNoLetters == False:
        print("Chyba nie umiesz liczyć. Miało być " + str(lengthOfWordToGues) + " liter, a twoje " + enteredWord + " ma " + str(len(enteredWord)) + " liter")
        continue
    isSame = compareAndPrint(wordToGuess, enteredWord)
    print()
    if isSame:
        print("Brawo, zgadłeś!")
        exit()

print("Przegrałeś. Zapraszamy ponownie!")
exit()

