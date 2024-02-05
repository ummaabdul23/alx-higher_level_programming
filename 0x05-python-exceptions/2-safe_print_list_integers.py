#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        count = 0
        for i in my_list:
            if count < x:
                if type(i) == int:
                    print("{:d}".format(i), end="")
                    count += 1
            else:
                break
        print()
        return count
    except Exception as e:
        print(f"An error occurred: {e}")
        return 0
