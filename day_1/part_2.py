import re

with open('day_1/input.txt', 'r') as file:
    data = file.read()

print(sum([int("".join([m[group] if group in (m:={'one': '1','two': '2','three': '3','four': '4','five': '5','six': '6','seven': '7','eight': '8','nine': '9'}) else group for group in matches[0]])) for line in data.split('\n') if (matches := re.findall(r'(?:(\d|one|two|three|four|five|six|seven|eight|nine).*(\d|one|two|three|four|five|six|seven|eight|nine))|(?:((\d|one|two|three|four|five|six|seven|eight|nine)))', line))]))