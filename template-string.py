"""
    There are several ways to manipulate Strings in Python.
    Most primitive way is to using format method for small
    changes it can be used for small changes however for
    wider changes it's wise to use Template.
"""
from string import Template

str1 = "You can use format {0} to manupilate to strings in {1}".format("method", "Python")

templ = Template("You can use format ${sub1} to manupilate to strings in ${sub2}")
str2 = templ.substitute(sub1="method", sub2="Python")

data = {"sub1":"method","sub2":"Python"}
str3 = templ.substitute(data)

if str1 == str2 and str2 == str3:
    print("All of them same")