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
    if matrix[row][col] != 'A':
        return 0
    diagonals = [
        [[-1, -1], [1, 1]],
        [[1, -1], [-1, 1]]
    ]
    characters = ['M', 'S']
    position = [row, col]
    is_valid = True
    for diagonal in diagonals:
        for offset in diagonal:
            if position[0] + offset[0] < 0 or position[0] + offset[0] >= rows:
                is_valid = False

            if position[1] + offset[1] < 0 or position[1] + offset[1] >= cols:
                is_valid = False

        if not is_valid:
            break

        first_point = [position[0] + diagonal[0][0], position[1] + diagonal[0][1]]
        if not matrix[first_point[0]][first_point[1]] in characters:
            is_valid = False
            break

        first_character = characters.index(matrix[first_point[0]][first_point[1]])
        second_character = characters[1 - first_character]
        second_point = [position[0] + diagonal[1][0], position[1] + diagonal[1][1]]
        if matrix[second_point[0]][second_point[1]] != second_character:
            is_valid = False
            break

    if not is_valid:
        return 0

    if is_valid:
        return 1

    return counter

total = 0
for i in range(rows):
    for j in range(cols):
        total += check_position(i, j)

print(total)
