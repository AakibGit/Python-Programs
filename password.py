import string
import random

s = list(string.ascii_lowercase)
s1 = list(string.ascii_uppercase)
s2 = list(string.digits)
s3 = list(string.punctuation)

pass_word = []

pass_word.extend(s)
pass_word.extend(s1)
pass_word.extend(s2)
pass_word.extend(s3)

random.shuffle(pass_word)

user = int(input("Enter the length of the password you want:\n"))
print("".join(pass_word[0:user]))
