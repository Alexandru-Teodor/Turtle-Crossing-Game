from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.top_cars = []
        self.bottom_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_top_cars(self):
        new_car = Turtle("square")
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.penup()
        new_car.color(random.choice(COLORS))
        random_x = random.randrange(-270, 270, 40)
        random_y = random.randrange(10, 250, 20)
        new_car.goto(random_x, random_y)
        self.top_cars.append(new_car)

    def create_bottom_cars(self):
        new_car = Turtle("square")
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.penup()
        new_car.color(random.choice(COLORS))
        random_x = random.randrange(-270, 270, 40)
        random_y = random.randrange(-250, -10, 20)
        new_car.goto(random_x, random_y)
        self.bottom_cars.append(new_car)

    def move_cars(self):
        for car in self.top_cars:
            car.backward(self.car_speed)
        for car in self.bottom_cars:
            car.forward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT

    def check_cars_on_screen(self):
        for car in self.top_cars:
            if car.xcor() < -319:
                random_y = random.randrange(10, 250, 20)
                car.goto(320, random_y)
        for car in self.bottom_cars:
            if car.xcor() > 319:
                random_y = random.randrange(-250, -10, 20)
                car.goto(-320, random_y)
