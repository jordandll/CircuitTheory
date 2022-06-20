import numpy as np
from CircuitTheory.Components.inductor import Inductor
from CircuitTheory.Components.capacitor import Capacitor
from CircuitTheory.Components.resistor import Resistor


def mag(z: complex):
    """Returns the magnitude of the complex number, 'z'.
    """
    return np.sqrt(z.real ** 2 + z.imag ** 2)


class SeriesLCResonantFilter:

    def __init__(self, E: complex, l1: Inductor, c1: Capacitor, load: Resistor):
        self.E = E
        self.L1 = l1
        self.C1 = c1
        self.load = load

    def Z(self, f):
        """ The total impedance of the circuit (including the load) as a function of the 			frequency (f).
        Note that this returns the complex number representation of the impedance in 			rectangular form. """
        return self.load.impedance + self.L1.impedance(f) + self.C1.impedance(f)

    def mag_Z(self, f):
        """ The magnitude of total impedance of the circuit (including the load). """
        return mag(self.Z(f))

    def I(self, f):
        """ The current flowing circuit as a function of the frequency (f).
        Note that this returns the complex number representation of the current in 				rectangular form. """
        return self.E / self.Z(f)

    def mag_I(self, f):
        return mag(self.I(f))

    def load_voltage(self, f):
        """ The output voltage signal. """
        return self.load.resistance * self.I(f)

    def load_voltage_mag(self, f):
        return mag(self.load_voltage(f))

class CapacitiveBandPassFilter:

    def __init__(self, E: complex, c1: Capacitor, c2: Capacitor, r1: Resistor, load: Resistor):
        self.E = E
        self.magE = mag(E)
        self.c1 = self.capacitor1 = c1
        self.C_1 = c1.capacitance
        self.c2 = self.capacitor2 = c2
        self.C_2 = c2.capacitance
        self.r1 = self.resistor1 = r1
        self.R_1 = r1.resistance
        self.Z_1 = r1.impedance
        self.load = load
        self.R_L = load.resistance

    def _Z_a(self, f):
        return self.capacitor1.impedance(f)

    def _Z_b(self, f):
        return self.load.impedance + self.capacitor2.impedance(f)

    def _D(self, f):
        return 1 / self._Z_a(f) + 1 / self._Z_b(f)

    def Z_2(self, f):
        return 1 / self._D(f)

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
        return (self._Z_a(f) * self.I(f)) / (self._Z_a(f) + self._Z_b(f))

    def load_voltage(self, f):
        """The voltage dropped across the load as a function of the frequency of the input voltage signal (input to the filter).
        This function returns the complex number representation of the output voltage waveform."""
        return self.load.impedance * self.I_b(f)

    def load_voltage_mag(self, f):
        """The amplitude (or magnitude) of the output voltage signal."""
        return self.R_L * mag(self.I_b(f))


class InductiveBandPassFilter:

    def __init__(self, E: complex, r1: Resistor, l1: Inductor, l2: Inductor, load: Resistor):
        self.E = E
        self.magE = mag(E)
        self.r1 = self.resistor1 = r1
        self.Z_1 = r1.impedance
        self.l1 = self.inductor1 = l1
        self.l2 = self.inductor2 = l2
        self.load = load

    def _Z_a(self, f):
        return self.inductor1.impedance(f)

    def _Z_b(self, f):
        return self.load.impedance + self.inductor2.impedance(f)

    def _D(self, f):
        return 1 / self._Z_a(f) + 1 / self._Z_b(f)

    def Z_2(self, f):
        return 1 / self._D(f)

    def Z_T(self, f):
        return self.Z_1 + self.Z_2(f)

    def I(self, f):
        return self.E / self.Z_T(f)

    def I_b(self, f):
        return (self._Z_a(f) * self.I(f)) / (self._Z_a(f) + self._Z_b(f))

    def load_voltage(self, f):
        return self.load.impedance * self.I_b(f)

    def load_voltage_mag(self, f):
        return self.load.resistance * mag(self.I_b(f))


class TwinTBandStopFilter:
    """Also called band-elimination, band-reject, or notch filters, this kind of filter passes all frequencies above and
     below a particular range set by the component values. Not surprisingly, it can be made out of a low-pass and a
     high-pass filter, just like the band-pass design, except that this time we connect the two filter sections in
     parallel with each other instead of in series.

     Basically, this is the inverse of a band pass filter."""

    def __init__(self, E: complex, r1: Resistor, r2: Resistor, c1: Capacitor, c2: Capacitor, c3: Capacitor,
                 r3: Resistor,
                 load: Resistor):
        """The low-pass filter section consists of r1, r2, and c1 in a “T” configuration. The high-pass filter
        section consists of c2, c3, and r3 in a “T” configuration as well.

        This kind of filter gives a sharp response when the component values are chosen with the following ratios:

        R_1 = R_2 = 2 * R_3
        C_1 = C_2 = 0.5 * C_3"""
        self.E = E

        self.r1 = self.resistor1 = r1
        self.r2 = self.resistor2 = r2
        self.r3 = self.resistor3 = r3
        self.load = load

        self.c1 = self.capacitor1 = c1
        self.c2 = self.capacitor2 = c2
        self.c3 = self.capacitor3 = c3

    def I_34(self, f):
        """One of the two branch currents that flow through the load.  This function returns the complex number
        representation of said current."""
        """U := (Z_{R1}+Z_{C1})(R_2 + R_L) + Z_{C1}Z_{R1}"""
        R_1 = self.r1.resistance
        R_3 = self.r3.resistance
        R_L = self.load.resistance
        U = (self.r1.resistance + self.c1.Z(f)) * (self.r2.resistance + self.load.Z) + self.c1.Z(f) * self.r1.resistance
        Q = self.c2.Z(f) + self.r3.Z

        """I_{34}(R_L^2(Z_{C2}+R_3)(R_1+Z_{C1}) - U(R_3Z_{C2} + (Z_{C2}+R_3)(Z_{C3}+R_L)) ) 
        = R_LZ_{C1}E(Z_{C2}+R_3) - R_3EU"""

        Z_C1 = self.c1.Z
        Z_C2 = self.c2.Z
        Z_C3 = self.c3.Z

        return (self.load.resistance * self.c1.Z(f) * self.E * Q - self.r3.resistance * self.E * U) / (
                R_L ** 2 * Q * (R_1 + Z_C1(f)) - U * (R_3 * Z_C2(f) + Q * (Z_C3(f) + R_L)))

    def I_24(self, f):
        """The complex number representation of one of the two branch currents that flow through the load."""
        I_34 = self.I_34(f)
        R_3 = self.r3.resistance
        R_L = self.load.resistance
        Z_C2 = self.c2.Z(f)
        Z_C3 = self.c3.Z(f)
        E = self.E

        return (R_3 * (E - Z_C2 * I_34)) / (R_L * (Z_C2 + R_3)) - Z_C3 * I_34 / R_L - I_34

    def load_voltage(self, f):
        """Returns the complex number representation of the output voltage signal as a function of the frequency (f)."""
        return self.load.impedance * (self.I_34(f) + self.I_24(f))

    def load_voltage_mag(self, f):
        """The amplitude (magnitude) of the output voltage signal as a function of the frequency (f).
        The frequency of maximum rejection, a.k.a. the  notch frequency, denoted as 'f_notch', which is when the amplitude
        of the output voltage signal is at its lowest, is given by:

        f_notch = 1/(4*pi*R_3*C_3)"""
        return self.load.resistance * mag(self.I_24(f) + self.I_34(f))
