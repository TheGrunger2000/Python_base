# -*- coding: utf-8 -*-

# Mastermind game engine v.0.1.0
# Made by Bogdan Czoriev. 2019
from random import randint

_hidden_number = []
NUMBER_LENGTH = 4


def generate_number():
    """
    Generation of four digit random number
    """
    global _hidden_number
    _hidden_number = []
    for digit in range(NUMBER_LENGTH):
        begin = 1 if digit == 0 else 0
        _hidden_number.append(randint(begin, 9))
    return _hidden_number


def check_number(number_string):
    """
    Checking the number for answering how much bulls and cows is here
    """
    user_answer = [int(x) for x in number_string]
    state = {'Bulls': 0, 'Cows': 0}

    for first_key, user_digit in enumerate(user_answer):
        if user_digit == _hidden_number[first_key]:
            state['Bulls'] += 1

    cow_count = 0
    cow_state = [True for _ in range(NUMBER_LENGTH)]
    for first_digit in user_answer:
        for index, second_digit in enumerate(_hidden_number):
            if first_digit == second_digit and cow_state[index]:
                cow_count += 1
                cow_state[index] = False

    state['Cows'] = cow_count - state['Bulls']
    return state
