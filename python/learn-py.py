
x= "sdsd"
d = ["dada","sdsds","fgdfdf","vxcvcvc"]
if x=="sdsd":
    print("haha")

d.append("ahaha")

object = {
    "key1": 123,
    "key2": "sdsdsd"
}

for y in d:
    print(y)

print(x)
print(d[0])
print(object["key1"])

for key in object:
    print("ahaha", object)

class Car:
    def __init__(self, number_of_wheels, seating_capacity, maximum_velocity):
        self.number_of_wheels = number_of_wheels
        self.seating_capacity = seating_capacity
        self.maximum_velocity = maximum_velocity

class Notification:
    def __init__(self, number_of_wheels, seating_capacity, maximum_velocity):
        Car.__init__(self, number_of_wheels, seating_capacity, maximum_velocity)

my_electric_car = Notification(4, 5, 250)
print(my_electric_car.number_of_wheels) # => 4
print(my_electric_car.seating_capacity) # => 5
print(my_electric_car.maximum_velocity) # => 250