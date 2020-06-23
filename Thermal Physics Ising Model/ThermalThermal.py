from __future__ import division
import numpy as np
from numpy.random import rand
import matplotlib.pyplot as plt

def initialstate(N):
    state = 2*np.random.randint(2, size=(N,N))-1
    return state

def mcmove(config, beta):
    for i in range(N):
        for j in range(N):
                a = np.random.randint(0, N)
                b = np.random.randint(0, N)
                s =  config[a, b]
                nb = config[(a+1)%N,b] + config[a,(b+1)%N] + config[(a-1)%N,b] + config[a,(b-1)%N]
                cost = 2*s*nb
                if cost < 0:
                    s *= -1
                elif rand() < np.exp(-cost*beta):
                    s *= -1
                config[a, b] = s
    return config

def calcEnergy(config):
    energy = 0
    for i in range(len(config)):
        for j in range(len(config)):
            S = config[i,j]
            nb = config[(i+1)%N, j] + config[i,(j+1)%N] + config[(i-1)%N, j] + config[i,(j-1)%N]
            energy += -nb*S
    return energy/4.


nt = 250  # number of temperature points
N = 7  # size of the lattice, N x N
eqSteps = 1000  # number of MC sweeps for equilibration
mcSteps = 1000  # number of MC sweeps for calculation

T = np.linspace(1, 4, nt)  # temperature
Energy = np.zeros(nt)
Magnetization = np.zeros(nt)
SpecificHeat = np.zeros(nt)
Susceptibility = np.zeros(nt)

for m in range(len(T)):
    print m
    E1 = M1 = E2 = M2 = 0
    config = initialstate(N)

    for i in range(eqSteps):
        mcmove(config, 1.0 / T[m])

    for i in range(mcSteps):
        mcmove(config, 1.0 / T[m])  # monte carlo moves
        Ene = calcEnergy(config)  # calculate the energy

        E1 = E1 + Ene
        E2 = E2 + Ene * Ene;

        Energy[m] = E1 / (mcSteps * N * N)
        SpecificHeat[m] = (E2 / mcSteps - E1 * E1 / (mcSteps * mcSteps)) / (N * T[m] * T[m]);

f = plt.figure(figsize=(18, 10), dpi=80, facecolor='w', edgecolor='k');

sp = f.add_subplot(2, 2, 1);
plt.plot(T, Energy, 'o', color="#A60628", label=' Energy');
plt.xlabel("Temperature (T)", fontsize=20);
plt.ylabel("Energy ", fontsize=20);

sp = f.add_subplot(2, 2, 2);
plt.plot(T, SpecificHeat, 'd', color="black", label='Specific Heat');
plt.xlabel("Temperature (T)", fontsize=20);
plt.ylabel("Specific Heat ", fontsize=20);


plt.show()
#plt.savefig("8.27 20x20 512 time steps.pdf")

