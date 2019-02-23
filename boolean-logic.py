"""
    False:
        False or None
        Numeric Zero
        Empty Sequences/Collections ", (), [], {}"
        Empty set() & range(0)
        Custom Object that overrides bool & length
"""
class myClass:
    def __bool__(self):
        return False

    def __len__(self):
        return 0

customObj = myClass()

print(bool(customObj))
print(len(customObj))