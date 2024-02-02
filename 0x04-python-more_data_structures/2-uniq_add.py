#!/usr/bin/python3
def uniq_add(my_list=[]):
    # Use a set to keep track of unique integers
    unique_set = set()

    # Iterate through the elements in the list
    # and add unique integers to the set
    for item in my_list:
        if isinstance(item, int):
            unique_set.add(item)

    # Calculate the sum of unique integers in the set
    sum_of_unique = sum(unique_set)

    return sum_of_unique
