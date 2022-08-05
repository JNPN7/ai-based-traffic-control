from abc import abstractclassmethod
from turtle import Vec2D


class Vehicle:
    def __init__(self, pos, speed, length, breadth) -> None:
        self.speed = speed
        self.length = length
        self.breadth = breadth
        self.pos = pos

        pass

    def get_speed(self) -> int:
        return self.speed
    
    def move(self):
        pass
    
    def stop(self):
        pass

    def change_speed(self):
        pass

    def draw(self):
        pass

class Bus(Vehicle):
    def __init__(self, pos, speed, length, breadth) -> None:
        super().__init__(pos, speed, length, breadth)
    

class Car(Vehicle):
    def __init__(self, pos, speed, length, breadth) -> None:
        super().__init__(pos, speed, length, breadth)