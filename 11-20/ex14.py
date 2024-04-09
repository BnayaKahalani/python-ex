# Given a string, the task is to check if that string contains any special character (defined special character set). 
# If any special character is found, don’t accept that string.

# Examples : 

# Input : Geeks$For$Geeks
# Output : String is not accepted.
# Input : Geeks For Geeks
# Output : String is accepted

def check_special(str):
  are_letters = str.replace(" ", "").isalpha()
  if are_letters:
    print("String is accepted")
  else:
    print("String is not accepted")

check_special("Geeks$For$Geeks")

