def list_division(my_list_1, my_list_2, list_length):
    result_list = []

    try:
        for i in range(list_length):
            try:
                element_1 = my_list_1[i] if i < len(my_list_1) else 0
                element_2 = my_list_2[i] if i < len(my_list_2) else 0
                result = element_1 / element_2
            except ZeroDivisionError:
                print("division by 0")
                result = 0
            except (ValueError, TypeError):
                print("wrong type")
                result = 0
            except IndexError:
                print("out of range")
                result = 0
            finally:
                result_list.append(result)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    return result_list

