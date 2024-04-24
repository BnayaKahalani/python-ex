# The problem is quite simple. Given a string, we need to replace all commas with dots and all dots with the commas. 
# This can be achieved in many different ways. 
# Examples: 

# Input : 14, 625, 498.002
# Output : 14.625.498, 002 

def replace_commas(str):
  result = ""
  i = 0
  while i < len(str):
      if str[i] == ',':
          result += '.'
      elif str[i] == '.':
          result += ', '
      else:
          result += str[i]
      if i < len(str) - 1 and str[i + 1] == ' ':
          i += 1
      i += 1
  print(result)

replace_commas("14, 625, 498.002")