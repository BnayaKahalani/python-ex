# Given an Integer list, perform join with the delimiter, avoiding the extra delimiter at the end.

# Input : test_list = [4, 7, 8, 3, 2, 1, 9], delim = “*” 
# Output : 4*7*8*3*2*1*9 
# Explanation : The rear “*” which usually occurs in concatenation, is avoided.

# Input : test_list = [4, 7, 8, 3], delim = “*” 
# Output : 4*7*8*3 
# Explanation : The rear “*” which usually occurs in concatenation, is avoided. 

def join_delimiter(test_list):
 
  print("The original list is : " + str(test_list))
  
  delim = "$"
  
  res = delim.join(map(str, test_list))
  
  print("The joined string : " + str(res))

join_delimiter([4, 7, 8, 3, 2, 1, 9])