(fin-edu:investing:merton)=
# Merton's portfolio problem

Merton's portfolio problem is an **optimization problem** dealing with the choice of optimal fraction of investment in a risky asset $\pi_t$ and the consumption $c_t$, making a value function maximum. Merton's assume that the portfolio is build with a risk-free and a risky asset only. In this problem, there's no minimum spending level (subsistence level, what you need for survival), or transasction costs. Under some assumptions, the optimal fraction of the investment in the risky asset $\pi^*_t$ is constant (need for - free, as costs are neglected - rebalancing) and equal to the ratio of the excess return of the risky asset $\mu - r$, scaled by its volatility $\sigma^2$ and a personal risk aversion $\gamma$,

$$\pi^* = \frac{\mu - r}{\gamma \sigma^2} \ ,$$

and the consumption is proportional to the wealth by a factor depending on time $t$,

$$c^*_t = \frac{X_t}{f(t)}$$

(fin-edu:investing:merton:wealth-dynamics)=
## Wealth dynamics

Assuming that the wealth of a family or an individual can is invested with a fraction $\pi_t$ in a risky part of the portfolio with expected return $\mu$ and standard variation $\sigma_t$, and with a fraction $1-\pi_t$ in a risk-free asset with expected return $r_t$ and zero standard deviation, the wealth $x_t$ of a family or an individual evolves with the SDE

$$\begin{aligned}
  d X_t
  & = \underbrace{ (1 - \pi_t ) r_t X_t \, dt }_{\text{risk-free asset}} + \underbrace{\pi_t \left( \mu_t X_t \, dt + \sigma_t X_t \, dW_t \right)}_{\text{risky asset}} - \underbrace{ c_t \, dt}_{\text{consumption}} \ ,
\end{aligned}$$

or, rearranging for $dt$, and $dW_t$,

$$\begin{aligned}
  dX_t & = \underbrace{\left[ r_t + \left( \mu_t - r_t \right) \pi_t \right] X_t \, dt}_{\text{expected return}} - \underbrace{c_t \, dt}_{\text{consumption}} + \underbrace{\pi_t \sigma_t X_t \, dW_t}_{\text{volatility of the return}} \ , 
\end{aligned}$$

