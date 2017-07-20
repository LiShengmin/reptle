
class Person:
    def __init__(self, name):
        self.name = name
    def say(self):
        print "Hello, class:"+ self.name

p = Person('Lee Shemmy')
p.say()

