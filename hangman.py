import random

def hangman():
    list = random.choice(["mumbai","delhi","dublin","tokyo","newyork","london","wuhan","berlin","nairobi","rio"])
    validletters='abcdefghijklmnopqrstuvwxyz'
    turns =10
    guessmade=''
    while len(list) > 0:
        main =""

        for letter in list:
            if letter in guessmade:
                main += letter
            else:
                main = main + "_" + ""

        if main == list:
            print("You won the game")
            break

        print("Guess the word:", main)
        guess = input()

        if guess in validletters:
            guessmade = guessmade + guess
        else:
            while guess not in validletters:
                print("Enter a valid character")
                guess = input()
        if guess not in list:
            turns -= 1

            if turns == 9:
                print("turns left:",turns)
                print("  --------  ")
            if turns == 8:
                print("turns left:",turns)
                print("  --------  ")
                print("     O      ")
            if turns == 7:
                print("turns left:",turns)
                print("  --------  ")
                print("     O      ")
                print("     |      ")
            if turns == 6:
                print("turns left:",turns)
                print("  --------  ")
                print("     O      ")
                print("     |      ")
                print("    /       ")
            if turns == 5:
                print("turns left:",turns)
                print("  --------  ")
                print("     O      ")
                print("     |      ")
                print("    / \     ")
            if turns == 4:
                print("turns left:",turns)
                print("  --------  ")
                print("   \ O      ")
                print("     |      ")
                print("    / \     ")
            if turns == 3:
                print("turns left:",turns)
                print("  --------  ")
                print("   \ O /    ")
                print("     |      ")
                print("    / \     ")
            if turns == 2:
                print("turns left:",turns)
                print("  --------  ")
                print("   \ O /|   ")
                print("     |      ")
                print("    / \     ")
            if turns == 1:
                print("turns left:",turns)
                print("Last breaths counting, Take care!")
                print("  --------  ")
                print("   \ O_|/   ")
                print("     |      ")
                print("    / \     ")
            if turns == 0:
                print("You loose")
                print("You let a kind man die")
                print("  --------  ")
                print("     O_|    ")
                print("    /|\      ")
                print("    / \     ")
                break


name=input("Enter user name\n")
print(f"Wecome {name} to the Hangman game")
print("----------------------------------")
print("Try to guess the the Famous city in less than 10 attempts")
hangman()
