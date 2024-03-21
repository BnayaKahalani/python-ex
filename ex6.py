# Given a String, perform uppercase of the later part of the string.

# Input : test_str = 'geeksforgeek' 
# Output : geeksfORGEEK 
# Explanation : Latter half of string is uppercased. 
# Input : test_str = 'apples' 
# Output : appLES 
# Explanation : Latter half of string is uppercased.

def later_upper(str):
  mid = len(str)//2
  res = str[:mid]+str[mid:].upper()
  print(res)
  
later_upper('apples')