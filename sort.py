def sort(numbers):
    for i in range(len(numbers) - 1):
        for j in range(len(numbers) - 1):
            if numbers[j] > numbers[j + 1]:
                tmp = numbers[j]
                numbers[j] = numbers[j + 1]
                numbers[j + 1] = tmp
    return numbers

