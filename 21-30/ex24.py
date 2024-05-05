# Given a string “str” and another string “sub_str”. We are allowed to delete “sub_str” from “str” any number of times. 
# It is also given that the “sub_str” appears only once at a time. 
# The task is to find if “str” can become empty by removing “sub_str” again and again. Examples:

# Input  : str = "GEEGEEKSKS", sub_str = "GEEKS"
# Output : Yes
# Explanation : In the string GEEGEEKSKS, we can first 
#               delete the substring GEEKS from position 4.
#               The new string now becomes GEEKS. We can 
#               again delete sub-string GEEKS from position 1. 
#               Now the string becomes empty.


# Input  : str = "GEEGEEKSSGEK", sub_str = "GEEKS"
# Output : No
# Explanation : In the string it is not possible to make the
#               string empty in any possible manner.

def checkEmpty(str, pattern):
	
	if len(str)== 0 and len(pattern)== 0:
		return 'true'

	if len(pattern)== 0:
		return 'false'

	while (len(str) != 0):

		index = str.find(pattern)

		if (index ==(-1)):
			return 'false'

		str = str[0:index] + str[index + len(pattern):]		 
	return 'true'

str ='GEEGEEKSKS'
pattern ='GEEKS'
print(checkEmpty(str, pattern))
