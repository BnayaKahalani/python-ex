# Given a string in Python. The task is to check whether the string has at least one letter(character) and one number. 
# Return “True” if the given string fully fill the above condition else return “False” (without quotes).

# Examples: 

# Input: welcome2ourcountry34
# Output: True

# Input: stringwithoutnum
# Output: False

def find_letter_number(str):
  flag_l = False
  flag_n = False

  for i in str:

    if i.isalpha():
      flag_l = True
      
    if i.isdigit():
      flag_n = True

  print(f"{flag_l and flag_n}")
    
find_letter_number("welcome2ourcountry34")