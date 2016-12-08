# -*- coding: utf-8 -*-

import re

from findways.backend.business.way import Way


def remove_symbol(price):
    """Removes the € symbol from the price"""
    reg = r"[0-9]+(-|.)[0-9]+"
    numbers = re.finditer(reg, price, re.MULTILINE)
    for matchNum, number in enumerate(numbers):
        return number.group()


class Uber(Way):
    """Class that inherits from the Way class. Objects from this class are Uber Ways with all the relevant information"""
    def __init__(self, display_name="", low_price_estimate=0, high_price_estimate=0, price=0, surge_multiplier=1, wait_time=0, duration=0, distance=0):
        Way.__init__(self)
        self.type = ["u"]
        self.display_name = display_name
        self.low_price_estimate = low_price_estimate
        self.high_price_estimate = high_price_estimate
        self.price = price
        self.surge_multiplier = surge_multiplier
        self.wait_time = wait_time
        self.duration = duration
        self.distance = distance

    def get_type(self):
        return self.type

    def get_display_name(self):
        return self.display_name

    def get_low_estimate(self):
        return self.low_price_estimate

    def get_high_estimate(self):
        return self.high_price_estimate

    def get_price(self):
        return self.price

    def get_surge_multiplier(self):
        return self.surge_multiplier

    def get_wait_time(self):
        return self.wait_time

    def get_duration(self):
        return self.duration

    def get_distance(self):
        return self.distance

    def uber_to_string(self):
        print("Display name: " + str(self.display_name) + "\nLow estimate: " + str(self.low_price_estimate) + "\nHigh estimate: " + str(self.high_price_estimate)
            + "\nSurge multiplier: " + str(self.surge_multiplier) + "\nWait time: " + str(self.wait_time) + '\nDuration: ' + str(self.duration) + '\n')

if __name__ == "__main__":
    print(remove_symbol('62.82 €'))