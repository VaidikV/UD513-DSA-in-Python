
def bubble_sort(elements):
    size = len(elements)

    for i in range(size-1):
        swapped = False
        for j in range(size-1-i):
            if elements[j] > elements[j+1]:
                tmp = elements[j]
                elements[j] = elements[j+1]
                elements[j+1] = tmp
                swapped = True
        if not swapped:
            break


if __name__ == '__main__':
    list_of_elements = [5, 9, 2, 1, 67, 34, 88, 34]
    list_of_elements1 = ["Rick", "Walter", "Morty", "Tom", "Bojack"]
    bubble_sort(list_of_elements1)
    print(list_of_elements1)
