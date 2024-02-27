import re

with open("day_2/input.txt") as file:
    data = file.readlines()

print(sum(eval("*".join(map(str,(max(map(int, re.findall(r"\d+(?= {0})".format(color), draws)))for color in ["red", "green", "blue"]),))) for _, draws in (line.split(":") for line in data)))