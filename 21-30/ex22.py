# Given a string S, containing numeric words, the task is to convert the given string to the actual number.

# Example: 

# Input: S = “zero four zero one”
# Output: 0401

# Input: S = “four zero one four”
# Output: 4014

def convert_to_num(s):
    nums = {
        "zero": "0", "one": "1", "two": "2", "three": "3", "four": "4",
        "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"
    }
    return "".join([nums[word] for word in s.split()])

input_str = "zero four zero one"
print(convert_to_num(input_str)) 

