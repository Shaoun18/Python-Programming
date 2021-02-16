matrix = [
    [1,2,3],
    [5,6,7],
]

for row in matrix:
    for col in row:
        print(col)

matrix[0][2] = 10
print(matrix[0][2])