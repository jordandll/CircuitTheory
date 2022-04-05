from numpy import pi


class Capacitor:

    def __init__(self, C: float):
        self.C = C

    @property
    def capacitance(self):
        return self.C

    @capacitance.setter
    def capacitance(self, C: float):
        self.C = C

    def reactance(self, f):
        return 1 / (2 * pi * f * self.C)

    def impedance(self, f):
        return complex(0, -self.reactance(f))

    X = reactance
    Z = impedance
