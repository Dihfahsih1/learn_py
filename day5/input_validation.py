def validate_input_list(lst):
    if not isinstance(lst, list):
        raise ValueError("Invalid input. The list must be provided.")
    
    if not lst:
        raise ValueError("Empty list. Nothing to search.")