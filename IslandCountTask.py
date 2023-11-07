def matrix_to_list(matrix):
    def is_valid(x, y):
        return 0 <= x < len(matrix) and 0 <= y < len(matrix[0])

    where_to_look = [(1, 0), (0, 1), (1, 1), (-1, 1), (-1, -1), (1, -1), (0, -1), (-1, 0)]
    adjacency_list = {}

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 1:
                adjacency_list[(i, j)] = [(i + dx, j + dy) for dx, dy in where_to_look
                                          if is_valid(i + dx, j + dy) and matrix[i + dx][j + dy] == 1]

    return adjacency_list


def land_check(matrix):
    def bfs(node):
        queue = [node]
        visited.add(node)

        while queue:
            current_node = queue.pop(0)
            for neighbor in adjacency_list[current_node]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)

    if not matrix:
        return 0

    adjacency_list = matrix_to_list(matrix)
    visited = set()
    count = 0

    for node in adjacency_list.keys():
        if node not in visited:
            bfs(node)
            count += 1

    return count


def read_matrix_from_stream(file_stream):
    matrix = []
    for line in file_stream:
        matrix.append(list(map(int, line.strip().split())))

    return matrix


def write_result_to_stream(result, file_stream):
    file_stream.write(str(result))


input_file_path = './result/input_matrix.txt'
output_file_path = './result/output_result.txt'


with open(input_file_path, 'r') as input_file:
    graph = read_matrix_from_stream(input_file)

result = land_check(graph)


with open(output_file_path, 'w') as output_file:
    write_result_to_stream(result, output_file)

print("Matrix read from file:", graph)
print("Result written to output file:", result)
