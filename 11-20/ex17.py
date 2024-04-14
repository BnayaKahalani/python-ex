# Given the string, we have to remove the ith indexed character from the string. 
# In any string, indexing always start from 0. Suppose we have a string geeks then its indexing will be as –

# g e e k s
# 0 1 2 3 4
# Examples :

# Input : Geek
#         i = 1
# Output : Gek

# Input : Peter 
#         i = 4
# Output : Pete

def remove_idx(str, i):
    a = str[:i] 
    b = str[i + 1:] 
    print(a + b) 
    
remove_idx("Geek", 1)