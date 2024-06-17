# Advanced Text Processing with Python Regex
import re

text = "Name: John Doe; Age: 30; Occupation: Engineer; Location: New York"
# Extract the Occupation from the text
# Your code here
str_split_res = re.split(";", text)
for i in str_split_res:
    ind_res = re.split(":", i)
    print(f"{ind_res[-1]}")