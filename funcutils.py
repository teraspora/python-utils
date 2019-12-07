import numpy as np
import matplotlib.pyplot as plt

def fseries(func, amp, freq):
    """
    Return the input function modified by 
    multiplying the argument by freq and the result by amp.
    """
    return lambda x: amp * func(freq * x)

def fsum(func, amps, freqs):
    """
    Return a function which applies the input function modified by the supplied
    arrays of amplitudes and frequencies and returns the sum of all these terms.
    """
    if len(amps) != len(freqs):
        return None
    else:
        return lambda x: sum([fseries(func, amp, freq)(x) for amp, freq in zip(amps, freqs)])

def plot_func_over_domain(func, ordinates):
    global plt
    abscissae = [func(x) for x in ordinates]
    plt.plot(ordinates, abscissae)
    plt.show()

def arng(start=0, stop=1, step=0.02):
    return np.arange(start, stop, step)

