def sum(list_of_integers):
    if isinstance(list_of_integers, list):
        if list_of_integers[0] < 0:
            raise Exception("Positive integers only.")
        sum_of_integers = list_of_integers[0]
    else:
        raise Exception("Input type 'list' only.")

    return sum_of_integers
