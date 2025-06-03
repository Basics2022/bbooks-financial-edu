"""

Test about MPT, Modern Portfolio Theory

3-asset portfolio

"""

import numpy as np
from scipy.optimize import minimize
from functools import partial

import matplotlib.pyplot as plt

#> Expected returns and covariance
mu1, mu2, mu3 = 3.,  6., 10.
si1, si2, si3 = 1., 10., 25.
r12, r13, r23 = .2, .5, -.8

mu = np.array([mu1, mu2, mu3])
si = np.array([
    [      si1**2, si1*si2*r12, si1*si3*r12],
    [ si1*si2*r12,      si2**2, si2*si3*r13],
    [ si1*si3*r13, si2*si3*r23,      si3**2]
 ])

#> MPT
# Constraints:
# - desired PTF expected return, w*mu = r
# - sum of weights = 1         , sum(w) = 1
# Optimize (find min) PTF variance
# siR = w * si * w
# 
# with constraints on weights, 0 <= w[i] <= 1
#
# Without prescribing inequality constraints in the optimization, it's possible to perform
# optimization with equality constraints only, and then check if the inequality constraints
# are satisfied. Augmented objective function reads
#
# si = w * si * w - s1 * ( R - w.T * mu ) - s2 ( 1 - w.T * 1 )
# 
# An analytical solution of the equality constrined-only optimization exists
# [ 2*si   mu    1   ] [ w  ]    [ 0 ]
# [ mu.T    0    0   ] [ s1 ]  = [ R ]
# [  1.T    0    0   ] [ s2 ]    [ 1 ]

#> Initialize plot
fig, ax = plt.subplots(1,1, figsize=(6,6))

ax.plot(si1, mu1, 'o', label='Asset 1')
ax.plot(si2, mu2, 'o', label='Asset 2')
ax.plot(si3, mu3, 'o', label='Asset 3')

#> Loop over desired returns, between min and max return of single assets
des_ret_v = np.linspace(mu1, mu3, 15)

A = np.block([[ 2*si, mu.reshape(3,1), np.ones((3,1))], [mu.reshape(1,3), np.zeros((1,2))], [np.ones((1,3)), np.zeros((1,2))]])
b = np.zeros(5)
b[4] = 1. 

#> Constraints
def eq_desired_return(x, mu, desired_ret):
    return np.sum( x * mu ) - desired_ret

def eq_weight_sum(x):
    return np.sum(x) - 1

#> Objective function
def ptf_var(x, sigma):
    return x.T @ sigma @ x

wmat = [ ]
min_sig = []

for desired_ret in des_ret_v:

    eq_cons = [
        {'type':   'eq', 'fun': partial(eq_desired_return, mu=mu, desired_ret=desired_ret)},
        {'type':   'eq', 'fun': eq_weight_sum},
        {'type': 'ineq', 'fun': lambda x: x[0]},
        {'type': 'ineq', 'fun': lambda x: x[1]},
        {'type': 'ineq', 'fun': lambda x: x[2]},
        {'type': 'ineq', 'fun': lambda x: 1-x[0]},
        {'type': 'ineq', 'fun': lambda x: 1-x[1]},
        {'type': 'ineq', 'fun': lambda x: 1-x[2]},
    ]

    cost_fun = partial(ptf_var, sigma=si)

    x0 = np.zeros(3); x0[0] = 1  #  np.ones(3) / 3.
    res = minimize(cost_fun, x0, constraints=eq_cons,)

    # print(f"Desired Return: {desired_ret}, res: {res.x}")

    ptf_si = np.sqrt(res.x @ si @ res.x)
    ptf_mu = np.sum(res.x * mu)
    ax.plot(ptf_si, ptf_mu, 'x', color='black' )

    #> Store weights and min variance, for the desired expected return
    wmat += [ res.x ]
    min_sig += [ ptf_si ]

ax.set_xlabel("Variance")
ax.set_ylabel("Expected return")
ax.grid()
ax.legend()


#> Asset weights
wmat = np.array(wmat)

fig, ax = plt.subplots(2,1, figsize=(6,6))

for i in np.arange(np.shape(wmat)[1]):
    ax[0].plot(des_ret_v, wmat[:,i], label=f"Asset{i}")

ax[0].legend()
ax[0].set_ylabel("Weights")
ax[0].grid()

ax[1].plot(des_ret_v, min_sig)
ax[1].grid()
ax[1].set_xlabel("Desired return")
ax[1].set_ylabel("Min variance")

plt.show()


