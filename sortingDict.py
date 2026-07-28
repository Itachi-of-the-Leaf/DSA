givenDict = {5: 7, 6: 67, 2: 76, 6: 100}

def quickSort(array):
    if len(array) <= 1:
        return array
    else:
        pivot = array[-1]

        left = [x for x in array[:-1] if x < pivot]
        right = [x for x in array[:-1] if x > pivot]

        return quickSort(left) + [pivot] + quickSort(right)

print(quickSort(list(givenDict.keys())))
givenDict = {str(k): givenDict[k] for k in quickSort(list(givenDict.keys()))}
print(givenDict)