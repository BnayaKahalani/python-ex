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

string = 'khokho'
half = int(len(string) / 2)
 
 
first_str = string[:half]
second_str = string[half:]
 
 
if first_str == second_str:
    print(string, 'string is symmetrical')
else:
    print(string, 'string is not symmetrical')
 

if first_str == second_str[::-1]: 
    print(string, 'string is palindrome')
else:
    print(string, 'string is not palindrome')
  