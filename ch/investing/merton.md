(fin-edu:investing:merton)=
# Merton's portfolio problem

Merton's portfolio problem deals with the choice of optimal fraction of investment in a risky asset $\pi_t$ and the consumption $c_t$.

Assuming that the wealth of a family or an individual can is invested with a fraction $\pi_t$ in a risky part of the portfolio with expected return $\mu$ and standard variation $\sigma_t$, and with a fraction $1-\pi_t$ in a risk-free asset with expected return $r_t$ and zero standard deviation, the wealth $x_t$ of a family or an individual evolves with the SDE

$$\begin{aligned}
  d X_t
  & = r_t (1 - \pi_t ) X_t \, dt + \mu_t \pi_t X_t \, dt - c_t \, dt + \pi_t \sigma_t X_t \, dW_t = \\
  & = r_t  X_t \, dt + \left( \mu_t - r_t \right) \pi_t X_t \, dt - c_t \, dt + \pi_t \sigma_t X_t \, dW_t \ , 
\end{aligned}$$

i.e. the equation of a [geometric Brownian motion with drift](https://basics2022.github.io/bbooks-statistics/ch/prob/processes-calculus.html#geometric-brownian-motion-with-drift), the same equation that can be used to discuss [sequence risk](fin-edu:principles:sequence-risk) in investment, especially dealing with withdrawal.

Optimization problem can be solved using **continuous-time reinforcement learning**, see as an example [Math:Introduction to RL](https://basics2022.github.io/bbooks-math-miscellanea/ch/rl/intro.html), and [Statistics:RL](https://basics2022.github.io/bbooks-statistics/ch/ml/rl.html) (**todo**). Optimal solution $\pi_t^*$, $c_t^*$ is the fraction invested in the risky asset and consumption that maximises the **value function**,

$$V(x,t) = \mathbb{E} \left[ \left. \int_{s=t}^{T} e^{- \rho (s-t)} u(c_s) \, ds + e^{-\rho(T-t)} B(T) u(X_T) \right| X_t = x \right] \ ,$$

i.e. the return of the choice defined as the cumulative discounted reward. Reward per unit time is the **utility function** $u(c_s)$, $\rho$ is a personal discount factor that weights present and future rewards, and $B(T)$ is a bequest function.

For constant expected return and volatility of the assets, and a utility function $u(x) = \frac{x^{1-\gamma}}{1 - \gamma}$ it's possible to find an analytical solution with optimal fraction invested in the risky asset

$$\pi^* = \frac{\mu - r}{\gamma \sigma^2} \ .$$

(fin-edu:investing:merton:hjb)=
## Recursive relation and Hamilton-Jacobi-Bellman relation

Writing the value function $V(X_{t+dt}, t+dt)$ and expanding as a Taylor series up to the first order in $dt$, it's possible to find a **Hamilton-Jacobi-Bellman** equation from a recursive relation.

$$\begin{aligned}
  V(X_t+dX_t, t+ dt) 
  & = \mathbb{E} \left[ \left. \int_{s=t+dt}^{T} e^{- \rho (s-t-dt)} u(c_s) \, ds + e^{-\rho(T-t-dt)} B(T) u(X_T) \right| X_{t+dt} \right] = \\
\end{aligned}$$

### Recursive relation

$$e^{-\rho  t    } V(X_t     , t   ) = \mathbb{E} \left[  \left. \int_{s=t   }^{T} e^{- \rho s} u(c_s) \, ds + e^{-\rho T} B(T) u(X_T) \right| X_{t   } \right]$$

$$\begin{aligned}
  e^{-\rho (t+dt)} V(X_t+dX_t, t+dt)
  & = \mathbb{E} \left[  \left. \int_{s=t+dt}^{T} e^{- \rho s} u(c_s) \, ds + e^{-\rho T} B(T) u(X_T) \right| X_{t+dt} \right] = \\
  & = \mathbb{E} \left[  \left. \int_{s=t   }^{T} e^{- \rho s} u(c_s) \, ds + e^{-\rho T} B(T) u(X_T) \right| X_{t+dt} \right]     
    - \mathbb{E} \left[  \left. \int_{s=t}^{t+dt} e^{- \rho s} u(c_s) \, ds                           \right| X_{t+dt} \right] = \\
\end{aligned}$$

$$e^{-\rho (t+dt)} V(X_t+dX_t, t+dt) = e^{-\rho t} V(X_t, t) - e^{-\rho t} u(c_t) \, dt$$
$$d \left( e^{-\rho t} V(X_t, t) \right) = - e^{-\rho t} u(c_t) \, dt$$
$$\rho V \, dt = d V + u(c_t) \, dt $$


### Taylor expansion
Taylor expansion of value function $v(t,x)$, valued with $x = X_t$, reads

$$\begin{aligned}
  dv 
  & = \partial_t v \, dt + \partial_x v \, dx + \dfrac{1}{2} \partial_{xx} v \, dx^2 + o(dt) = \\
  & = \partial_t v \, dt + \partial_x v \, dX_t + \dfrac{1}{2} \partial_{xx} v \, dX_t^2 + o(dt) = \\
  & = dt \left( \partial_t v + \partial_x v ( r_t + (\mu_t - r_t) \pi_t) X_t - \partial_x v \, c_t \right) + \partial_x v \, \pi_t \sigma_t X_t \, dW_t + \dfrac{1}{2} \partial_{xx} v \, \left( \pi_t \sigma_t X_t \right)^2 \, dt + o(dt) = \\
\end{aligned}$$

as $dX_t^2 = \left( \pi_t \sigma_t X_t \right)^2 dW_t^2 + o(dt) = \left(  \pi_t \sigma_t X_t \right)^2 dt + o(dt)$. Taking expected value,

$$d V = dt \, \mathbb{E}\left[ \partial_t v + \partial_x v ( r_t + (\mu_t - r_t) \pi_t) X_t - \partial_x v \, c_t + \dfrac{1}{2} \partial_{xx} v \, \left( \pi_t \sigma_t X_t \right)^2 \right] \ .$$

### Recursive relation for optimal solution

First order in $dt$ reads

$$\rho V^* = \max_{\pi_t, c_t} \left\{ \partial_t V^* + \partial_x V^* \left[ (\pi_t (\mu-r) + r) X_t - c_t  \right] + \dfrac{1}{2} \partial_{xx} V^* (\pi \sigma_t X_t)^2 + u(c_t) \right\} = \max_{\pi_t, c_t} \Phi$$

### Optimality condition

Zero gradient is a necessary condition for local extreme points,

$$\begin{cases}
  0 = \partial_{\pi_t} \Phi(\pi^*_t, c^*_t) = (\mu-r) X_t \partial_x V^* + \partial_{xx} V^* \pi^*_t \left( \sigma_t X_t \right)^2 \\
  0 = \partial_{  c_t} \Phi(\pi^*_t, c^*_t) = - \partial_x V^* + \partial_{c_t} u(c^*_t) \\
\end{cases}$$

and thus

$$
  \pi^*_t = -\dfrac{\partial_x V^*}{\partial_{xx} V^*} \dfrac{\mu - r}{X_t \sigma^2} \\
$$

```{dropdown} Necessary conditions on $\ u()\ $ for the Hessian to be definite negative

**todo**

```

### Example: utility function $u(x) = \frac{x^{1-\gamma}}{1-\gamma}$

$$\begin{cases}
  \pi^*_t = -\dfrac{\partial_x V^*}{\partial_{xx} V^*} \dfrac{\mu - r}{X_t \sigma^2} \\
  c^*_t = \left( \partial_x V^* \right)^{-\frac{1}{\gamma}}
\end{cases}$$

### Example: value function $\ V^*(t, x) = f^{\gamma}(t) \frac{x^{1-\gamma}}{1 - \gamma}$

With value function $V^*(x,t) = \dots$ and bequest function $B(T) = \varepsilon^T$

$$\dot{f}(t) = \nu \, f(t) - 1$$

with final condition $f(T) = \varepsilon$, and

$$\nu = \dfrac{1}{\gamma} \left\{ \rho - (1 - \gamma) \left( \dfrac{(\mu-r)^2}{2 \sigma^2 \gamma} + r  \right)  \right\} \ .$$

The solution of the ODE reads

$$f(t) =
\begin{cases}
  \dfrac{1}{\nu} + \left( \varepsilon - \dfrac{1}{\nu} \right) e^{-\nu (T-t)} & \text{,} \quad \text{ if $\nu \ne 0$} \\
  T - t + \varepsilon                                                         & \text{,} \quad \text{ if $\nu =   0$} \\
\end{cases}$$

Thus

$$\begin{aligned}
  \pi^*_t & = \dfrac{\mu - r}{\gamma \sigma^2} \\
  c^*_t   & = \dfrac{X_t}{f(t)} \\
\end{aligned}$$


