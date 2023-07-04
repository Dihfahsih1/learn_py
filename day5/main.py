from input_validation import validate_input_list
from binary_search import integer_binary_search

def main():
    elements = input("Enter a list of integers to be searched, separated by a comma: ")
    try:
        my_list = [int(num) for num in elements.split(',')]
        my_new = [pow(n,2) for n in my_list]
        print("New listy: ", my_new)
    except ValueError:
        print("Invalid input. The list must contain only integers.")
        return

    target = int(input("Enter the target number from the list: "))
    try:
        validate_input_list(my_list)
        result = integer_binary_search(my_list,target)
        if result != -1:
            print("Target found at index:", result)
        else:
            print("Target not found in the list.")
    except ValueError as e:
        print(str(e))

if __name__ == '__main__':
    main()