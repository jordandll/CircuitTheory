import resonance as res
import numpy as np
import matplotlib.pyplot as plt


def simple_series(R, L, C, E_T, start=100.00, stop=200.00, n=200):
    """Plots the amplitude of the current (in milli amps or mA) as a function of the frequency
    with the given parameters and returns the associated figure and axes
    objects (in that order)."""

    I = res.simple_series(R, L, C, E_T)
    mI = lambda f: 1000 * I(f)
    X = F = np.linspace(start, stop, num=n)
    mY = np.array(list(map(mI, F)))

    fig, ax = plt.subplots()
    ax.set_xlabel('frequency (Hz)')
    ax.set_ylabel('Amplitude (mA)')
    ax.set_title('Simples LC Series')
    ax.plot(X, mY, label=f'R={int(R):,d}' + r'$\Omega$')
    ax.legend()

    return fig, ax
