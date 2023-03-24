#Python program to flatten tuple of list to tuple

#Creating a tuple of list
tupleList = ([1,2], [1,2,3], [4,5], [9, 10])
print("Tuple of list: ", tupleList)

#Converting and storing tuple of list to tuple
res = tuple(sum(tupleList,[]))
print("Flatten tuple: ", res)

flattenTuple = tuple(item for sublist in tupleList for item in sublist)
print("Flatten tuple: ", flattenTuple)
