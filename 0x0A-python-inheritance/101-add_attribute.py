#!/usr/bin/python3
add_attribute = __import__('101-add_attribute').add_attribute

class MyClass():
    pass

alx = MyClass()
add_attribute(alx, "name", "dan")
print(alx.name)

try:
    xx = "My String"
    add_attribute(xx, "name", "agweli")
    print(xx.name)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
