"""
Problem: First line contains main character kirito's level (1st value) and no. of dragons (n) (2nd value)
         Then 'n' number of lines follow, each having the dragon's level (1st value) and levels gained reward (2nd value)
         If Kirito's level > dragon's level then he gets the reward and moves on
         Else he dies
         He can fight dragons in any order
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

print(dragonDict)