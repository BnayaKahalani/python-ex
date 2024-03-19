# Given a String, compute all the characters, except spaces.

# Input : test_str = ‘geeksforgeeks 33 best’ 
# Output : 19 
# Explanation : Total characters are 19. 

# Input : test_str = ‘geeksforgeeks best’ 
# Output : 17 
# Explanation : Total characters are 17 except spaces.

def without_space(str):
  str_without_space = str.replace(" ","")
  print(len(str_without_space))
  
without_space("geeksforgeeks 33 best")