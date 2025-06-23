grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print("Original grid:")
for row in grid:
    print(row)

for row_index in range(len(grid)):
    for col_index in range(len(grid[row_index])):
        number = grid[row_index][col_index]
        
        if number % 2 == 0:
            grid[row_index][col_index] *= 2
        else:
            grid[row_index][col_index] = 0

print("\nModified grid:")
for row in grid:    
    print(row)
