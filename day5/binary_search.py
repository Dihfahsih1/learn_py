def binary_search(lst, element):
    middle = 0
    start = 0
    end = len(lst)
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
    
    return -1

elements = input("Enter list of numbers to be searched, separated by a comma: ")

# Validate the input list
try:
    my_list = [int(num) for num in elements.split(',')]
except ValueError:
    print("Invalid input format. Please provide a comma-separated list of integers.")
    exit()

target_input = input("Enter the target number from the list: ")

# Validate the target number
try:
    target = int(target_input)
except ValueError:
    print("Invalid target number. Please enter an integer.")
    exit()

result = binary_search(my_list, target)
print("Target found at index:", result)
