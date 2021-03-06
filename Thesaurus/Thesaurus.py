# Import relevant libraries and packages
import json
from difflib import SequenceMatcher, get_close_matches

# Load in json data for dictionary of words and definitions
data = json.load(open("/Users/anthonycarannante/Desktop/Github_Repos/Udemy_Python_Apps/Real-World-Python-Applications/Thesaurus/data.json"))

# Define a function called translate to look up word in the json dictionary data
def translate(w):
    w = w.lower()

    # If statement for checking spelling of potentially mispelled words
    if w in data:
        return data[w]
    
    # If word is a proper noun (i.e., it's in sentence case)
    elif w.title() in data:
        return data[w.title()]
    
    # If a word is an acronym (i.e., it's in all caps)
    elif w.upper() in data:
        return data[w.upper()]

    # If the word is close in spelling to a word in the data file, ask the user if they meant the most closely related word
    elif len(get_close_matches(w, data.keys())) > 0:
        w_corr = get_close_matches(w, data.keys())[0]
        yn = input(f"Did you mean {w_corr}? Enter Y if yes, or N if no. ")
        if yn.upper() == "Y":
            return data[w_corr]
        elif yn.upper() == "N":
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your entrey."

    # If the word doesn't exist in the data
    else:
        return "The word doesn't exist. Please double check it."

# User input to look up a word
word = input("Enter word: ")

# Store word into a variable adn call the translate function
output = translate(word)

# Print the results
# If the output is a list, print all values in the list (i.e., each definition)
if type(output) == list:
    for item in output:
        print(item)
# If the word cannot be found, print just the output, not a list.
else:
    print(output)
