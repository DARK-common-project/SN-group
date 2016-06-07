#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division, print_function

import numpy as np

# Plotting
import matplotlib.pyplot as pl
import seaborn
seaborn.set_style('ticks')

cmap = seaborn.cubehelix_palette(8, start = 0.2, rot = 2.2)



def main():
    z = np.arange(0, 10, 0.001)
    logoh = np.arange(5, 10, 0.001)
    mstar = np.arange(5, 13, 0.001) # log(mstar)

    logoh_mstar = -1.492 + 1.847*mstar - 0.08026*mstar**2.
    Nia_fractionalchange = logoh_mstar ** (((2.35 - 1) * -0.08) / 0.5)
    # pl.plot(mstar, Nia_fractionalchange)#/(min(Nia_fractionalchange)))
    # pl.show()


    R_IIm = 10**(-12.15 -0.8*mstar)
    pl.plot(mstar, R_IIm)
    pl.semilogy()
    pl.xlabel(r"Log(M$_\star$)")
    pl.show()





if __name__ == '__main__':
    main()