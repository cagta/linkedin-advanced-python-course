import collections as col

Grades = col.namedtuple("Grade", "Number Letter")

stud1 = Grades(90, "A")
stud2 = Grades(19, "F")

#We can use tuple without index. 
#Remember that tuples are immutable.
if (stud1.Number >= 80):
    stud1 = stud1._replace(Number=100)

print(stud1, stud2)