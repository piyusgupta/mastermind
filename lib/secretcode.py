import sys
import random


class AvailableColours():
    Red = 1
    Green = 2
    Brown = 3
    Orange = 4
    Yellow = 5
    Blue = 6

    Black = 7
    White = 8

    NotAvailable = 0


class SecretCode():
    # available six colours
    available_colours = {1: 'Red',
                         2: 'Green',
                         3: 'Brown',
                         4: 'Orange',
                         5: 'Yellow',
                         6: 'Blue'}

    score_colours = {7: 'Black',
                     8: 'White',
                     0: 'Wrong'}

    def __init__(self):
        pass

    def set_secret_code(self):
        codes = []
        while len(codes) < 4:
            colour = random.choice(SecretCode.available_colours.keys())
            if colour not in codes:
                codes.append(colour)
        return codes
