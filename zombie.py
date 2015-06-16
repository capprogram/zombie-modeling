# zombie apocalypse modeling
# This code has been modified from http://www.scipy.org/Cookbook/Zombie_Apocalypse_ODEINT

#Below we import packages needed to solve and plot ODE's
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from pylab import savefig

# turn on interactive mode for matplotlib
plt.ion()

# set the parameter values
P = 0       # birth rate
d = 0.0001  # natural death percent (per day)
B = 0.0095  # transmission percent  (per day)
G = 0.0001  # resurect percent (per day)
A = 0.0001  # destroy percent  (per day)
N = 1000   	# Number of time steps
Tf = 10		# final time (days)

# solve the system dy/dt = f(y, t)
def f(y, t):
        Si = y[0]
        Zi = y[1]
        Ri = y[2]
        # the model equations (see Munz et al. 2009)
        f0 = P - B*Si*Zi - d*Si
        f1 = B*Si*Zi + G*Ri - A*Si*Zi
        f2 = d*Si + A*Si*Zi - G*Ri
        return [f0, f1, f2]

# initial conditions
S0 = 500.               # initial population
Z0 = 0                  # initial zombie population
R0 = 0                  # initial death population
y0 = [S0, Z0, R0]       # initial condition vector
t  = np.linspace(0, Tf, N)   # time grid

# solve the DEs
soln = odeint(f, y0, t)
S = soln[:, 0]
Z = soln[:, 1]
R = soln[:, 2]

# plot results
plt.figure()
plt.plot(t, S, label='Living')
plt.plot(t, Z, label='Zombies')
plt.xlabel('Days from outbreak')
plt.ylabel('Population')
plt.title('Zombie Apocalypse - No Init. Dead Pop.; No New Births.')
plt.legend(loc=0)
savefig('R0=0-P=0.png', dpi=100)