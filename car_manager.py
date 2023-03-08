from turtle import Turtle
import random
import math

COLORS = ["red", "orange", "black", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
SPAWN_Y_COORD_RANGE = list(range(-250, 260, 1))
SPAWN_X_COORD_RANGE = 300


class Car(Turtle):
    def __init__(self, speed):
        super().__init__()
        self.color(random.choice(COLORS))
        self.penup()
        self.setheading(180)
        self.setposition((SPAWN_X_COORD_RANGE, random.choice(SPAWN_Y_COORD_RANGE)))
        self.car_speed = speed
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=3)

    def move(self):
        self.forward(self.car_speed)

    def speed_car(self, increment):
        self.car_speed += increment


class CarManager:
    def __init__(self):
        self.min_num_of_cars = 0
        self.max_num_of_cars = 3
        self.cars = []
        self.car_base_speed = STARTING_MOVE_DISTANCE
        self.add_cars_to_cars_list()

    def add_cars_to_cars_list(self):
        num_of_cars_to_add = random.randint(self.min_num_of_cars, self.max_num_of_cars)
        for i in range(num_of_cars_to_add):
            self.cars.append(Car(self.get_car_base_speed()))

    def get_car_base_speed(self):
        return self.car_base_speed

    def speed_up_cars(self):
        self.car_base_speed += MOVE_INCREMENT
        self.min_num_of_cars += 1
        self.max_num_of_cars += 1
        for car in self.cars:
            car.speed_car(MOVE_INCREMENT)

    def delete_if_goes_out_of_screen(self, car):
        if car.xcor() >= 300:
            car.clear()
            del (self.cars[self.cars.index(car)])

    def move_cars(self):
        for car in self.cars:
            car.move()
            self.delete_if_goes_out_of_screen(car)

    def do_they_in_range_in_y(self, car_y_cor, turtle_y_cor):
        distance_on_y = abs(car_y_cor) - abs(turtle_y_cor)
        return abs(distance_on_y) <= 20

    # TODO figure out front and side collision

    def did_collision_happen(self, turtle_pos):
        collision_happened = False
        for car in self.cars:
            if car.distance(turtle_pos[0], turtle_pos[1]) < 45:
                if self.do_they_in_range_in_y(car.ycor(), turtle_pos[1]):
                    print("collision!")
                    collision_happened = True
                    break
        return collision_happened
