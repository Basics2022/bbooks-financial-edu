"""

Test about MPT, Modern Portfolio Theory

3-asset portfolio

"""

import numpy as np
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
des_ret_v = np.linspace(mu1, mu3, 8)

print(des_ret_v)

A = np.block([[ 2*si, mu.reshape(3,1), np.ones((3,1))], [mu.reshape(1,3), np.zeros((1,2))], [np.ones((1,3)), np.zeros((1,2))]])
b = np.zeros(5)
b[4] = 1. 

for desired_ret in des_ret_v:

    b[3] = desired_ret
    x = np.linalg.solve(A,b)

    sig2 = np.sqrt(x[:3].T @ si @ x[:3])

    print(f"Desired Return: {desired_ret}; Weights: {x[:3]}; Min variance: {sig2}")

    ax.plot(sig2, desired_ret, 'x', label=f"MPT", color='black')

ax.set_xlabel("Variance")
ax.set_ylabel("Expected return")
ax.grid()
ax.legend()

plt.show()


