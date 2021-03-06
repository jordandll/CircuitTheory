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
        self.r1 = self.resistor1 = r1; self.R_1 = r1.resistance
        self.load = load; self.R_L = load.resistance

    def _Z_a(self, f):
        return complex(0, -self.capacitor1.reactance(f))

    def _Z_b(self, f):
        return complex(self.load.resistance, -self.capacitor2.reactance(f))

    def _D(self, f):
        return 1/self._Z_a(f) + 1/self._Z_b(f)


    def Z_2(self, f):
        return complex(self.load.resistance/(mag(self._D(f))**2*mag(self._Z_b(f))**2),
                       (self.capacitor2.reactance(f)+1/self.capacitor1.reactance(f))/(mag(self._D(f))**2*mag(self._Z_b(f))**2))

    def _D_T(self, f):
        return self.resistor1.impedance + self.Z_2(f)

    def I(self, f):
        """The total current flowing through the entire circuit as a function of the frequency.
        Note that this function returns the complex number representation of the waveform of aforementioned current."""
        return complex(self.resistor1.resistance - (1/mag(self._D(f))**2)*(1/self.capacitor1.reactance(f) + self.capacitor2.reactance(f)/mag(self._Z_b(f))**2),
                       self.load.resistance/(mag(self._D(f))**2*mag(self._Z_b(f))**2))*complex(self.magE/mag(self._D_T(f))**2, 0)

    def I_a(self, f):
        """The branch current flowing through the capacitor denoted as 'c1' as a function of the frequency.
        This function returns the complex number representation of the waveform of the branch current."""
        pass

    def _I_b_real(self, f):
        """The real part of the complex number representation of the waveform of I_b"""
        return self.magE/mag(self._D_T(f))**2*(self.R_1 - 1/mag(self._D(f))**2*(self.c2.X(f)/mag(self._Z_b(f))**2 + 1/self.c1.X(f) - (self.R_1*self.R_L)/(self.c1.X(f)*mag(self._Z_b(f))**2)))

    def _I_b_imag(self, f):
        """The imaginary part of the complex number representation of the waveform of I_b"""
        return self.magE/mag(self._D_T(f))**2*(1/self.c1.X(f)*(mag(self._D_T(f))**2 - self.R_1**2 + self.R_1/mag(self._D(f))**2*(self.c2.X(f)/mag(self._Z_b(f))**2 + 1/self.c1.X(f))) - self.R_L/(mag(self._D(f))**2*mag(self._Z_b(f))**2))

    def I_b(self, f):
        """The branch current flowing through the capacitor denoted as 'c2' and the load as a function of the frequency.
        This function returns the complex number representation of the waveform of the branch current."""
        return complex(self._I_b_real(f), self._I_b_imag(f))

    def load_voltage(self, f):
        """The voltage dropped across the load as a function of the frequency of the input voltage signal (input to the filter).
        This function returns the complex number representation of the output voltage waveform."""
        return self.resistor1.impedance*self.I_b(f)

    def load_voltage_mag(self, f):
        """The amplitude (or magnitude) of the output voltage signal."""
        return self.R_L*mag(self.I_b(f))
