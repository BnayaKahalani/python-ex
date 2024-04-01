# We are given a string and we need to reverse words of a given string

# Examples:

# Input : str =" geeks quiz practice code"
# Output : str = code practice quiz geeks  
# Input : str = "my name is laxmi"
# output : str= laxmi is name my 

# Reverse the words in the given string program 

def reverse(str):
  splitted_str = str.strip().split()
  reversed_str = " ".join(splitted_str[::-1])
  print(reversed_str)
  
reverse("my name is laxmi")