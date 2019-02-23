"""
    Best practices of DocStrings:
        First line should be summary.
        If the document is written for
            MODULE:
                List important classes, functions, exceptions
            CLASSES:
                List important methods
            FUNCTIONS:
                List and explain each param, exceptions and return,
                one per line.
"""
def customFunctions(arg1, arg2=None):
    """This is an example function for docstrings.

    arg1 = Example Argument
    arg2 = Example Argument with default value.
    """
    print(arg1, arg2)

print(customFunctions.__doc__)