from itertools import combinations
from collections import defaultdict

from itertools import combinations

def find_combinations(tribes):
    all_combinations = set()

    for i in range(len(tribes)):
        for j in range(i + 1, len(tribes)):
            tribe1 = tribes[i]
            tribe2 = tribes[j]

            # Finding all possible combinations of two numbers from different tribes
            tribe_combinations = combinations(tribe1, 1)  # Picking the first member from tribe1

            for member1 in tribe_combinations:
                for member2 in tribe2:
                    all_combinations.add((member1[0], member2))
                    all_combinations.add((member2, member1[0]))

    return all_combinations

def generate_odd_even_pairs(combinations_set):
    odd_even_pairs = set()

    for combination in combinations_set:
        for pair in combinations(combination, 2):
            if pair[0] % 2 != pair[1] % 2:
                odd_even_pairs.add(pair)

    return odd_even_pairs

def form_tribes(data):
    connections = defaultdict(list)

    lines = data.split("\n")

    for line in lines:
        if line:
            person1, person2 = map(int, line.split())
            connections[person1].append(person2)
            connections[person2].append(person1)

    visited = set()
    tribes = []

    for start_person in connections:
        if start_person not in visited:
            tribe = set()
            stack = [start_person]

            while stack:
                current = stack.pop()
                if current not in visited:
                    visited.add(current)
                    tribe.add(current)
                    stack.extend(connections[current])

            tribes.append(tribe)

    return tribes

if __name__ == "__main__":
    data_input = """1 2
                    2 4
                    3 5"""

    result = form_tribes(data_input)

    combinations_result = find_combinations(result)
    for combination in combinations_result:
        print(combination)

    valid_pairs_result = generate_odd_even_pairs(combinations_result)
    print("\nValid Pairs (One even, one odd):")
    for valid_pair in valid_pairs_result:
        print(valid_pair)
