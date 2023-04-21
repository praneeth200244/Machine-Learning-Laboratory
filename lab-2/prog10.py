# Python program to categorize tuple values into dictionay values list

originalList = [(12,25), (15,69), (12,115), (16,58), (15,34), (16,32), (16,45)]
print("Original list: " + str(originalList))

referenceValue = list()

for item in originalList :
    if item[0] not in referenceValue :
        referenceValue.append(item[0])

dictValuesList = dict()

for item in referenceValue :
    matchedValues = list()
    for values in originalList :
        if (values[0] == item) :
            matchedValues.append(values[1])

        dictValuesList[item] = matchedValues

print("The dictionary converted from tuple list: " + str(dictValuesList))