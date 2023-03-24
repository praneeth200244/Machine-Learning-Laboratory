# Python program to convertset to tuple and tuple to set

#Creating a set
s = {1,2,3,4,5,6,7,8,9,0}
#s = {'a','b','c','d'}
print(s)
print(type(s),"  ",s)

#Converting ad storing set as a tuple
t=tuple(s)
print(t)
print(type(t),"  ",t)

#Converting ad storing tuple as set
s=tuple(t)
print(s)
print(type(s),"  ",s)
