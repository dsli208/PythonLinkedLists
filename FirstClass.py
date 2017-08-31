class FirstClass(object):
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName

me = FirstClass("David", "Li")
print(me.firstName)
print(me.lastName)