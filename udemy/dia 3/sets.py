mi_set = set([1, 2, 3, 4, 5])
print(type(mi_set))
print(mi_set)

otro_set = {1, 2, 3, 4, 5}
print(type(otro_set))
print(otro_set)

nuevo_set = {1, 2, 3, 4, 5, 6, 5, 4, 3, 4, 5, 6, 7, 5, 4, 3, 2, 1}
print(nuevo_set)

set_tuple = {1, 2, 3, (9, 9, 9), 4, 5}
print(set_tuple)
print(len(set_tuple))
print(2 in set_tuple)

s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8}
s3 = s1.union(s2)
print(s3)
s1.add(0)
s1.add(2)
print(s1)
s1.remove(3)
print(s1)
s1.discard(2)
print(s1)
s1.discard(432)
s1.pop()
print(s1)
s1.clear()
print(s1)
