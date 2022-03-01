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


