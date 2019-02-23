teamA = ["PG_A","SG_A","SF_A","PF_A","C_A"]
teamB = ["PG_B","SG_B","SF_B","PF_B","C_B"]

i = iter(teamA)

print(next(i))
print(next(i))
print(next(i))

"""
    We can use primitives for iterating over
    sequences. But enumerate will make your code
    more readable compared to classical way.
"""
for i in range(len(teamA)):
    print(i+1, teamA[i])

for i,j in enumerate(teamA, start=1):
    print(i,j)


"""
    Combining Sequences

    zip can be very usefull depending on your use
    case. If you want to use it please remember to upper
    note for writing more readable code.
"""
for i in zip(teamA,teamB):
    print(i)

for i, j in enumerate(zip(teamA,teamB), start=1):
    print(i,j[0],"=",j[1])
