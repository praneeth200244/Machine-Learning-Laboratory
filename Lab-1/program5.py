#Python program to convert tuple matrix to tuple list

#Creating tuple matrix
tupleMatrix = ((1,2,3),(4,5,6),(7,8,9),(10,11,12))

#Printing tuple matrix
print("Tuple matrix: ", tupleMatrix)

#Converrting tuple matrix to tuple list
tupleList = [tuple(row) for row in tupleMatrix]
tupleList1 = list(map(tuple, tupleMatrix))

#Printing tuple list
print("Tuple matrix: ", tupleList)
print("Tuple matrix: ", tupleList1)

for item in tupleList :
    print(item)


