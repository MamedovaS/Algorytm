def my_search(haystack, needle):
    comparisons = 0

    if not needle:
        return -1, comparisons

    for i in range(len(haystack) - 1, -1, -1):
        comparisons += 1
        if haystack[i:i + len(needle)] == needle:
            return i, comparisons

    return -1, comparisons

haystack = "Lorem ipsum dolor sit amet, consectetur adipiscing elit"
needle = "ipsum"

index, comparisons = my_search(haystack, needle)

if index != -1:
    print(f"Знайдено на позиції {index}, кількість порівнянь: {comparisons}")
else:
    print("Підстрічка не знайдена")
