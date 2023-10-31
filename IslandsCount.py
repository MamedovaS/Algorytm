def IslandsCount(grid):
    if not grid:
        return 0


    def landCheck(i, j):
        if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == "1":
            grid[i][j] = "0"

            landCheck(i - 1, j)
            landCheck(i + 1, j)
            landCheck(i, j - 1)
            landCheck(i, j + 1)
            landCheck(i - 1, j - 1)
            landCheck(i - 1, j + 1)
            landCheck(i + 1, j - 1)
            landCheck(i + 1, j + 1)

    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "1":
                count += 1
                landCheck(i, j)

    return count

if __name__ == "__main__":
    matrix = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
    print(IslandsCount(matrix))

