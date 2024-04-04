# We are given a string and we need to remove all duplicates from it? 
# What will be the output if the order of character matters? Examples:

# Input : geeksforgeeks 
# Output : geksf

def remove_duplicates(str):
  res = []
  for char in str:
    if char in res:
      continue
    else:
      res.append(char)
  print("".join(res))
  
remove_duplicates("geeksforgeeks")