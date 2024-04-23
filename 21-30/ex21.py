# The problem is quite simple. Given a string, we need to replace all commas with dots and all dots with the commas. 
# This can be achieved in many different ways. 
# Examples: 

# Input : 14, 625, 498.002
# Output : 14.625.498, 002 

def replace_commas(str):
  result = ""
  for char in str:
      if char == ', ':
          result += '.'
      elif char == '.':
          result += ', '
      else:
          result += char
  print(result)

replace_commas("14, 625, 498.002")