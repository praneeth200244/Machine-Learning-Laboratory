# Python program to convert dictionary values list to dictionary list 

originalList = [
    {'Udupi' : ['K', 'A', 2, 0]},
    {'Mangaluru' : ['K', 'A', 1, 9]},
    {'Puttur' : ['K', 'A', 2, 1]},
    {'Bhatkal' : ['K', 'A', 4, 7]},
] 

print("The original list: " + str(originalList))

resultantList = list({} for index in range(len(originalList)))

index = 0

for keyValuePair in originalList :
    for key,value in keyValuePair.items():
        for element in value :
            resultantList[index][key] = element
            index += 1
        index = 0
print("Records after conversion: " + str(resultantList))
print("\nRecords after conversion:")
for item in resultantList:
    print(item)