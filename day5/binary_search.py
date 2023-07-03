def binary_search(lst, element):
    if not isinstance(lst, list):
        print("Invalid input: the list must be provided.")
        return -1

    if not lst:
        print("Empty list. Nothing to search.")
        return -1
    
    if not isinstance(element, int):
        print("Invalid input: the target must be an integer.")
        return -1
    
    start = 0
    end = len(lst) - 1
    steps = 0

    while start <= end:
        print("Step", steps, ":", str(lst[start:end+1]))

        steps += 1
        middle = (start + end) // 2

        if element == lst[middle]:
            return middle
        if element < lst[middle]:
            end = middle - 1
        else:
            start = middle + 1
    
    print("Target not found in the list.")
    return -1

elements = input("Enter list of numbers to be searched, separated by a comma: ")
my_list = [int(num) for num in elements.split(',')]

if not my_list:
    print("Empty list. Nothing to search.")
else:
    target = int(input("Enter the target number from the list: "))

    result = binary_search(my_list, target)

    if result != -1:
        print("Target found at index:", result)
