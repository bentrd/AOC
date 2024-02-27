import re

with open("day_2/input.txt") as file:
    data = file.readlines()

print(sum(int(line.split(":")[0].split(" ")[1]) for line in data if all(int(n) <= max for color, max in {"red": 12, "green": 13, "blue": 14}.items() if (match := re.findall(r"(\d+)(?= {0})".format(color),line.split(":")[1])) for n in match)))
