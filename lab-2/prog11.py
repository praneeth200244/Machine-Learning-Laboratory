# Python program to convert tuple list to dictionary with key from a given start value

originalList = [(1,2),(3,4),(5,6),(7,8),(9,10),(11,12),(13,14),(14,15),(15,16),(17,18),(19,20),(21,22),(23,24)]
print(f"The original list: {originalList}")

startValue = int(input("Enter the start value: "))

resultantDict = dict()

for item in originalList :
    resultantDict[startValue] = item
    startValue += 1

print(f"Constructed dictionary: {resultantDict}")































































