# Given two strings s1 and s2. The task is to find out the minimum number of string rotations for the given string s1 to obtain the actual string s2. 
# Examples:

# Input : eeksg, geeks
# Output: 1 
# Explanation: g is rotated left to obtain geeks.

# Input : eksge, geeks
# Output: 2
# Explanation : e and g are left rotated to obtain geeks.

def findRotations(str1, str2):
    x = 0
    y = 0
    m = str1
     
    while True:
      m = m[len(m)-1] + m[:len(m)-1] 
        
      if(m == str2):
          x += 1
          break
            
      else:
          x += 1
          if x > len(str2) :
              break

    while True:
         
      str1 = str1[1:len(str1)]+str1[0] 
        
      if(str1 == str2):
          y += 1
          break
            
      else:
          y += 1
          if y > len(str2):
              break
                
    if x < len(str2):     
        print(min(x,y))      
    else:
        print("given strings are not of same kind")
         
findRotations("eksge", "geeks")