# -*- coding: utf-8 -*-
from composition_idea.src.objects import *  # That's because we need all the objects from that file

home_sweet_home = House()
print(home_sweet_home)

jack = Human(name="Jack")
print(jack)

cat = Cat()
print(cat)

jack.go_to_the_house(new_house=home_sweet_home)
jack.pick_a_cat(new_cat=cat, cat_name="Tomas")
print(cat)

for day in range(366):
    print("================================== Day {} ==================================".format(day))
    jack.act()
    cat.act()

    print("----------------------------------------------------------------------------")
    print("Daily Reward:")
    print("\n")
    print(jack)
    print(cat)
    print("\n")
    print(home_sweet_home)
    print("----------------------------------------------------------------------------")
