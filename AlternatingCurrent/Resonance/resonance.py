from math import sqrt, pi

def Vt(f: float):
	"""The angular velocity as a function of the frequency, denoted as 'f'."""
	return 2 * pi * f

def Wt(f: float):
	"""The angular velocity squared as a function of the frequency, denoted as 'f'."""
	return Vt(f)**2

def X_L_gen(L: float):
	""" The reactance of an inductor with an inductance of L as a function of the frequency,
	denoted as 'f'.  Note that this is a parametric function, with the only parameter being
 	the inductance, denoted as 'L', that returns another function with one *variable*, the
 	aforementioned frequency."""
	return lambda f: L * Vt(f)

def X_C_gen(C: float):
	""" The reactance of a capacitor with a capacitance of C as a function of the frequency,
	denoted as 'f'.  Note that this is a parametric function, with the only parameter being
 	the capacitance, denoted as 'C', that returns another function with one *variable*, the
 	aforementioned frequency."""
	return lambda f: 1/(C*Vt(f))

def tank_circ_zero_gen(L: float, C: float, E_T: float):
	"""The amplitude of the current -- in amps -- flowing through a simple LC parallel circuit
	(i.e. tank circuit) with zero resistance as a function of the frequency (f) of the AC waveform,
	the inductance (L), the capacitance (C), and the magnitude of the supplied or total voltage (E_T).
	Note that this is a parametric lambda function that returns a univariate function, with the only
	variable being the aforementioned frequency, denoted as 'f', in Hertz (Hz).

	Parameters:
		L:   Inductance in Henries(H);
		C:   Capacitance in Farads (F);
		E_T: Magnitude of the total voltage in volts (V)."""
	return lambda f: E_T*abs((C*L*(2*pi*f)**2-1)/(2*pi*f*L))

tank_circ_zero_res = tank_circ_zero_gen

def simple_series(R, L, C, E_T):
	X_L = X_L_gen(L)
	X_C = X_C_gen(C)
	return lambda f: E_T/sqrt(R**2+(X_L(f)-X_C(f))**2)

def A_gen(R, L, C, e):
	X_L = X_L_gen(L)
	return lambda f: e*sqrt(R**2 + Wt(f)*(C*(R**2+X_L(f)**2)-L)**2)/(R**2+X_L(f)**2)

def _Z1mag_gen(R, C):
	return lambda f: sqrt(R**2 + X_C_gen(C)(f)**2)

_gen_magZ1 = _Z1mag_gen

def A_gen_alt(R, L, C, e):
	Z1mag = _Z1mag_gen(R, C)
	return lambda f: sqrt(R**2/Z1mag(f)**4 + (X_C_gen(C)(f)/Z1mag(f)**2 - 1/X_L_gen(L)(f))**2)

gen_A_CsR_p_L = A_gen_alt
gen_A_C_p_RsL = A_gen

def _gen_magD_Z2(R, L):
	X_L = X_L_gen(L)
	return lambda f: sqrt(1/R**2 + 1/X_L(f)**2)

def gen_A_RsCsRpL(R_1, C, R_2, L, e):
	magD_Z2 = _gen_magD_Z2(R_2, L)
	def magZ_T(f):
		return sqrt((R_1 + 1/(R_2*magD_Z2(f)**2))**2 + (1/(X_L_gen(L)(f)*magD_Z2(f)**2) - X_C_gen(C)(f))**2)
	return lambda f: e / magZ_T(f)


