"""
    Anonymous Function implementation of Python
    is Lambda.

    You can define as:
        lambda (params) : (expression)

    PS: You can pass them like an argument.
"""
def Square(num):
    return num*num

numbers = [1,2,3,4,5]

print(list(map(Square, numbers)))

#Lambda makes your code more readable instead of named function.
print(list(map(lambda n: n*n, numbers)))