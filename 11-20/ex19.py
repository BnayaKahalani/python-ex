# We are given a list of pattern strings and a single input string. 
# We need to find all possible close good enough matches of input string into list of pattern strings. Examples:

# Input : patterns = ['ape', 'apple', 
#                   'peach', 'puppy'], 
#           input = 'appel'
# Output : ['apple', 'ape']

from difflib import get_close_matches

def closeMatches(patterns, word):
     print(get_close_matches(word, patterns))
     
word = 'appel'
patterns = ['ape', 'apple', 'peach', 'puppy']
closeMatches(['ape', 'apple', 'peach', 'puppy'], 'appel')
     
     