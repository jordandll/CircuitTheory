class Resistor:

    def __init__(self, R: float):
        self.R = R

    @property
    def resistance(self):
        return self.R

    @resistance.setter
    def resistance(self, R: float):
        self.R = R

    @property
    def reactance(self):
        return self.R

    @property
    def impedance(self):
        return complex(self.R, 0)

    X = reactance
    Z = impedance
