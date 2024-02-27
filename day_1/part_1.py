import re

with open('day_1/input.txt', 'r') as file:
    data = file.read()

print(sum(int(''.join(group)) for line in data.split('\n') if (matches := re.findall(r'^\D*(?:(\d).*(\d))|(?:((\d)))\D*$', line)) for group in matches if any(group)))