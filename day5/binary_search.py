def integer_binary_search(lst, element):
    if not lst:
        print("Empty list. Nothing to search.")
        return -1
    middle = 0
    start = 0
    end = len(lst)
    steps = 0

    while (start <= end):
        print("Step", steps, ":", str(lst[start : end + 1]))

        steps = steps + 1
        middle = (end + start) // 2

        if element == lst[middle]:
            return middle
        if element < lst[middle]:
            end = middle - 1
        else:
            start = middle + 1

    return -1
