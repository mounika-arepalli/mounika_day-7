a={'rahul','raj','sonam','rani'}
b={'sumit','rahul','rani','python','java'}
print("A:",a)
print("B:",b)
print()
#insertion() method
ism=a.intersection(b)
print("intersection:",ism)
print("--------------------------------------")
#union() method
um=a.union(b)
print("union:",um)
print("---------------------------------------")
#difference method
dm=a.difference(b)
print("difference:",dm)
print("-------------------------------------------")
#issubset() method
isub=a.issubset(b)
print("issubset:",isub)
print("--------------------------------------------")
#issupresent() method
isup=a.issuperset(b)
print("issuperset:",isup)
print()