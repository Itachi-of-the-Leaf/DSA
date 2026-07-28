"""
Problem: First line contains main character kirito's level (1st value) and no. of dragons (n) (2nd value)
         Then 'n' number of lines follow, each having the dragon's level (1st value) and levels gained reward (2nd value)
         If Kirito's level > dragon's level then he gets the reward and moves on
         Else he dies
         He can fight dragons in any order
"""

"""
initial_info = list(map(int, input("Enter Kirito's level and number of dragons: ").split()))
print(initial_info)
kirito_strength = initial_info[0]
no_of_dragons = initial_info[1]
print(f"Kirito's strength: {kirito_strength}, Number of dragons: {no_of_dragons}")

#Initialize a dictionary to store dragon's level-reward pairs
dragonDict = {}
for i in range(no_of_dragons):
    dragon_stats = list(map(int, input("Enter dragon's level and reward (space-separated): ").split()))
    dragonDict.update({dragon_stats[0] : dragon_stats[1]})
    #dragonDict = sorted(dragonDict)

#Now that we've stored the values, we need to sort via a sorting algo. Let's go with quicksort

def quickSort(givenArray: list) -> list:
    #Best case, already sorted
    if len(givenArray) <= 1:
        return givenArray

    else: #Divide into groups
        pivot = givenArray[-1]

        left = [x for x in givenArray[:-1] if x <= pivot] #list comprehension; iterate over every element except the last to avoid duplicates
        right = [x for x in givenArray[:-1] if x > pivot]

        #Recursion and combine
        return quickSort(left) + [pivot] + quickSort(right)

#Now we sort the values in dictionary from highest to lowest so that we can decide if Kirito can go ahead with his win

dragonDict = {k: dragonDict[k] for k in quickSort(list(dragonDict.keys()))} #For 'k' in the sorted keys array, put key-value pair in dict

#Now we see if kirito can do it 
isAlive = True
for dragonStrength in dragonDict.keys():

    if kirito_strength > dragonStrength:
        kirito_strength += dragonDict.get(dragonStrength) #The reward value associated with strength

    else:
        isAlive = False

#Final decision logic
print("YES") if (isAlive == True) else print("NO")
"""
#The codeforces version

initial_info = list(map(int, input().split()))

kirito_strength = initial_info[0]
no_of_dragons = initial_info[1]


#Initialize a list to store dragon's level-reward pairs
dragonList = []
for i in range(no_of_dragons):
    dragon_stats = list(map(int, input().split()))
    dragonList.append(dragon_stats)

#Now that we've stored the values, we need to sort via a sorting algo. Let's go with quicksort

def quickSort(givenArray: list) -> list:
    #Best case, already sorted
    if len(givenArray) <= 1:
        return givenArray

    else: #Divide into groups
        pivot = givenArray[-1]

        left = [x for x in givenArray[:-1] if x <= pivot] #list comprehension; iterate over every element except the last to avoid duplicates
        right = [x for x in givenArray[:-1] if x > pivot]

        #Recursion and combine
        return quickSort(left) + [pivot] + quickSort(right)

#Sorting the dragonList
dragonList = quickSort(dragonList)

#Check if Kirito can fight his way through
isAlive = True
for i in range(len(dragonList)):
    if (kirito_strength > dragonList[i][0]):
        kirito_strength += dragonList[i][1]
    else:
        isAlive = False

print("YES") if isAlive == True else print("NO")