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

if __name__ == "__main__":
    print "Hello World"
    plt.figure(figsize=(8,4))
    plt.savefig("kf.png")
