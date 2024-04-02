# Given a string, count the number of vowels present in the given string using Sets. 
# You can use sets to count the number of vowels in a given string in Python. 
# Sets are useful to efficiently check for counting the unique occurrences of vowels.

# Input : GeeksforGeeks
# Output : No. of vowels : 5
# Explaination: The string GeeksforGeeks contains 5 vowels in it 4 letter of 'e' and 1 'o'.

def count_vowels(str):
  vowels = {"a", "e", "i", "o", "u"}
  count = 0
  for i in str.lower():
    if i in vowels:
      count += 1
  print(count)
  
count_vowels("GeeksforGeeks")
  