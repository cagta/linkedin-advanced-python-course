"""
    For preventing bad usage we can protect our functions with
    keywords. 

    customFunc can be use without specifying keyword. Which can be dangerous.
    customFuncKeyword can only be use with keyword.
"""
def customFunc(arg1, arg2, keyword=False):
    print("1:", arg1, "2:", arg2, "keyword:", keyword)

def customFuncKeyword(arg1, arg2, *, keyword=False):
    print("1:", arg1, "2:", arg2, "keyword:", keyword)

customFunc(1,2,True)
customFunc(1,2,keyword=True)

customFuncKeyword(1,2,keyword=True)