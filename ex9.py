# Given a string, the task is to check if every vowel is present or not. 
# We consider a vowel to be present if it is present in upper case or lower case. 
# i.e. ‘a’, ‘e’, ‘i’.’o’, ‘u’ or ‘A’, ‘E’, ‘I’, ‘O’, ‘U’ . 

# Examples : 

# Input : geeksforgeeks
# Output : Not Accepted
# All vowels except 'a','i','u' are not present

# Input : ABeeIghiObhkUul
# Output : Accepted
# All vowels are present

def every_vowel(str):
    vowels = ['a', 'e', 'i', 'o', 'u']
    res = all(char.lower() in str.lower() for char in vowels)
    print("Accepted") if res == True else print("Not accepted")

every_vowel("ABeeIghiObhkUul")