import json
from difflib import get_close_matches

# This load function is quite costly. If the json file size is large, it's gonna take some time. So, we can use DB instead for optimization.
data = json.load(open("data.json",'r'))

def translate(word):
    if word in data:
        return data[word]
    elif word.lower() in data:
        return data[word.lower()]
    elif word.title() in data: #if user entered "texas" this will check for "Texas" as well.
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word,data.keys(),cutoff=0.8)) > 0:
        yn = input("Did you mean %s instead? Enter Y for yes or Enter N for No: " % get_close_matches(word,data.keys(),cutoff = 0.8)[0])
        if yn == 'Y':
            return translate(get_close_matches(word,data.keys(),cutoff = 0.8)[0])
        elif yn == 'N':
            return "Okay, try again with a different word."
        else:
            return "We didn't understand your entry. Try again later!"
    else:
        print("The word doesn't exist.Please try again.")

word = input("Enter word: ")
print(data.keys())
output = translate(word)
if type(output) == list:
    t = 1
    for item in output:
        print("Meaning ",t,": ",item)
        t+=1
else:
    print(output)
