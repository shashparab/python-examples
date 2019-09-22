class MyClass:
    variable = "blah"

    def function(self):
        print("This is inside class.")


myobjectx = MyClass()
myobjecty = MyClass()


myobjectx.function()
print(myobjecty.variable)
