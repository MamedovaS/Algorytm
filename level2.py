def count_pairs(N, pairs):
    count = 0
    for i in range(N):
        for j in range(i + 1, N):
            if pairs[i][0] != pairs[j][0] and pairs[i][0] != pairs[j][1] and pairs[i][1] != pairs[j][0] and pairs[i][
                1] != pairs[j][1]:
                count += 1
    return count


N = int(input())
pairs = []

for _ in range(N):
    pair = list(map(int, input().split()))
    pairs.append(pair)

result = count_pairs(N, pairs)
print(result)
