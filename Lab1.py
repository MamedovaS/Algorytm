class Lab1:
    def find_indexer(self, numbers, target):
        result = {}
        n = len(numbers)

        for i in range(n):
            pair = target - numbers[i]
            for j in range(i + 1, n):
                if numbers[j] == pair:
                    result[0] = i
                    result[1] = j
                    return result

        return -1


if __name__ == "__main__":
    lab1 = Lab1()
    nums1 = [4,2]
    target1 = 6
    result1 = lab1.find_indexer(nums1, target1)
    print("Результат 1: [{}, {}]".format(result1[0], result1[1]))
