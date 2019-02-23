"""
    This is the most primitive way to
    perform file I/O with Python.

    We need to be sure that even if there
    is an error, we should close the file.
"""
handler = open("sample.txt", "r")

for line in handler:
    if 'consequat' in line.lower():
        print(line, end='')

handler.close()

"""
    If we use with, even if there is a
    raised exception we can be sure
    that file will be closed.
"""
with open("sample.txt", "r") as handler:
    for line in handler:
        if 'consequat' in line.lower():
            print(line, end='')
