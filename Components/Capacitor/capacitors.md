Suppose we have a circuit with only one component, a capacitor with a
capacitance of $C$ farads, along with a power source supplying a voltage
of $E$ volts. $$\frac{1}{C}\cdot\int i \cdot dt = E$$ The charge,
denoted as ’$q$’, as a function of time, is given by:
$$q(t) = \int i \cdot dt = C \cdot E(t)$$ The current, denoted as ’$i$’,
as a function of time is given by is given by: $$i(t) = C \cdot E'(t)$$

Negligible Resistance
=====================

The conductive materials that are used to construct circuits typically
have low, negligible, but still non-zero resistance. While this can
usually be ignored with most applications, for demonstrative purposes,
we will include this resistance, denoted as ’$R$’, in a circuit
equation. $$Ri + \frac{1}{C} \int i \cdot dt = E$$ The above is an
integral-differential (sp?) equation. To find the general solution for
$i$ we must differentiate throughout the equation with respect to time.
First note that there are two scenarios that will be covered: one where
the voltage is constant; and one where it is variable.

Constant Voltage
----------------

$$Ri' + \frac{1}{C} i = 0$$ Multiplying throughout by $C$ gives:
$$CRi' + i = 0$$ The general solution is of the form:
$$i\coloneqq i(t)=Ae^{mt}$$ Here, $A \in \math bb{R}$ is an arbitrary
constant to be solved for using an IVP or IBP, and $m$ is the solution
to the auxiliary equation (AE): $$CRm + 1 = 0$$ $$m = -\frac{1}{CR}$$ If
the initial charge in the capacitor is zero then the IVP must be:
$$\begin{gathered}
        Ri(0) + 0 = E\\
        RA = E\\
        A = \frac{E}{R}\\
    \end{gathered}$$ As one can see by looking at the solution for $m$,
the lower the capacitance, the faster the current approaches zero.

Capacitors In Series
====================

When there are two capacitors in series the total capacitance of the
circuit, denoted as ’$C_T$’, is given by:
$$C_T = \frac{1}{\frac{1}{C_1} + \frac{1}{C_2}}$$ This makes more sense
when looking at the following circuit equation.
$$Ri + \frac{1}{C_1} \int i \cdot dt + \frac{1}{C_2} \int i \cdot dt = E$$
Via the axiom of distribution,
$$Ri + \left(\frac{1}{C_1} + \frac{1}{C_2}\right)\int i \cdot dt = E$$
Via the above equation and the first equation of this section,
$$Ri + \frac{1}{C_T}\int i \cdot dt = E$$ And, via the first equation of
this section, $$\frac{1}{C_T} = \frac{1}{C_1} + \frac{1}{C_2}$$ Note
that the above equations are extensible. Assuming there are $n \in 
    \mathbb{N}$ capacitors in series,
$$C_T = \frac{1}{\frac{1}{C_1} + \frac{1}{C_2} + \dots +
    \frac{1}{C_n}}$$ and
$$\frac{1}{C_1} + \frac{1}{C_2} + \dots + \frac{1}{C_n}$$

Capacitors in Parallel
======================

Suppose there are two capacitors, denoted as ’$C1$’ and ’$C2$’, each
with a capacitance of $C_1$ and $C_2$ respectively, in parallel with one
another. The total capacitance, denoted as $C_T$, of the parallel
circuit is given by: $$\label{eq:parallel-capac}
        C_T = C_1 + C_2$$ In a parallel circuit, the voltage running
across each sub circuit is equal to the voltage of the power supply. In
the case of this circuit, the voltage running across $C1$ will be equal
to the voltage running across $C2$. This is in stark contrast to a
series circuit, in which case the voltages of each capacitor would add
up to the voltage of the power supply, meaning they wouldn’t be equal in
voltage per se.\
\
Assuming the voltage of the power supply of this parallel circuit is
equal to $E$ volts, the following holds true:
$$\label{eq:parallel-volts}
        \frac{1}{C_1}\int i_1 \cdot dt = \frac{1}{C_2} \int i_2 \cdot dt = E$$
