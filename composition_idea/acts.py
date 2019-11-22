# -*- coding: utf-8 -*-


# Superclass
class Action:

    def __init__(self, exposed_person):
        self.exposed_person = exposed_person
        self.exposed_house = exposed_person.get_house()


# Actions
class Walk(Action):

    def perform(self):
        self.exposed_person.change_fullness_count(fullness_count=-10)
        print("{} walked".format(self.exposed_person.get_name()))


class Eat(Action):

    def perform(self):
        self.exposed_person.change_fullness_count(fullness_count=30)
        self.exposed_house.change_food_count(food_count=-30)
        print("{} ate something".format(self.exposed_person.get_name()))


class Work(Action):

    def perform(self):
        self.exposed_person.change_fullness_count(fullness_count=-20)
        self.exposed_house.change_money_count(money_count=150)
        print("{} worked and got a lot of money".format(self.exposed_person.get_name()))
