from collections import Counter

list1 = ["A","B","C","A"]
list2 = ["B","C","C"]

c1 = Counter(list1)
c2 = Counter(list2)

print("There is", sum(c1.values()), " elements in list1")

print("There is", c1["A"], "A element in list1")

c1.update(list2)
print("There is", sum(c1.values()), " element in both list")

print("Most common element in both list is", c1.most_common(1))

c1.subtract(list2)

print("Most common element in list1 is", c1.most_common(1))

print("Most common element in both list is", c1 & c2)

