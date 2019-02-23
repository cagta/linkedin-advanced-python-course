import itertools

seq = ["1st","2nd","3rd"]

#You can iterate over cycle infinetly
cycle = itertools.cycle(seq)

print(next(cycle),next(cycle),next(cycle),next(cycle))

#You can use counter with givin start point and step
start=100
step=10
count = itertools.count(start,step)

print(next(count),next(count),next(count),next(count))