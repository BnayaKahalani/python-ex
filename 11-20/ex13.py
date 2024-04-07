# Given a String list, extract frequency of specific characters in the whole strings list.

# Input : test_list = [“geeksforgeeks is best for geeks”], chr_list = [‘e’, ‘b’, ‘g’, ‘f’] 
# Output : {‘g’: 3, ‘e’: 7, ‘b’: 1, ‘f’ : 2} 
# Explanation : Frequency of certain characters extracted. 

# Input : test_list = [“geeksforgeeks”], chr_list = [‘e’, ‘g’] 
# Output : {‘g’: 2, ‘e’: 4} 
# Explanation : Frequency of certain characters extracted.

def char_freq(test_list, char_list):
  res = {}
  
  for char in test_list:
    if char in char_list:
      res[char] = res.get(char, 0) + 1
  print (res)
  
char_freq("geeksforgeeks is best for geeks", ["e", "b", "g", "f"])
  
