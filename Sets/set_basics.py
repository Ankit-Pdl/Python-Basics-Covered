
#! collection of data

#! sets are mutable. 

mySet = {
    1,2,3,2,3,5
}
print(mySet)

for x in mySet:
    print(x)

mySet.add(34) 
print(mySet)   


set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)
