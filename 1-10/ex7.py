# Python program to capitalize the first and last character of each word in a string
# Given the string, the task is to capitalize the first and last character of each word in a string. 

# Examples:

# Input: hello world 
# Output: HellO WorlD

# Input: welcome to geeksforgeeks
# Output: WelcomE TO GeeksforgeekS

def capitalize_first_last(str):
  splitted = str.split()
  capitalized = []
  for word in splitted:
    word = word.capitalize()
    word = word[:len(word)-1] + word[-1].upper()
    capitalized.append(word)
  res = " ".join(capitalized)
  print(res)
    
  
capitalize_first_last("welcome to geeksforgeeks")