Suppose the paradigm is such that:

-   $C1$ is the nearest to the power supply and is in between points $1$
    and $4$;

-   $C2$ is in between points $2$ and $3$;

-   And point $1$ is adjacent to the positive pole of the power supply.

The current, denoted as ’$I_T$’, in between point $1$ and the positive
pole of the power supply, henceforth ’$(+)$’, is equal to the current in
between point $4$ and the negative pole of the power supply, ’$(-)$’.
Both quantities are given by: $$\label{eq:parallel-cur}
        I_T = i_1 + i_2$$ Differentiating throughout equation
(\[eq:parallel-volts\]) with respect to time gives:
$$\tag{\ref{eq:parallel-volts}}
        \frac{1}{C_1} \cdot i_1 = \frac{1}{C_2} \cdot i_2 = E'(t)$$ Via
the above equation, equation (\[eq:parallel-cur\]), and substitution,
$$\tag{\ref{eq:parallel-cur}}
        I_T = (C_1  + C_2) \cdot E'(t)$$ And, via the above equation and
equation (\[eq:parallel-capac\]), $$\tag{\ref{eq:parallel-cur}}
        I_T = C_T \cdot E'(t)$$ Now consider the following:
$$E = \frac{1}{C_T} \int I_T \cdot dt$$ The above fits the form of the
standard equation that relates voltage with capacitance and charge,
which is equal to the primitive integral or anti-derivative of the
current.\
\
If we divide throughout equation (\[eq:parallel-cur\]) by $C_T$ and then
integrate throughout with respect to time we get the same equation that
relate capacitance and charge with voltage.

Capacitor as a Battery
======================

Using a capacitor as the battery or power supply of a circuit is one way
of discharging one.\
\
Suppose there is a circuit consisting of only a capacitor, serving as
the battery or power supply of the circuit, with a capacitance of $C$
farads and an initial charge of $q_0$ Coloumbs and a resistor with a
resistance of $R$ ohms. The following equations hold true:
$$V_C + V_R = \frac{1}{C}q(t) + Rq'(t) = 0$$ The above is a differential
equation with the charge in the capacitor, denoted as ’$q$’, as the
dependent variable and time ($t$) as the independent variable. As such,
the general solution for $q(t)$ is of the form:
$$q(t) := q(t \vert C, R, q_0) = Ae^{mt}$$ To solve for $m$, we use the
auxiliary equation: $$\begin{gathered}
        Rm + \frac{1}{C} = 0\\
        CRm + 1 = 0\\
        m = - \frac{1}{CR}\\
    \end{gathered}$$ And to solve for the arbitrary constant,
$A \in \mathbb{R}$, we use the IVP: $$q(0) = Ae^{m \cdot 0} = A = q_0$$
This leaves us with the specific solution for the parametric function
that gives the charge in the capacitor as a function of time.
$$q(t \vert C, R, q_0) = q_0e^{mt}$$

Time to Discharge
-----------------

The time it takes to discharge to a, presumably acceptable, value of
$X\text{\%}$ of $q_0$ is given by: $$\begin{gathered}
        q_0e^{mt} = 0.01Xq_0\\
        e^{mt} = 0.01X\\
        mt = \ln(0.01X) = \ln X - 2\ln 10\\
        t := t(X \vert C, R) = CR(2\ln 10 - \ln X)\\
    \end{gathered}$$

The Current
-----------

The measure of the current in is given by:
$$i(t) := i(t\vert C, R, q_0) = q'(t) = mq_0e^{mt}$$ Notice how,
assuming the product of the resistance and the initial charge is
positive, the current will be negative at any point in time – or, in
other words, the co-domain of $i(t)$ consists of only negative values.
This makes sense because the capacitor is discharging, or, in other
words, the charge is decreasing over time.
