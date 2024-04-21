# Given two sentences as strings A and B. The task is to return a list of all uncommon words. 
# A word is uncommon if it appears exactly once in any one of the sentences, and does not appear in the other sentence. 
# Note: A sentence is a string of space-separated words. Each word consists only of lowercase letters. 

# Examples:

# Input : A = “Geeks for Geeks”,  B = “Learning from Geeks for Geeks”
# Output : [‘Learning’, ‘from’]

# Input : A = “apple banana mango” , B = “banana fruits mango”
# Output : [‘apple’, ‘fruits’]

def check_uncommon(str1, str2):
  l1 = str1.split()
  l2 = str2.split()
  res = []
  
  for word in l1:
    if word not in l2 and word not in res:
      res.append(word)
      
  for word in l2:
    if word not in l1 and word not in res:
      res.append(word)
      
  print(res)

check_uncommon("Geeks for Geeks", "Learning from Geeks for Geeks")