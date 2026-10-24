class Vehicle:

    def __init__(self, max_speed, milage):
        self.max_speed = max_speed
        self.milage = milage

ModelX = Vehicle(240, 18)

print("Model max speed:", ModelX.max_speed)
print("Model milage:", ModelX.milage)