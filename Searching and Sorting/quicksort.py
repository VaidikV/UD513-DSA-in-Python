def quick_sort(elements):
    length = len(elements)
    if length <=1:
        return elements
    else:
        pivot = elements.pop()

    items_greater = []
    items_lower = []

    for item in elements:
        if item > pivot:
            items_greater.append(item)

        else:
            items_lower.append(item)

    return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)


print(quick_sort([2, 67, 43, 66, 12, 7, 43, 9, 7]))

