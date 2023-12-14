def create_sets_for_tribes(tribes_data):
    sets_for_tribes = {}

    for tribe in tribes_data:
        current_set = set(tribe)
        sets_for_tribes[tuple(tribe)] = current_set

    return sets_for_tribes


def sex(main_set):
    even_subset = {item for item in main_set if item % 2 == 0}
    odd_subset = {item for item in main_set if item % 2 != 0}

    return even_subset, odd_subset


def count_possible_pairs(N, pairs):
    # Створюємо словник для збереження племен і їх членів
    tribes_sets = create_sets_for_tribes(pairs)

    # Список для зберігання пар
    pairs_list = []

    while True:
        # Ініціалізуємо лічильник можливих пар
        count = 0

        # Тимчасовий список для зберігання нових пар
        temp_pairs_list = []

        # Обчислюємо кількість та пари
        for i in range(1, N, 2):  # Перевіряємо пари хлопців/дівчат
            for j in range(0, N, 2):
                if i != j:
                    pair_key1 = tuple(pairs[i])
                    pair_key2 = tuple(pairs[j])

                    if pair_key1 in tribes_sets and pair_key2 in tribes_sets:
                        set1 = tribes_sets[pair_key1]
                        set2 = tribes_sets[pair_key2]

                        if list(sex(set1))[0] and list(sex(set2))[1]:
                            count += 1
                            temp_pairs_list.append((pairs[i][0], pairs[j][0]))

        # Якщо жодна пара не відповідає умовам, виходимо з циклу
        if count == 0:
            break

        # Додаємо нові пари до загального списку
        pairs_list.extend(temp_pairs_list)

        # Оновлюємо дані племен
        keys_to_delete = []
        for pair in temp_pairs_list:
            for key, value in tribes_sets.items():
                if pair[0] in value or pair[1] in value:
                    keys_to_delete.append(key)

        for key in keys_to_delete:
            if key in tribes_sets:
                del tribes_sets[key]

    # Виводимо кількість та пари
    print(len(pairs_list))
    for pair in pairs_list:
        print(f"{pair[0]}/{pair[1]}")

    return count


# Зчитуємо вхідні дані
N = int(input("Enter the number of pairs: "))
pairs = [list(map(int, input("Enter a pair of numbers separated by space: ").split(" "))) for _ in range(N)]

# Обчислення та вивід результату
result = count_possible_pairs(N, pairs)
print(result)
