# concatenating strings using upper, lower and title printing functions
str1 = "pyTHon "
str2 = "proGraMMinG"
int_week = int(input("enter what week"))
str3 = str1 + str2 + " week "+ str(int_week)
upper_str = str3.upper()
lower_str = str3.lower()
title_str = str3.title()
capitalize_str = str3.capitalize()

swapcase_str=str3.swapcase() # swaps the letter's case
print(upper_str)
print(lower_str)
print(title_str)
print(swapcase_str)
