# Given the string, the task is to generate the same string using the random combination of special character, numbers, and alphabets.

# Examples :

# Input : GFG
# Output :n4W
#         mK7
#         k1x
#         q;;, !g
#         .
#         .
#         .
#         .
#         .
#         GF,
#         GFf
#         GFp
#         GFG

# Target matched after 167 iterations

import random
import string

def generate_random_string(str):
    str_length = len(str)
    chars = string.ascii_letters + string.digits + string.punctuation + " "
    iterations = 0

    while True:
        iterations += 1
        generated_string = ''.join(random.choice(chars) for _ in range(str_length))
        print(generated_string)

        if generated_string == str:
            break

    return iterations

iterations = generate_random_string("GFG")
print(f"Target matched after {iterations} iterations")
