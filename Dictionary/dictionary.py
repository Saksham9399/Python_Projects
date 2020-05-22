import json #importing json library
from difflib import get_close_matches # A library to get similar words related to the users input

data = json.load(open("original.json")) #importing data of Json file in the data variable

i="t" # variable to continue the loop for the dictionary

def translate(x): #function to search in dectionary
    x= x.lower()
    if x in data:
        return (data[x])
    elif x.title() in data:
        return (data[x.title()])
    elif x.upper() in data:
        return (data[x.upper()])
    elif len(get_close_matches(x,data.keys())) > 0: # using this library we are searching through the closest words related to the entered word
        print("Did you mean %s instead" %get_close_matches(x,data.keys())[0])
        decide= input("press y for yes and n for no\n")
        if decide=="y":
             return data[get_close_matches(x,data.keys())[0]]
        elif decide=="n":
            return("The word entered is invalid.\n Please enter a valid word\n")
        else:
            return("You have entered wrong input. Please enter y or n")

    else:
        print("The word entered is invalid.\n Please enter a valid word\n")

while(i=="t"):
    word = input("Enter the word you want to search in the dictionary\n")
    output=translate(word)
    if type(output) == list:
        for y in output:
            print(y)


    i=input("Press t to continue with your search \n---------or---------\nPress any other letter to quit\n")
