def sum(list_of_integers):
    # Check if input is a list only
    if isinstance(list_of_integers, list):
        sum_of_integers = 0

        # Check if list has items
        if len(list_of_integers) <= 0:
            raise Exception("List cannot be empty.")
        
        # Iterate through the list of integers
        for integer_item in list_of_integers:
            print("integer: ",integer_item)

            # Check if list items are positive integers
            if not isinstance(integer_item, int) or integer_item < 0:
                raise Exception("Positive integers only.")

            # Build the sum
            sum_of_integers += integer_item
    
    else:
        raise Exception("Input type 'list' only.")

    return sum_of_integers
