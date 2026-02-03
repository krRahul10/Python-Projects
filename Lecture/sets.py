# no duplicates values store

# set is the collection of the unordered items each element in the set must be unique and immutable
# but set is mutable not element mean item change nhi hoga add or delete hojyega 

collections = {1,2,3,4,6,2,45,3,"hello", "world", "hello"}

print(collections)
print(len(collections))

collections.add("8")
print(collections)
print(collections.clear(
))