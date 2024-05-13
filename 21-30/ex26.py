# Sometimes while working with Python strings, we can have a problem in which we need to extract the frequency of all the words in a string. 

# Input : test_str = 'Gfg is best' 
# Output : {'Gfg': 1, 'is': 1, 'best': 1} 
# Input : test_str = 'Gfg Gfg Gfg' 
# Output : {'Gfg': 3}

def print_freq(test_str):
  print("The original string is : " + str(test_str))
  res = {key: test_str.count(key) for key in test_str.split()}
  print("The words frequency : " + str(res))
  
print_freq('Gfg is best . Geeks are good and Geeks like Gfg')