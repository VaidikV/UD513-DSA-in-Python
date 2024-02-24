def binary_search(sorted_list, value):
    left = 0
    right = len(sorted_list) + 1
    while left <= right:
        midpoint = ((left + right) // 2) - 1
        current_item = sorted_list[midpoint]
        if current_item == value:
            return midpoint
        elif value < current_item:
            right = midpoint - 1
        else:
            left = midpoint + 1
    return - 1


test_list = [1, 3, 9, 11, 15, 19, 29, 32, 45]
test_val1 = 45
test_val2 = 15

print(binary_search(test_list, test_val2))
