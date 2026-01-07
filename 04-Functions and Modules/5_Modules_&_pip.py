'''
There are two types of modules in python:
1. Built-in modules
2. External modules

    List of all built-in modules: https://docs.python.org/3/py-modindex.html
'''


import math # math is a built-in module
print("The square root of 16 is: ",math.sqrt(16))
print(" ")


import My_Module # here, My_Module is an external module 
My_Module.mdls(11,5)
print(" ")


# we can also use pre defined or pre written external modules by 'pip intall requests' in terminal
# this request file doesn't show in my folder but python can read or use this file behind the scene
# after install the requests module file:
import requests # requests is module which is used to fetch the HTML of online pages
ggl = requests.get("https://www.google.com")
print(ggl.text) # it'll show the google's HTML code as text .. here text is a property