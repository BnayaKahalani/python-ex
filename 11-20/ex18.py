# Given string str. The task is to check whether it is a binary string or not. 

# Examples:  

# Input: str = "01010101010"
# Output: Yes

# Input: str = "geeks101"
# Output: No

def check_binary(str):
  is_binary = "Yes"
  for char in str:
    if char != "0" and char != "1":
      is_binary = "No"
      break
  print(is_binary) 
  
check_binary("geeks101")