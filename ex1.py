# Python program to check whether the string is Symmetrical or Palindrome

'''Given a string. the task is to check if the string is symmetrical and palindrome or not. 
A string is said to be symmetrical if both the halves of the string are the same and a string is said to be a palindrome string 
if one half of the string is the reverse of the other half or if a string appears same when read forward or backward.

Example: 

Input: khokho
Output: 
The entered string is symmetrical
The entered string is not palindrome

Input:amaama
Output:
The entered string is symmetrical
The entered string is palindrome'''

def check_symmetrical_palindrome(str):
    if str == str[::-1]:
        print("The entered string is symmetrical")
    else:
        print("The entered string is not symmetrical")

    if str == str[::-1]:
        print("The entered string is palindrome")
    else:
        print("The entered string is not palindrome")

check_symmetrical_palindrome("khokho")
check_symmetrical_palindrome("amaama")
  