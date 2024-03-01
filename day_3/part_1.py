with open('/day_3/input.txt') as f:
    data = f.read()

class Number:
    def __init__(self, value):
        self.value = value
        self.neighbors = {
            'up': None,
            'down': None,
            'left': None,
            'right': None,
            'up_left': None,
            'up_right': None,
            'down_left': None,
            'down_right': None
        }
        self.neighbors_count = 0


def get_neighbors(x, y, grid):
    neighbors = {
        'up': None,
        'down': None,
        'left': None,
        'right': None,
        'up_left': None,
        'up_right': None,
        'down_left': None,
        'down_right': None
    }
    if x - 1 >= 0:
        neighbors['left'] = grid[y][x - 1]
    if x + 1 < len(grid[y]):
        neighbors['right'] = grid[y][x + 1]
    if y - 1 >= 0:
        neighbors['up'] = grid[y - 1][x]
    if y + 1 < len(grid):
        neighbors['down'] = grid[y + 1][x]
    if x - 1 >= 0 and y - 1 >= 0:
        neighbors['up_left'] = grid[y - 1][x - 1]
    if x + 1 < len(grid[y]) and y - 1 >= 0:
        neighbors['up_right'] = grid[y - 1][x + 1]
    if x - 1 >= 0 and y + 1 < len(grid):
        neighbors['down_left'] = grid[y + 1][x - 1]
    if x + 1 < len(grid[y]) and y + 1 < len(grid):
        neighbors['down_right'] = grid[y + 1][x + 1]
    return neighbors


def get_numbers(data):
    grid = []
    for line in data.split('\n'):
        row = []
        for char in line:
            row.append(char)
        grid.append(row)
    for y, row in enumerate(grid):
        for x, number in enumerate(row):
            number.neighbors = get_neighbors(x, y, grid)

    return grid


if __name__ == '__main__':
    grid = get_numbers(data)
    for row in grid:
        for number in row:
            print(number)