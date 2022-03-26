from numpy import pi


class Capacitor:

    def __init__(self, C: float):
        self.C = C

    def reactance(self, f: float):
        return 1 / (2 * pi * f * self.C)

    def impedance(self, f: float):
        return complex(0, -self.reactance(f))
