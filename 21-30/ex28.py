# Given String list, perform sort operation on basis of frequency of particular character.

# Input : test_list = [“geekforgeekss”, “is”, “bessst”, “for”, “geeks”], K = ‘s’ 
# Output : [‘bessst’, ‘geekforgeekss’, ‘geeks’, ‘is’, ‘for’] 
# Explanation : bessst has 3 occurrence, geeksforgeekss has 3, and so on.

# Input : test_list = [“geekforgeekss”, “is”, “bessst”], K = ‘e’ 
# Output : [“geekforgeekss”, “bessst”, “is”] 
# Explanation : Ordered decreasing order of ‘e’ count. 

def sort_freq(test_list):
 
  print("The original list is : " + str(test_list))
  K = 'e'
  res = sorted(test_list, key = lambda ele: -ele.count(K))
  print("Sorted String : " + str(res))
  
sort_freq(["geekforgeeks", "is", "best", "for", "geeks"])