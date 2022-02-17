
# This function determines if the complements of the given value is in the array
# It returns True if it is found, otherwise, it returns False.
def is_complement_existing(list_integers, value_to_find):

    my_list = list(list_integers).copy()
    complements = {}

    for i in range(0, len(my_list)):

        difference = value_to_find - my_list[i]
        comp_sum = difference + my_list[i]

        if difference in complements and comp_sum == value_to_find:
            return True

        # if the above condition is not true, then we keep adding the value to dictionary
        complements[my_list[i]] = my_list[i]

    return False

input_list = [1, 2, 3, 4, 12, -1]

# Test Cases
# print(is_complement_existing(input_list, 6))
# print(is_complement_existing(input_list, 12))
# print(is_complement_existing(input_list, 5))
# print(is_complement_existing(input_list, 7))
# print(is_complement_existing(input_list, 3))
# print(is_complement_existing(input_list, 4))
# print(is_complement_existing(input_list, 34))
# print(is_complement_existing(input_list, 0))
# print(is_complement_existing(input_list, 11))

print(get_complements(input_list, 6))
print(get_complements(input_list, 5))
