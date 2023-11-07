from collections import deque


def islands_count(matrix):
    if not matrix:
        return 0

    def land_check(i, j):
        if 0 <= i < len(matrix) and 0 <= j < len(matrix[0]) and matrix[i][j] == "1":

            matrix[i][j] = "0"

            land_check(i - 1, j)
            land_check(i + 1, j)
            land_check(i, j - 1)
            land_check(i, j + 1)
            land_check(i - 1, j - 1)
            land_check(i - 1, j + 1)
            land_check(i + 1, j - 1)
            land_check(i + 1, j + 1)

    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == "1":
                count += 1
                land_check(i, j)

    return count


if __name__ == "__main__":
    matrix = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
    print(islands_count(matrix))

# def land_check(i, j):
#     queue = deque()
#     queue.append((i, j))
#     while queue:
#         x, y = queue.popleft()
#         if 0 <= x < len(matrix) and 0 <= y < len(matrix[0]) and matrix[x][y] == "1":
#             matrix[x][y] = "0"
#
#             directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
#             for dx, dy in directions:
#                 nx, ny = x + dx, y + dy
#                 queue.append((nx, ny))
#
# flattened_matrix = [(i, j) for i in range(len(matrix)) for j in range(len(matrix[0])) if matrix[i][j] == "1"]
