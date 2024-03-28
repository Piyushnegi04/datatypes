# #string data type is used to stode the text info.
# x = "avi"
# print(x)
# # to check datatype of any variable type(variable name)
# print(type(x))

# #numerical datatype
# #int
# y=30
# print(y)
# print(type(y))

# #flot
# z=11.34
# print(z)
# print(type(z))

# #complex no.
# a=34j
# print(a)
# print(type(a))

# #dataset in sequence
# #list- ordered and changeable, can have elements of different types
# d = ["avi","is","awesome",1,2,3]
# print(type(d))

# #range
# r = range(5)
# print(type(r))

# #tuple - immutable ,ordered and can't be changed 
# t = ('Avi', 'Is','Awesome')
# print(type(t))

# #dictionary- stored in keyvalue pair or key reference
# b = {"avi":"avi","email":"avi2004@gmail.com"}   
# print(type(b))

# #set- also store multiple  values but unordered, unchangeble, no duplicate value
# s = {'avi','is','awesome'}
# print(type(s))

# #boolean dataset - True/False
# f = False
# g = True
# print(type(f), type(g))

#bytes, bytearray, memory view
# l =  b"Hello World"  
# print(type(l))

# p=bytearray(b"Hello world")
# print(type(p))

# m=memoryview(b"Hello world")
# print(type(m))
# print(m[0])

# d = [1,2,3]
# print(type(d))

# # f = bytes(d)
# # f[1] =7
# f = bytearray(d)
# f[1] =7
# for i in f:
#     print(i)

#none dt
n = None
print(type(n))