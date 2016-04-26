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
    z = np.arange(0, 10, 10000)


    Thermonuclear_z = np.array([0.05, 0.25, 0.45, 0.65, 0.84, 1.16, 1.64])
    Thermonuclear_rate = np.array([0.25, 0.29, 0.44, 0.58, 0.64, 0.87, 0.63])*1e-4
    Thermonuclear_rate_error = np.array([0.05, 0.07, 0.11, 0.14, 0.20, 0.22, 0.22])*1e-4
    Corecollapse_z = np.array([0.04, 0.25, 0.38, 0.59, 1.14, 1.93])
    Corecollapse_ze = np.array([0.04, 0.04, 0.09, 0.13, 0.42, 0.37])
    Corecollapse_rate = np.array([0.72, 1.33, 1.81, 3.91, 3.22, 3.76])*1e-4
    Corecollapse_rate_error_high = np.array([0.06, 0.37, 0.31, 0.95, 0.93, 3.01])*1e-4
    Corecollapse_rate_error_low = np.array([0.06, 0.29, 0.28, 0.71, 0.58, 1.58])*1e-4

    fig, ax1 = pl.subplots()
    def plot_SN(rate, kinetic_energy, label, ax, color):
        calib = rate*kinetic_energy
        ax.plot(Corecollapse_z, calib*Corecollapse_rate, label=label, color = color)
        ax.errorbar(Corecollapse_z, calib*Corecollapse_rate, xerr=Corecollapse_ze, yerr=[calib*Corecollapse_rate_error_low , calib*Corecollapse_rate_error_high], fmt=".", capsize=0, elinewidth=1.5, ms=7, color = color)


    rates = np.array([0.524, 0.073, 0.064, 0.069, 0.176, 0.094])
    labels = ["IIP", "IIL", "IIn", "Ib", "Ic", "Faint CCSNe"]
    KE = np.array([1e51, 1e51, 1e51, 1e51, 1e51, 1e51])

    for ii, kk in enumerate(rates):
        plot_SN(kk, KE[ii], labels[ii], ax1, cmap[ii])


    ax1.plot(Thermonuclear_z, 1e51*Thermonuclear_rate, label="Ia", color = cmap[-2])
    ax1.errorbar(Thermonuclear_z, 1e51*Thermonuclear_rate, yerr=1e51*Thermonuclear_rate_error, fmt=".", capsize=0, elinewidth=1.5, ms=7, color = cmap[-2])


    SLSN_z = np.array([0.15, 1.5])
    SLSN_rate = np.array([55, 5*55])*1e-9
    SLSN_rate_error_high = np.array([45, 5*45])*1e-9
    SLSN_rate_error_low = np.array([45, 5*45])*1e-9

    ax1.plot(SLSN_z, 1e53*SLSN_rate, label="SLSN", color = cmap[-1])
    ax1.errorbar(SLSN_z, 1e53*SLSN_rate, yerr=[1e53*SLSN_rate_error_low , 1e53*SLSN_rate_error_high], fmt=".", capsize=0, elinewidth=1.5, ms=7, color = cmap[-1])


    ax1.set_xlabel("Redshift")
    ax1.set_ylabel(r"Energy Deposition / [erg yr$^{-1}$ Mpc$^{-3}$]")
    pl.legend(loc=2)
    ax1. set_ylim((0, 2.5e47))
    # ax1.semilogy()
    pl.savefig("figs/energy.pdf", clobber=True)
    pl.show()


if __name__ == '__main__':

    main()