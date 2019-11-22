# -*- coding: utf-8 -*-
from random import randint

from .acts import *  # That's because we should import all the available actions from this file


class House:

    def __init__(self):
        self.food = 50
        self.cat_food = 10
        self.dirt = 0
        self.money = 100

    def __str__(self):
        return "Statistics: Food - {} || Cat Food - {} || Dirt - {} || Money - {}".format(self.get_food_count(),
                                                                                          self.get_cat_food_count(),
                                                                                          self.get_dirt_count(),
                                                                                          self.get_money_count())

    # Changers
    def change_food_count(self, food_count):
        self.food += food_count

    def change_cat_food_count(self, cat_food_count):
        self.cat_food += cat_food_count
    
    def change_dirt_count(self, dirt_count):
        self.dirt += dirt_count

    def change_money_count(self, money_count):
        self.money += money_count

    # Getters
    def get_food_count(self):
        return self.food

    def get_cat_food_count(self):
        return self.cat_food

    def get_dirt_count(self):
        return self.dirt

    def get_money_count(self):
        return self.money


class Person:

    def __init__(self):
        self.house = None
        self.name = ""
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
        self.action.perform()

    # Special getter (just in case)
    def get_action(self):
        return type(self.action)


class Human(Person):

    def __init__(self, name):
        super().__init__()
        self.cat = None

        self.set_name(name)

    def __str__(self):
        return "I am {}, my fullness - {}".format(self.get_name(), self.get_fullness())

    # Setters
    def set_cat(self, new_cat):
        self.cat = new_cat

    # Getters
    def get_cat(self):
        return self.cat

    # Special Methods
    def pick_a_cat(self, new_cat, cat_name):
        self.set_cat(new_cat)
        new_cat.set_owner(self)
        new_cat.set_house(self.house)
        new_cat.set_name(cat_name)
        print("{} picked a cat and called him {}".format(self.get_name(), cat_name))

    def go_to_the_house(self, new_house):
        self.set_house(new_house)
        print("{} now get his home! Congratulations!!!".format(self.get_name()))

    def act(self):
        if self.get_fullness() <= 30 <= self.house.get_food_count():
            self.set_action(EatHumanFood)
            self.run_action()
        elif self.house.get_money_count() <= 30:
            self.set_action(Work)
            self.run_action()
        else:
            bool_dice = randint(1, 2)
            if bool_dice == 1:
                self.set_action(Walk)
                self.run_action()
            else:
                self.set_action(Sleep)
                self.run_action()


class Cat(Person):

    def __init__(self):
        super().__init__()
        self.owner = None

        self.set_fullness(20)

    def __str__(self):
        return "It's a Cat {}. Fullness - {}. MEOW!!!".format(self.get_name(), self.get_fullness())

    # Setters
    def set_owner(self, possible_owner):
        self.owner = possible_owner

    # Getters
    def get_owner(self):
        return self.owner

    def act(self):
        if self.get_fullness() <= 15 <= self.house.get_cat_food_count():
            self.set_action(EatCatFood)
            self.run_action()
        else:
            bool_dice = randint(1, 3)
            if bool_dice == 1:
                self.set_action(Meow)
                self.run_action()
            elif bool_dice == 2:
                self.set_action(Spoil)
                self.run_action()
            else:
                self.set_action(Sleep)
                self.run_action()
