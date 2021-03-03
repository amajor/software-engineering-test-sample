def sum(list_of_integers):
    # Check if input is a list only
    if isinstance(list_of_integers, list):

        # Check if list has items
        if len(list_of_integers) <= 0:
            raise Exception("List cannot be empty.")
        
        # Check if list items are positive integers
        if list_of_integers[0] < 0:
            raise Exception("Positive integers only.")

        # Build the sum
        sum_of_integers = list_of_integers[0]
    
    else:
        raise Exception("Input type 'list' only.")

    return sum_of_integers
