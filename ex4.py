# Given a string. The task is to print all words with even length in the given string.

# Examples: 

# Input: s = "This is a python language"
# Output: This is python language

# Input: s = "i am laxmi"
# Output: am

def print_even(str):
  splitted_str = str.strip().split()
  res = []
  for word in splitted_str:
    if len(word) % 2 == 0:
      res.append(word)
  print(" ".join(res))
  
print_even("i am laxmi")
  