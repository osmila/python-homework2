import math

import validate_input_console

A_TEXT = 'Enter parameters of quadratic equation. a = '
B_TEXT = 'b = '
C_TEXT = 'c = '


class QuadraticEquation:

    def __init__(self):
        self.a = validate_input_console.validate_input_is_not_zero(A_TEXT)
        self.b = validate_input_console.validate_input_is_float_number(B_TEXT)
        self.c = validate_input_console.validate_input_is_float_number(C_TEXT)
        self.d = 0
        self.x1 = 0
        self.x2 = 0

    def calc_discriminant(self):
        self.d = self.b * self.b - 4 * self.a * self.c

    def calc_roots(self):
        self.calc_discriminant()
        if self.d < 0:
            return self.x1, self.x2
        elif self.d > 0:
            self.x1 = (self.b * (-1) + math.sqrt(self.d)) / 2 * self.a
            self.x2 = (self.b * (-1) - math.sqrt(self.d)) / 2 * self.a
        else:
            self.x1 = self.x2 = (self.b * (-1)) / 2 * self.a
        return self.x1, self.x2

    def print_roots(self):
        self.calc_roots()
        self.x1 = round(self.x1, 4)
        self.x2 = round(self.x2, 4)
        if self.x1 == 0 and self.x2 == 0:
            print('There are no real roots: discriminant < 0')
        elif self.x1 == self.x2:
            print(f'There is only 1 root: x = {self.x1}')
        else:
            print(f'There are 2 real roots: x1 = {self.x1}, x2 = {self.x2}')
