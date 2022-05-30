""" 
Created by RoSteik (Telegram: @Rosteik)
"""


class Resistor:

    def __init__(self, name: str, resistance: int, power: int, accuracy: float):
        self.accuracy = accuracy  # - from 0 to 1
        self.power = power
        self.resistance = resistance
        self.name = name

    def __str__(self):
        return f'Name: {self.name}, resistance: {self.resistance}, power: {self.power}, accuracy: {self.accuracy}'
