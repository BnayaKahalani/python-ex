# Sometimes, while working with Python Strings, we have problem in which we need to perform a case conversion of String. 

# Input : geeks_for_geeks Output : GeeksforGeeks Input : left_index Output : leftIndex

import string

def case_conv(test_str):
  
  print("The original string is : " + test_str)
  res = string.capwords(test_str.replace("_", " ")).replace(" ", "")
  print("The String after changing case : " + str(res)) 

case_conv('geeksforgeeks_is_best')