class Lab1:
    def find_indexer(self, numbers, target):
        result = []
        n = len(numbers)

        for i in range(n):
            pair = target - numbers[i]
            for j in range(i + 1, n):
                if numbers[j] == pair:
                    result.append([i,j])

        if len(result) == 0:
            return -1
        return result


if __name__ == "__main__":
    lab1 = Lab1()
    nums1 = [4, 2, 3, 3, 5, 1]
    target1 = 6
    result1 = lab1.find_indexer(nums1, target1)
    print(result1)