i.e. the equation of a [geometric Brownian motion with drift](https://basics2022.github.io/bbooks-statistics/ch/prob/processes-calculus.html#geometric-brownian-motion-with-drift), with
* 1-period (or percentage) expected value $(1-\pi_t) r_t + \pi_t \mu_t = r_t + \pi_t (\mu_t - r_t)$
* 1-period (or percentage) std-deviation $\pi_t \sigma_t$
* 1-period (or percentage) drift $-c_t$


This is the same equation as the one that can be used to discuss [sequence risk](fin-edu:principles:sequence-risk) in investment, especially dealing with withdrawal.

(fin-edu:investing:merton:value-function)=
## Value function

The goal of the problem is the maximization of a objective function representing the life-time cumulative discounted reward, using *continuous-time* **reinforcement learning** vocabulary, see as an example [Math:Introduction to RL](https://basics2022.github.io/bbooks-math-miscellanea/ch/rl/intro.html), or - roughly - cumulative happiness. The objective function can be written as a value function,

$$V(x,t) = \mathbb{E} \left[ \left. \int_{s=t}^{T} e^{- \rho (s-t)} u(c_s) \, ds + e^{-\rho(T-t)} B(T) u(X_T) \right| X_t = x \right] \ ,$$

with
* $u(c)$ the **utility function**, the "joy from spending"
* $\rho$ the **discount rate**, i.e. "the **personal** weight of the present", or a "measure of impatience"
* $B(T)$, the **bequest weight**, i.e. "the importance of leaving money behind"

Optimization problem can be solved using **continuous-time reinforcement learning**, see as an example [Math:Introduction to RL](https://basics2022.github.io/bbooks-math-miscellanea/ch/rl/intro.html), and [Statistics:RL](https://basics2022.github.io/bbooks-statistics/ch/ml/rl.html) (**todo**). Optimal solution $\pi_t^*$, $c_t^*$ is the fraction invested in the risky asset and consumption that maximises the **value function**, $V(x,t)$.

<!--
$$V(x,t) = \mathbb{E} \left[ \left. \int_{s=t}^{T} e^{- \rho (s-t)} u(c_s) \, ds + e^{-\rho(T-t)} B(T) u(X_T) \right| X_t = x \right] \ ,$$

i.e. the return of the choice defined as the cumulative discounted reward. Reward per unit time is the **utility function** $u(c_s)$, $\rho$ is a personal discount factor that weights present and future rewards, and $B(T)$ is a bequest function.
-->

```{admonition} Arguments of the value function
:class: dropdown

Value function may be written as a function of several arguments, that can be treated as
* independent variables, like:
  * the initial time $t$
  * the initial value of the wealth $x$
* parameters, like
  * the final time $T$
  * the discount rate $\rho$,
  * the parameters in wealth dynamics, e.g. $r$, $\mu$, $\sigma$
* functions and its parameters, like
  * the wealth fraction invested in the risky asset $\pi_t$
  * the utility function $u_t(c; \gamma)$, and the risk aversion therein $\gamma$
  * ...

For brevity, the value function is usually written as a function of the independent variables $x$, $t$ only, but it could be written with the explict dependence from parameters and functions,

$$V(x,t; \mathbf{p}, \mathbf{f}_t) \ .$$

```

For constant expected return and volatility of the assets, under the assumption of **constant relative risk aversion (CCRA)**, i.e. utility function $u(x) = \frac{x^{1-\gamma}}{1 - \gamma}$, it's possible to find an analytical solution with optimal fraction invested in the risky asset

$$\pi^* = \frac{\mu - r}{\gamma \sigma^2} \ ,$$

and consumption that's proportional to the wealth with a function of time $f(t)$

$$c_t = \frac{X_t}{f(t)} \ .$$

(fin-edu:investing:merton:solution)=
## Solution of the optimization problem

The solution of the optimization problem in the framework of **reinforcement learning** (or stochastic control?) may exploit the **principle of optimality**, getting the global optimization of the value function over time range $[t, T]$ from the local optimization over all the elementary time-steps $dt$ in the time range of interest.

<!--
(fin-edu:investing:merton:hjb)=
### Recursive relation and Hamilton-Jacobi-Bellman relation
-->

```{dropdown} Recursive relation and Hamilton-Jacobi-Bellman relation
:open:

Writing the value function $V(X_{t+dt}, t+dt)$ and expanding as a Taylor series up to the first order in $dt$, it's possible to find a **Hamilton-Jacobi-Bellman** equation from a recursive relation. Let the value function be

$$V(x,t) = \mathbb{E}_{W} \left[ \left. \int_{s=t}^{T} e^{- \rho (s-t)} u(c_s) \, ds + e^{-\rho(T-t)} B(T) u(X_T) \right| X_t = x \right] \ ,$$

**subject to** [wealth dynamics](fin-edu:investing:merton:wealth-dynamics), with initial condition $X_t = x$. This constraint allows to move the conditioned probability from $X_{t+dt}$ to $X_t = x$, in $V(X_{t+dt}, t+dt)$,

$$\begin{aligned}
  V(X_{t+dt}, t+ dt) 
  & = \mathbb{E}_W \left[ \left. \int_{s=t+dt}^{T} e^{- \rho (s-t-dt)} u(c_s) \, ds + e^{-\rho(T-t-dt)} B(T) u(X_T) \right| X_{t+dt} \right] = \\
  & = \mathbb{E}_W \left[ \left. \int_{s=t+dt}^{T} e^{- \rho (s-t-dt)} u(c_s) \, ds + e^{-\rho(T-t-dt)} B(T) u(X_T) \right| X_{t} = x \right] = \\
\end{aligned}$$

**todo** *Be careful about arguments of $V$ function.*

Now, let's evaluate $e^{-\rho t V(x,t)}$ for $t$ and $t+dt$,

$$\begin{aligned}
  & e^{-\rho  t    } V(X_t     , t   ) = \\
  & \qquad = \mathbb{E}_W \left[  \left. \int_{s=t   }^{T} e^{- \rho s} u(c_s) \, ds + e^{-\rho T} B(T) u(X_T) \right| X_{t   } \right] \\ \\
  & e^{-\rho (t+dt)} V(X_t+dX_t, t+dt) = \\
  & \qquad = \mathbb{E}_W \left[  \left. \int_{s=t+dt}^{T} e^{- \rho s} u(c_s) \, ds + e^{-\rho T} B(T) u(X_T) \right| X_{t}=x \right] = \\
  & \qquad = \mathbb{E}_W \left[  \left. \int_{s=t   }^{T} e^{- \rho s} u(c_s) \, ds + e^{-\rho T} B(T) u(X_T) \right| X_{t}=x \right]     
          - \mathbb{E}_W \left[  \left. \int_{s=t}^{t+dt} e^{- \rho s} u(c_s) \, ds                           \right| X_{t}=x \right]  \ .
\end{aligned}$$

and approximating the latter integral with the average value theorem,

$$e^{-\rho (t+dt)} V(X_t+dX_t, t+dt) = e^{-\rho t} V(X_t, t) - e^{-\rho t} u(c_t) \, dt \ ,$$

collecting the increment,

$$d \left( e^{-\rho t} V(X_t, t) \right) = - e^{-\rho t} u(c_t) \, dt$$

and using the rule of product of the differentials,

$$\rho V \, dt = d V + u(c_t) \, dt \ .$$ (eq:merton:dv-dt-equation)

```
<!--
### Taylor expansion
-->

```{dropdown} Taylor expansion
:open:

In this section, the expression of $dV$ as a function of $dt$ is found, and later introduced in equation {eq}`eq:merton:dv-dt-equation` to find a relation not involving $dt$.
Taylor expansion of value function $V(t,x)$ subject to [wealth dynamics](fin-edu:investing:merton:wealth-dynamics) - thus $dV(t, X_t)$ - providing the expression of $dX_t$, and up to $dt$ (and thus, to $dX_t^2 \sim dt$), valued with $x = X_t$, reads

**todo** *Add expectation value properly*

$$\begin{aligned}
  dV 
  & = \left. \left[ \partial_t V \, dt + \partial_x V \, dx + \dfrac{1}{2} \partial_{xx} V \, dx^2 + o(dt) \right] \right|_{x = X_t} = \\
  & = \partial_t V \, dt + \partial_x V \, dX_t + \dfrac{1}{2} \partial_{xx} v \, dX_t^2 + o(dt) = \\
  & = dt \left( \partial_t V + \partial_x V ( r_t + (\mu_t - r_t) \pi_t) X_t - \partial_x V \, c_t \right) + \mathbb{E} [ \partial_x V \, \pi_t \sigma_t X_t \, dW_t ] + \dfrac{1}{2} \partial_{xx} V \, \left( \pi_t \sigma_t X_t \right)^2 \, dt + o(dt) \ , \\
  & = dt \left( \partial_t V + \partial_x V ( r_t + (\mu_t - r_t) \pi_t) X_t - \partial_x V \, c_t \right) + \dfrac{1}{2} \partial_{xx} V \, \left( \pi_t \sigma_t X_t \right)^2 \, dt + o(dt) \ , \\
\end{aligned}$$ (eq:merton:dv-dt)

having used the wealth dynamics for $dX_t$, $\mathbb{E}[ dW_t] = 0$, and the expression at the first order of $dX_t^2 = \left( \pi_t \sigma_t X_t \right)^2 dW_t^2 + o(dt) = \left(  \pi_t \sigma_t X_t \right)^2 dt + o(dt)$.

<!--
Taking expected value,

$$d V = dt \, \mathbb{E}\left[ \partial_t v + \partial_x v ( r_t + (\mu_t - r_t) \pi_t) X_t - \partial_x v \, c_t + \dfrac{1}{2} \partial_{xx} v \, \left( \pi_t \sigma_t X_t \right)^2 \right] \ .$$
-->

```

<!--
### Recursive relation for optimal solution
-->

```{dropdown} Recursive relation for optimal solution
:open:

Introducing the expression {eq}`eq:merton:dv-dt` into the relation {eq}`eq:merton:dv-dt-equation` the following relation holds

$$\rho V = \left( \partial_t V + \partial_x V ( r_t + (\mu_t - r_t) \pi_t) X_t - \partial_x V \, c_t \right) + \partial_x V \, \pi_t \sigma_t X_t + \dfrac{1}{2} \partial_{xx} V \, \left( \pi_t \sigma_t X_t \right)^2 + u(c_t) \ ,$$ (eq:bellman:recursive)

at first order in $dt$. This condition holds for every $\pi_t$, $u_t$. **Optimality condition** requires that the value function is maximum, i.e.

$$\rho V^* = \max_{\pi_t, c_t} \left\{ \partial_t V^* + \partial_x V^* \left[ (\pi_t (\mu-r) + r) X_t - c_t  \right] + \dfrac{1}{2} \partial_{xx} V^* (\pi \sigma_t X_t)^2 + u(c_t) \right\} = \max_{\pi_t, c_t} \Phi$$

Explicitly writing independent variables and parameters, and keeping all the parameters constant except for the risky asset function $\pi_t$ and the consumption function $c_t$

$$\rho V^*(X_t, t; \mathbf{p}) := \rho V(X_t, t; \mathbf{p}; \pi_t^*, c_t^*) = \Phi(\pi_t=\pi_t^*, c_t=c_t^*; X_t, t, \mathbf{p}) \ ,$$

for a given set of parameters $\mathbf{p}$, initial time $t$, and wealth dynamics $X_t$, in $[t,T]$ subject to a given initial condition $X_t = x$.


```

<!--
### Optimality condition
-->

```{dropdown} Optimality condition
:open:

With $\pi_t$, $c_t$ as the only free parameters, zero gradient w.r.t. these variables (function evaluated at a time $t$ can be treated as a variable) is a necessary condition for local extreme points,

$$\begin{cases}
  0 = \partial_{\pi_t} \Phi(\pi^*_t, c^*_t) = (\mu-r) X_t \partial_x V^* + \partial_{xx} V^* \pi^*_t \left( \sigma_t X_t \right)^2 \\
  0 = \partial_{  c_t} \Phi(\pi^*_t, c^*_t) = - \partial_x V^* + \partial_{c_t} u(c^*_t) \\
\end{cases}$$

and thus

$$\begin{cases}
  \pi^*_t = -\dfrac{\partial_x V^*}{\partial_{xx} V^*} \dfrac{\mu - r}{X_t \sigma^2} \\
  0 = - \partial_x V^* + \partial_{c_t} u(c_t^*)
\end{cases}$$

**Remark.** Optimal value function $V^*$ is not a function of $\pi_t$, $c_t$, as it's the value function evaluated in the optimal fraction and consumption by definition.

```

```{dropdown} Necessary conditions on $\ u()\ $ for the Hessian to be definite negative

**todo**

```

<!--
### Example: utility function $u(x) = \frac{x^{1-\gamma}}{1-\gamma}$
-->

```{dropdown} CCRA assumption: utility function $\ u(x) = \frac{x^{1-\gamma}}{1-\gamma}$
:open:

With the expression $u(x) = \frac{x^{1-\gamma}}{1-\gamma}$, $\partial_{c_t} u(c_t) = c_t^{-\gamma}$, and thus

$$\begin{cases}
  \pi^*_t = -\dfrac{\partial_x V^*}{\partial_{xx} V^*} \dfrac{\mu - r}{X_t \sigma^2} \\
  c^*_t = \left( \partial_x V^* \right)^{-\frac{1}{\gamma}}
\end{cases}$$



```
<!--
### Example: value function $\ V^*(t, x) = f^{\gamma}(t) \frac{x^{1-\gamma}}{1 - \gamma}$
-->

```{dropdown} CCRA assumption: value function $\ V^*(t, x) = f^{\gamma}(t) \frac{x^{1-\gamma}}{1 - \gamma}$
:open:

With value function $V^*(x,t) = f^{\gamma}(t) \frac{x^{1-\gamma}}{1 - \gamma}$ and bequest function $B(T) = \varepsilon^T$, first and second order derivatives read

$$\begin{aligned}
 \partial_{x } V^* & = f^{\gamma} x^{-\gamma} \\
 \partial_{xx} V^* & = -\gamma f^{\gamma} x^{-\gamma-1} \\
\end{aligned}$$

so that the ratio $\frac{\partial_x V^*(X_t,t)}{\partial_{xx} V^*(X_t,t) X_t}$ reads

$$\frac{\partial_x V^*(X_t,t)}{\partial_{xx} V^*(X_t,t) X_t} = - \frac{1}{\gamma}$$

and the optimal ratio invested in the risky asset is

$$\pi_t^* = \frac{\mu - r}{\gamma \sigma^2} \ ,$$

and the optimal consumption is

$$c_t^* = \left( f^\gamma(t) X_t^{-\gamma} \right)^{-\frac{1}{\gamma}} = \frac{X_t}{f(t)} \ .$$

```

```{dropdown} Differential function for $\ f(t)$
:open:

Plugging the expressions of the optimal faction of the risky asset and the optimal consumption into the recursive Bellman relation {eq}`eq:bellman:recursive`, for the optimal value function $V^*$

$$\rho V^* = \left( \partial_t V^* + \partial_x V^* ( r_t + (\mu_t - r_t) \pi^*_t) X_t - \partial_x V^* \, c_t^* \right) + \dfrac{1}{2} \partial_{xx} V^* \, \left( \pi_t \sigma X_t \right)^2 + u(c^*_t) \ ,$$ (eq:bellman:recursive:v-star)

$$\begin{aligned}
0
& = -\rho f^{\gamma} \frac{X_t^{1-\gamma}}{1-\gamma} + \gamma \dot{f} f^{\gamma-1} \frac{X_t^{1-\gamma}}{1-\gamma} + f^{\gamma} X_t^{-\gamma}  X_t \left( r_t + ( \mu_t - r_t ) \frac{\mu-r}{\gamma \sigma^2} - \frac{1}{f(t)} \right) + \frac{1}{2} \sigma^2 X_t^2 \frac{(\mu-r)^2}{\gamma^2 \sigma^4} \left( -\gamma f^\gamma X_t^{-\gamma-1} \right) + \frac{1}{1-\gamma} \left( \frac{X_t}{f(t)} \right)^{1-\gamma} = \\
& = \left[ -\frac{\rho}{1-\gamma} + \left( r + \frac{(\mu-r)^2}{\gamma \sigma^2} - \frac{1}{f(t)} \right) - \frac{1}{2} \frac{(\mu-r)^2}{\gamma \sigma^2}\right] f + \dot{f} \frac{\gamma}{1-\gamma} + \frac{1}{1-\gamma} - 1 = \\
& = \left[ -\frac{\rho}{1-\gamma} + r + \frac{(\mu-r)^2}{2 \gamma \sigma^2} \right] f + \dot{f} \frac{\gamma}{1-\gamma} + \frac{\gamma}{1-\gamma} \ ,
\end{aligned}$$

i.e.

$$0 =\frac{1}{\gamma} \left[ - \rho + ( 1 - \gamma ) \left( r + \frac{(\mu-r)^2}{2\gamma \sigma^2} \right) \right] f(t) + \dot{f}(t) - 1 \ .$$

Thus, function $f(t)$ satisfies the ODE

$$\dot{f}(t) = \nu \, f(t) - 1$$

with final condition $f(T) = \varepsilon$, and

$$\nu = \dfrac{1}{\gamma} \left\{ \rho - (1 - \gamma) \left( \dfrac{(\mu-r)^2}{2 \sigma^2 \gamma} + r  \right)  \right\} \ .$$

The solution of the ODE reads

$$f(t) =
\begin{cases}
  \dfrac{1}{\nu} + \left( \varepsilon - \dfrac{1}{\nu} \right) e^{-\nu (T-t)} & \text{,} \quad \text{ if $\nu \ne 0$} \\
  T - t + \varepsilon                                                         & \text{,} \quad \text{ if $\nu =   0$} \\
\end{cases}$$


```

