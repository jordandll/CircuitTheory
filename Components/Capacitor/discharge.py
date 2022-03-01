from math import e, log

__doc__="One way to dischare a capacitor is to use it as the battery or power supply\
of a simple circuit with only a resistor as the other component.  This module contains\
a collection of parametric functions that give the values of certain quantities that\
are attributes of or related to attributes of a capacitor in this kind of environment."

def gen_charge(C, R, q_0):
	"""A parametric function that gives the charge in capacitor as a function
of time.  The parameters are:
  C:	The capacitance in farads;
  R:	The resistance in ohms;
  q_0:	The initial charge in Coloumbs."""
	return lambda t: q_0*e**(-t/(C*R))

def gen_time(C, R):
	"""A parametric function that gives the time it takes for the charge in a 
capacitor with a capacitance of C farads to reach X% of it's initial charge.
Parameter:
  C:	Capacitance in farads;;
  R:	Resistance in ohms."""
	return lambda X: C*R*(2*log(10) - log(X))
