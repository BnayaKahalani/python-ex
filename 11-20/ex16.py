# A string is given, and you have to find all the words (substrings separated by a space) which are greater than the given length k.

# Examples:

# Input : str = "hello geeks for geeks 
#           is computer science portal" 
#         k = 4
# Output : hello geeks geeks computer 
#          science portal
# Explanation : The output is list of all 
# words that are of length more than k.
# Input : str = "string is fun in python"
#         k = 3
# Output : string python 

def find_words(str, k):
  l = str.split()
  res = []
  for word in l:
    if len(word) > k:
      res.append(word)
  print(" ".join(res))
  
find_words("string is fun in python", 3)