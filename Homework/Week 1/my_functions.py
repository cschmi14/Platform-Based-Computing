# Carter Schmidt

def find_maximum(list_param):
    '''
    Takes a list parameter and returns the maximum value in the list
    '''
    max_value = list_param[0]
    for x in list_param:
        if x > max_value:
            max_value = x
    return max_value


print("Max Value in List:", find_maximum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 11, 2, 1]))
print("Max Value in List:", find_maximum([1123, 432, 3145, 2431, 12431, 4532, 543, 2345, 12432, 234]))
print("Max Value in List:", find_maximum([4, 5, 3, 2, 1]))


def reverse(list_param):
    '''
    Returns the reversed version of the list passed into the function
    '''
    reversed_list = []
    for i in range(len(list_param)):
        reversed_list.append(list_param[len(list_param) - (i + 1)])
    return reversed_list


print("Reversed List:", reverse([1, 2, 3, 4, 5]))
print("Reversed List:", reverse([10, 20]))
print("Reversed List:", reverse([123, 234, 345, 1, 2, 3, 432, 321, 543, 43, 23, 3]))


