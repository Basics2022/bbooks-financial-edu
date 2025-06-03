"""

Test about MPT, Modern Portfolio Theory

2-asset portfolio

"""

import numpy as np
import matplotlib.pyplot as plt

#> Expected returns and covariance
mu1, mu2 = 3.,  6.
si1, si2 = 1., 10.
r12 = 1.

mu = np.array([mu1, mu2])
si = np.array([[si1**2, si1*si2*r12], [si1*si2*r12, si2**2]])

#> Some functions
#> PTF expected return
ptf_mu = lambda w1, w2: w1 * mu1 + w2 * mu2
#> PTF variance
ptf_si = lambda w1, w2, si: w1**2 * si[0,0] + 2 * w1 * w2 * si[0,1] + w2**2 * si[1,1]
#> Covariance as a function of correlation coefficient, rho
si_fun = lambda rho: np.array([[si1**2, si1*si2*rho], [si1*si2*rho, si2**2]])



# ax.set_xlim([.0, .02])
# ax.set_ylim([.0, .1 ])

#> Example: effect of correlation

fig, ax = plt.subplots(1,1, figsize=(6,6))

nw = 101
w1v = np.arange(nw); w1v = w1v / (nw-1)

n_rho = 5
rho_v = np.arange(-n_rho, n_rho+1) / n_rho

for rho in rho_v:
    mu_v, si_v = [], []
    for iw in np.arange(nw):
        #> Asset weights
        w1 = w1v[iw];  w2 = 1. - w1
        #> PTF expected return, and variance
        mu_v += [ ptf_mu(w1,w2) ]
        si_v += [ ptf_si(w1,w2,si_fun(rho)) ]

    ax.plot(np.sqrt(si_v), mu_v, label=f"PTF, $\\rho = {rho}$")

ax.plot(si1, mu1, 'o', label='Asset 1')
ax.plot(si2, mu2, 'o', label='Asset 2')

ax.set_xlabel("Variance")
ax.set_ylabel("Expected return")
ax.grid()
ax.legend()

plt.show()

