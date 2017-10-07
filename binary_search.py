def binary_search(array_num, num_to_find, low_index, high_index):
    #first base case, number not in the list
    if low_index > high_index:
        return False


    #assign middle index... between low and high
    middle = int((low_index + high_index) /2)

    #verify if the value we want to find is in the arr[middle]
    if num_to_find == array_num[middle]:
        return True
    elif num_to_find < array_num[middle]:
        return binary_search(array_num , num_to_find , low_index , middle - 1 )
    else:
        return binary_search(array_num , num_to_find , middle + 1, high_index )


if __name__ == '__main__':
    array_num = [1,2,3,4,6,8,10,12,25,27,28,34,37,49,51,52,53]
    num_to_find = int(input('give me a num: '))
    res = binary_search(array_num, num_to_find, 0, len(array_num) - 1)
    if res is True:
        print('Your number is in the list')
    else:
        print('Your number is NOT in the list')
