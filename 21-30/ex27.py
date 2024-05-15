# Sometimes, while working with Python strings, we can have a problem in which we need to find the frequency of next character of a particular word in string.

# Input : test_str = 'geeks are for geeksforgeeks', que_word = "geek" 
# Output : {'s': 3} 
# Input : test_str = 'geek', que_word = "geek" 
# Output : {}

import re 
     
test_str = 'geeksforgeeks is best for geeks. A geek should take interest.'
que_word = "geek"

def freq_next(string, que):  
  temp = [] 
  for sub in re.findall(que + '.', string): 
      temp.append(sub[-1]) 
  
  res = {que : temp.count(que) for que in temp} 
  
  print("The Characters Frequency is : " + str(res)) 
  
freq_next(test_str, que_word)