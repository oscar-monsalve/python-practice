class Robot:
    def __init__(self, name, color, weight):
        self.name = name
        self.color = color
        self.weight = weight

    def introduction(self):
        print(f"Hello!, my name is {self.name} and I am a robot")


r1 = Robot("Ramiro", "red", 80)

r1.introduction()
