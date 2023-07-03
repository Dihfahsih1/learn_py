def binary_search(list, element):
    middle = 0
    start = 0
    end = len(list)
    steps = 0

    while(start<=end):
        print("Step", steps, ":", str(list[start:end+1]))

        steps = steps +1
        middle = (start + end) // 2

        if element == list[middle]:
            return middle
        if element < list[middle]:
            end = middle -1
        else:
            start = middle + 1
    return -1

elements = input("Enter list of numbers to be searched, separated by a comma: ")
my_list = [int(num) for num in elements.split(',')]

target = int(input("Enter the target number from the list: "))

result = binary_search(my_list, target)
print("Target found at index:", result)

binary_search(my_list, target)