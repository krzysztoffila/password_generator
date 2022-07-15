from operator import length_hint
import random

lower_case = "abcdefghijklmnoprstwuxyz"
upper_case = "ABCDEFGHIJKLMNOPRSTUWXYZ"
number = "0123456789"
symbol = "!@#$%^&*(){}:?',./;'[]"

Use_for = lower_case + upper_case + number + symbol
length_for_password = 8

password = "".join(random.sample(Use_for, length_for_password))

print("Your Generated password is: ")

