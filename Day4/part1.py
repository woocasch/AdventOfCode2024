with open("input.txt", "r") as file:
    lines = file.read().splitlines()

rows = len(lines)
cols = len(lines[0])

matrix = [[0 for _ in range(cols)] for _ in range(rows)]

for i in range(rows):
    for j in range(cols):
        matrix[i][j] = lines[i][j]

def check_position(row, col):
    global matrix
    global cols
    global rows
    if matrix[row][col] != 'X':
        return 0
    directions = [
        [-1, -1],
        [-1, 0],
        [-1, 1],
        [0, -1],
        [0, 1],
        [1, -1],
        [1, 0],
        [1, 1]
    ]
    characters = ['M', 'A', 'S']
    counter = 0
    for direction in directions:
        position = [row, col]
        is_valid = True
        for character in characters:
            position = [
                position[0] + direction[0],
                position[1] + direction[1]
            ]

            if position[0] < 0 or position[0] >= rows:
                is_valid = False
                break;

            if position[1] < 0 or position[1] >= cols:
                is_valid = False
                break;

            if matrix[position[0]][position[1]] != character:
                is_valid = False
                break;

        if is_valid:
            counter = counter + 1

    return counter

total = 0
for i in range(rows):
    for j in range(cols):
        total += check_position(i, j)

print(total)
