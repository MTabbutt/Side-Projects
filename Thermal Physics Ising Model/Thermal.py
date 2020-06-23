from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
from numpy.random import rand


#What even is Thermal Physics?


#########################################################
######       The Ising Model of a Ferromagnet     #######
#########################################################



#Chapter Notes go here: Kudos for actually reading the chapter too


# N is the total number of dipoles
# S_i is the current state of the i-th dipole
# S=1 is dipole up and S = -1 is the dipole down
# energy of neighbor pairs if -e when parallel and +e when antiparallel
#Then energy can be written (-e)(S_i)(S_j)
# n is the number of nearest neighbors S_i has, so 4 in 2-D
# Monte Carlo simulation: Create a sampling of as many states as you can cuz
#                   you can't do it all, just like any undergrad realizes at some point
# Monte Carlo simulating with importance sampling
# Metropolis algorithm creates subset of system states in which low energy
#                   states occur more frequently than high



##############################################################
#Schroeder 8.26, A and B: If your computer isnt fast enough increase lattice size, scare to make run faster...

# A. Run lattice code for 20x20 lattice at T= 10, 5, 4, 3, 2.5 for at least 100 iterations per dipole per run
    # at each temperature make a rough estimate of the size of the largest cluster

#B. Repeat A for 40 x 40 answer questions. Dont forget like dummy you are sometimes.
##############################################################

class Ising():


    def M_C_Move (self, config, N, beta):     #The Monte Carlo moves
        for i in range (N):
            #print (i)
            for j in range(N):
                a = np.random.randint(0, N)
                b = np.random.randint(0, N)
                s = config[a,b]
                nb = config[(a+1)%N, b] + config[a, (b+1)%N] + config[(a-1)%N, b] + config[a, (b-1)%N]
                cost = 2*s*nb
                if cost < 0:
                    s *= -1
                elif rand() < np.exp(-cost*beta):
                    s *= -1
                config [a, b] = s
        return config

    def Simulate(self):
        T = 2.5
        N = 150
        config = 2*np.random.randint(2, size=(N,N))-1
        f = plt.figure(figsize=(15, 15), dpi=80);
        self.configPlot(f, config, 0, N, 1);

        measurement = 2500
        for i in range(measurement):
            print (i)
            self.M_C_Move(config, N, 1.0/T)

            if i == 1: self.configPlot(f, config, i, N, 2);
            if i == 500: self.configPlot(f, config, i, N, 3);
            if i == 1250: self.configPlot(f, config, i, N, 4);
            if i == 2000: self.configPlot(f, config, i, N, 5);
            if i == 2500: self.configPlot(f, config, i, N, 6);

    def configPlot(self, f, config, i, N, n_):
        X, Y = np.meshgrid(range(N), range(N))
        sp = f.add_subplot(3, 3, n_)
        plt.setp(sp.get_yticklabels(), visible=False)
        plt.setp(sp.get_xticklabels(), visible=False)
        plt.pcolormesh(X, Y, config, cmap='Greys');
        #plt.pcolormesh(X, Y, config, cmap=plt.cm.RdBu);
        plt.title('Time=%d' % i);
        plt.axis('tight')
        #plt.show()



#Scroeder 8.27: Insert Hint here and use wisely




rm = Ising()
rm.Simulate ()
plt.savefig("trying to break Mac 150x150 T=2.5, t=2500 GreyScale.pdf")
plt.show()



# Manually change numbers for B, didnt make it automated, because sometimes life should be harder...








