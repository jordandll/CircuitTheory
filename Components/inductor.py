from numpy import pi


class Inductor:

    def __init__(self, L: float):
        self.L = L

    @property
    def inductance(self):
        return self.L

    @inductance.setter
    def inductance(self, L):
        self.L = L

    def reactance(self, f: float):
        return 2 * pi * f * self.L

    def impedance(self, f: float):
        return complex(0, self.reactance(f))

    Z = impedance
    X = reactance
