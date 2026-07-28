def quickSort(array: list) -> list:
    #Best case
    if len(array) <= 1:
        return array

    else: #Split into two groups
        pivot = array[-1] #Select last element

        left = [x for x in array[:-1] if x <= pivot] #left is a list containing all elements in array (except the last one which we chose as pivot) which are less than the pivot
        right = [x for x in array[:-1] if x > pivot] #right is.. same as left but only contains elements greater than the pivot

        # Repeat for both sides and combine with pivot

        return quickSort(left) + [pivot] + quickSort(right) #[pivot] not pivot because pivot is an integer and [pivot is a list]

myArr = [6, 7, 87, 78, 67, 76]
sortedArray = quickSort(myArr)

print(sortedArray)