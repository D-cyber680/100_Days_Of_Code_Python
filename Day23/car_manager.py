import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
SIZE = (4.0, 8.0)


class CarManager:
    def __init__(self):
        self.list_of_cars = []
        self.distance = STARTING_MOVE_DISTANCE

    def create_car(self):
        if random.randint(1, 7) == 1:
            t = Turtle()
            t.penup()
            t.shape('square')
            t.shapesize(1, 2)
            t.color(random.choice(COLORS))
            t.goto(300, random.randint(-250, 250))
            self.list_of_cars.append(t)


    def move_car(self):
        for car in self.list_of_cars:
            car.backward(self.distance)

    # metodo para checar que el carro se encuentre en la pantalla, de ser asi eliminarlo de la lista
    def update_list(self):
        for car in self.list_of_cars:
            if car.xcor() > 340 or car.xcor() < -340:
                self.list_of_cars.remove(car)

        # metodo para checar la colision (distancia) de todos los carros de la lista con respecto al juagador

    def check_collision(self, player):
        for car in self.list_of_cars:
            if car.distance(player) < 20:
                return True

    def increment_speed_of_cars(self):
        self.distance += MOVE_INCREMENT



