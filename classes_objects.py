# define the Vehicle class
class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str
# your code goes here

car1 = Vehicle()
car2 = Vehicle()

#setting the name
car1.name = "Fer"
car2.name = "Jump"

#setting the color
car1.color = "red"
car2.color = "blue"

#setting the kind
car1.kind = "convertible"
car2.kind = "van"

#setting the value
car1.value = 60000.00
car2.value = 10000.00

# test code
print(car1.description())
print(car2.description())