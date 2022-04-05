import numpy as np
from Components.inductor import Inductor
from Components.capacitor import Capacitor
from Components.resistor import Resistor


def mag(z: complex):
    """Returns the magnitude of the complex number, 'z'.
    """
    return np.sqrt(z.real ** 2 + z.imag ** 2)


class CapacitiveBandPassFilter:

    def __init__(self, E: complex, c1: Capacitor, c2: Capacitor, r1: Resistor, load: Resistor):
        self.E = E; self.magE = mag(E)
        self.c1 = self.capacitor1 = c1; self.C_1 = c1.capacitance
        self.c2 = self.capacitor2 = c2; self.C_2 = c2.capacitance
        self.r1 = self.resistor1 = r1; self.R_1 = r1.resistance; self.Z_1 = r1.impedance
        self.load = load; self.R_L = load.resistance

    def _Z_a(self, f):
        return self.capacitor1.impedance(f)

    def _Z_b(self, f):
        return self.load.impedance + self.capacitor2.impedance(f)

    def _D(self, f):
        return 1/self._Z_a(f) + 1/self._Z_b(f)


    def Z_2(self, f):
        return 1/self._D(f)

    def _D_T(self, f):
        return self.Z_1 + self.Z_2(f)

    _Z_T = _D_T

    def I(self, f):
        """The total current flowing through the entire circuit as a function of the frequency.
        Note that this function returns the complex number representation of the waveform of aforementioned current."""
        return self.E / self._D_T(f)

    def I_a(self, f):
        """The branch current flowing through the capacitor denoted as 'c1' as a function of the frequency.
        This function returns the complex number representation of the waveform of the branch current."""
        pass

    def I_b(self, f):
        """The branch current flowing through the capacitor denoted as 'c2' and the load as a function of the frequency.
        This function returns the complex number representation of the waveform of the branch current."""
        return (self._Z_a(f) * self.I(f))/(self._Z_a(f) + self._Z_b(f))

    def load_voltage(self, f):
        """The voltage dropped across the load as a function of the frequency of the input voltage signal (input to the filter).
        This function returns the complex number representation of the output voltage waveform."""
        return self.load.impedance*self.I_b(f)

    def load_voltage_mag(self, f):
        """The amplitude (or magnitude) of the output voltage signal."""
        return self.R_L*mag(self.I_b(f))


class InductiveBandPassFilter:


    def __init__(self, E: complex, r1: Resistor, l1: Inductor, l2: Inductor, load: Resistor):
        self.E = E; self.magE = mag(E)
        self.r1 = self.resistor1 = r1; self.Z_1 = r1.impedance
        self.l1 = self.inductor1 = l1
        self.l2 = self.inductor2 = l2
        self.load = load

    def _Z_a(self, f):
        return self.inductor1.impedance(f)

    def _Z_b(self, f):
        return self.load.impedance + self.inductor2.impedance(f)

    def _D(self, f):
        return 1/self._Z_a(f) + 1/self._Z_b(f)

    def Z_2(self, f):
        return 1/self._D(f)

    def Z_T(self, f):
        return self.Z_1 + self.Z_2(f)

    def I(self, f):
        return self.E/self.Z_T(f)

    def I_b(self, f):
        return (self._Z_a(f)*self.I(f))/(self._Z_a(f) + self._Z_b(f))

    def load_voltage(self, f):
        return self.load.impedance * self.I_b(f)

    def load_voltage_mag(self, f):
        return self.load.resistance * mag(self.I_b(f))
