a={10,20,'students','raj',40}
#cant access using index
print(a)
print(id(a))
print("------------------------")
#duplicates are avoided
b={10,20,'students','raj',40,10,10}
print(b)
print("---------------------------")
#adding one element
print("adding one element:")
a.add('python')
print(a)
print(id(a))
print("------------------------------")
#adding multiple elements
print("adding multiple element:")
a.update([101,102,103])
print(a)
print(id(a))
print()