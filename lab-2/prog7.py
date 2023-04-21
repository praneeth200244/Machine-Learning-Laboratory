#Python program to merge tuple list by overlapping mid tuple

list1 = [(14,28), (9,2), (2,304), (951,980)]
list2 = [(10,252), (23,246), (154,20), (582,568)]

print("The original list-1 is: " + str(list1))
print("The original list-2 is: " + str(list2))

index = 0
j = 0
result = list()

while (j < len(list1)) :
    if ((list2[j][0] > list1[index][0]) and (list2[j][1] < list1[index+1][1])) :
        result.append((list1[index],list2[j],list1[index+1]))
        j += 1
        index = 0
    else :
        index += 1
    if (index == (len(list1)-1)) :
        index = 0
        j += 1

print("Merged tuples: " + str(result))



