import random
"""
Copying the code from the CodeDemos (Car Class), 
paste the code here and modify based on the instructions below
You are modifying the `Car` class to work as a self-driving car. 
Add a new instance variable: direction
- Direction is a single character, represented by "N", "E", "S", "W"
- The starting direction should be "N".
Add a `turn` method that takes in a string "L" or "R". 
- "L" represents the car turning Left
- "R" represents the car turning Right
Add a `drive` method to the car class. 
The drive method takes in a StopLight object.
- If the light is green, the car should accelerate by 5. 
- If the light is Yellow, the car should accelerate by 15, or brake. 
    - You can choose which implementation you prefer.
- If the light is red, the car should stop the car 
    - By pressing the brake (not setting speed to 0 manually).
"""

class Car:
    brakeSpeed = 15
    
    def __init__(self, make, model):
        """
        Constructor of car class. Takes in a make and model.
        The BlueTooth for a car is on by default.
        """
        self.carMake = make
        self.model = model
        self.blueToothOn = True
        self.speed = 0
        self.position = 0
        self.direction = "N"

    def getName(self):
        """
        Returns make and model of car instance.
        """
        return self.carMake + " " + self.model

    def onBlueTooth(self):
        """
        Turns on the BlueTooth
        """
        self.blueToothOn = True

    def offBlueTooth(self):
        """
        Turns off the BlueTooth
        """
        self.blueToothOn = False

    def accelerate(self, speed):
        """
        Given a speed, apply that much pressure
        """
        self.speed += speed

    def brake(self, color):
        """
        Brake the car
        """
        if self.speed < Car.brakeSpeed or color == "Red":
            self.speed = 0
        else:
            self.speed -= Car.brakeSpeed

    def isStopped(self):
        """
        tells if you are stopped
        """
        return self.speed == 0

    def turn(self, turn):
        if turn == "R" and self.direction == "N":
            self.direction = "E"
        elif turn == "L" and self.direction == "N":
            self.direction = "W"
        elif turn == "R" and self.direction == "E":
            self.direction = "S"
        elif turn == "L" and self.direction == "E":
            self.direction = "N"
        elif turn == "R" and self.direction == "S":
            self.direction = "W"
        elif turn == "L" and self.direction == "S":
            self.direction = "E"
        elif turn == "R" and self.direction == "W":
            self.direction = "N"
        elif turn == "L" and self.direction == "W":
            self.direction = "S"

    def getDirection(self):
        return self.direction

    def drive(self, light):
        if light.getColor() == "Green":
            self.speed += 5
        elif light.getColor() == "Yellow":
            x = random.randint(0,1)
            if x == 0:
                self.speed += 15
            else:
                self.brake(light.getColor())
        elif light.getColor() == "Red":
            self.brake(light.getColor())


    def __str__(self):
        """
        Displays the class instance in human form
        """

        return "Car: " + self.getName()


class StopLight:
  
    colors = ["Red", "Green", "Yellow"] # This is the same for all stoplight objects
    
    def __init__(self):
        self.index = 0 # This is different for each stoplight object
        self.light = StopLight.colors[self.index]

    def nextColor(self):
        if self.index == 2:
            self.index = 0
        else:
            self.index += 1
        
        self.light = StopLight.colors[self.index]

    def __str__(self):
        return "Light: " + self.light

    def getColor(self):
        return self.light

# TODO: Add Car class from CodeDemos here