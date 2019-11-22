# -*- coding: utf-8 -*-
from .acts import *


class House:

    def __init__(self):
        self.food = 50
        self.dirt = 0
        self.money = 100

    # Changers
    def change_food_count(self, food_count):
        self.food += food_count
    
    def change_dirt_count(self, dirt_count):
        self.dirt += dirt_count

    def change_money_count(self, money_count):
        self.money += money_count

    # Getters
    def get_food_count(self):
        return self.food

    def get_dirt_count(self):
        return self.dirt

    def get_money_count(self):
        return self.money


class Person:

    def __init__(self):
        self.house = None
        self.name = None
        self.fullness = 50

        self.action = None

    # Changers
    def change_fullness_count(self, fullness_count):
        self.fullness += fullness_count

    # Setters
    def set_name(self, new_name):
        self.name = new_name
    
    def set_house(self, new_house):
        self.house = new_house

    def set_fullness(self, new_fullness):
        self.fullness = new_fullness

    def set_action(self, performing_action):
        self.action = performing_action(exposed_person=self)

    # Getters
    def get_fullness(self):
        return self.fullness

    def get_name(self):
        return self.name

    def get_house(self):
        return self.house

    # Performer
    def run_action(self):
        self.action().perform()

    # Special getter (just in case)
    def get_action(self):
        return type(self.action)


class Human(Person):

    def __init__(self, name):
        super().__init__()
        self.cat = None

        self.set_name(name)

    # Setters
    def set_cat(self, new_cat):
        self.cat = new_cat

    # Getters
    def get_cat(self):
        return self.cat

    def act(self):
        if self.get_fullness() <= 30 <= self.house.get_food_count():
            self.set_action(Eat)
            self.run_action()
        elif self.house.get_money_count() <= 30:
            self.set_action(Work)
            self.run_action()
        else:
            self.set_action(Walk)
            self.run_action()


class Cat(Person):

    def __init__(self):
        super().__init__()
        self.owner = None

    # Setters
    def set_owner(self, possible_owner):
        self.owner = possible_owner

    # Getters
    def get_owner(self):
        return self.owner

    def act(self):
        pass
