# Given a pair of non-empty strings. Count the number of matching characters in those strings 
# (consider the single count for the character which have duplicates in the strings). 

# Examples:

# Input : str1 = 'abcdef'
#         str2 = 'defghia'
# Output : 4 
# (i.e. matching characters :- a, d, e, f)

# Input : str1 = 'aabcddekll12@'
#         str2 = 'bb22ll@55k'
# Output : 5 
# (i.e. matching characters :- b, 1, 2, @, k)

def match_char(str1, str2):
  res = []
  for char in str1:
    if char in str2 and char not in res:
      res.append(char)
  print(len(res))
  
match_char('aabcddekll12@', 'bb22ll@55k')

