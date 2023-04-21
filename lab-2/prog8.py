# Python program to find indices from other tuple lit

originalList = [(12,25), (52,69), (96,115), (85,58), (94,34)]
print("Original List: " + str(originalList)) 

searchList = [(96,115), (94,34), (45,68), (84,94), (89,98)]
print("Search List: " + str(searchList))

resultantlist = list()

for elementPair in searchList :
    if  elementPair in originalList :
        resultantlist.append(originalList.index(elementPair))

print("The matched tuple indices: " + str(resultantlist))