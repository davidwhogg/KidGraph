"""
This file is part of the Kid Function project.
Copyright 2013 David W. Hogg.

### bugs:
- doesn't work
"""

import matplotlib
matplotlib.use("Agg")
import pylab as plt
import numpy as np

def set_lims(ax):
    xlim = np.array([-2., 2.])
    ylim = np.array([-2., 2.])
    ax.set_xlim(xlim)
    ax.set_ylim(ylim)
    ax.axis('off')
    ax.axvline(0, color="0.5", lw=0.5)
    for y in (-1., 0., 1.):
        ax.axhline(y, color="0.5", lw=0.5)
    return xlim, ylim

def xvec(xlim):
    dx = 0.001
    return np.arange(xlim[0] + 0.5 * dx, 0., dx)

def yvec(xp, amps):
    yp = np.zeros_like(xp)
    kfactorial = 1
    for k in range(10):
        if len(amps) > k:
            kfactorial *= np.max([k, 1])
            yp += amps[k] * xp ** k / float(kfactorial)
    return yp

def savefig(fn):
    print "writing %s" % fn
    return plt.savefig(fn)

def make_card(fn, amps, even=False, odd=False):
    plt.figure(figsize=(8,4))
    plt.axes([0., 0., 1., 1.])
    ax = plt.gca()
    xlim, ylim = set_lims(ax)
    xp = xvec(xlim)
    yp = yvec(xp, amps)
    plt.plot(xp, yp, 'k-', lw=5.)
    assert (not (even and odd))
    if even:
        nyp = yp
    elif odd:
        nyp = -1. * yp
    else:
        nyp = yvec(-xp, amps)
    plt.plot(-xp, nyp, 'k-', lw=5.)
    savefig(fn)

if __name__ == "__main__":
    amplist = [-1., 0., 1.]
    i = 0
    for amp3 in amplist:
        for amp2 in amplist:
            for amp1 in amplist:
                for amp0 in amplist:
                    for even, odd in [(True, False), (False, True), (False, False)]:
                        fn = "kf%04d.png" % i
                        amps = np.array([amp0, amp1, amp2, amp3])
                        make_card(fn, amps, even=even, odd=odd)
                        i += 1
