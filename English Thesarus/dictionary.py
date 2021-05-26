import json
import difflib
from difflib import get_close_matches
data = json.load(open("data.json",'r'))

def translate(word):
    word = word.lower()
    if word in data:
        t = 1
        for i in data[word]:
            print("Meaning ",t,": ",i)
            t+=1
    elif len(get_close_matches(word,data.keys(),cutoff=0.8)) > 0:
        # print(len(get_close_matches(word,data.keys())))
        yn = input("Did you mean %s instead? Enter Y for yes or Enter N for No: " % get_close_matches(word,data.keys(),cutoff = 0.8)[0])
        if yn == 'Y':
            translate(get_close_matches(word,data.keys(),cutoff = 0.8)[0])
        elif yn == 'N':
            print("Okay, try again with a different word.")
        else:
            print("We didn't understand your entry. Try again later!")
    else:
        print("The word doesn't exist.Please try again.")

word = input("Enter word: ")
translate(word)