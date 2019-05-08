from classy import Car, StopLight

### Simulate 

myCar = Car("Honda", "Civic")

myCar.accelerate(35)
light1 = StopLight()
myCar.drive(light1)
print("Car speed should be 0 ?={}".format(myCar.speed))

# Continue the testing

myCar.accelerate(120)
light1.nextColor()
myCar.drive(light1)

print("Car speed should be 125 ?={}".format(myCar.speed))

myCar.turn("R")

print(myCar.getDirection())

myCar.turn("L")

print(myCar.getDirection())
