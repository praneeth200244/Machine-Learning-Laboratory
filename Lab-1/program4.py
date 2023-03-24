# Python program to sort tuple list by nth elemnet of tuple

#Creating list of tuples
tupleList = [(4,2,6),(1,5,6),(1,9,5),(1,8,3)]
print("List of tuples: ", tupleList)

#Taking input from the user
n = int(input("Enter the nth element: "))

#Sorting tuple list by nth elemnet of tuple
sortedList = sorted(tupleList, key=lambda x : x[n])

#Printing sorted list
print("Sorted list: ", sortedList)
