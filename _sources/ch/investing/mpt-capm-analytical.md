(fin-edu:investing:mpt-capm:analytical)=
# MPT and CAPM: analytical solution

## MPT
Analytical solution of the MPT optimization problem for a **fully invested portfolio** with **no risk-free asset**

$$
\mathbf{w}^* = \text{argmin}_{\mathbf{w}} \sigma^2 \quad \text{s.t.} \quad
\begin{aligned}
  & \mathbf{w}^T \boldsymbol\mu = \overline{\mu} \\
  & \sum_{i=1}^N w_i = 1
\end{aligned}
$$

without any additional constraint. Using Lagrange multiplier method, the augmented objective function

$$\widetilde{J}(\mathbf{w}; a, b) = \frac{1}{2} \mathbf{w}^T \boldsymbol\sigma^2 \mathbf{w} - a ( \mathbf{w}^T \boldsymbol\mu - \mu ) - b ( \mathbf{w}^T \mathbf{1} - 1 )$$

and setting its gradient equal to zero gives the following system of equations

$$\begin{cases}
  \mathbf{0} & = \boldsymbol\sigma^2 \mathbf{w}^* - a \boldsymbol\mu - b\mathbf{1} \\
  0 & = \boldsymbol\mu^T  \mathbf{w}^* - \mu \\
  0 & = \mathbf{1}^T \mathbf{w}^* - 1 \ ,
\end{cases}$$

or using matrix formalism

$$\begin{bmatrix} \boldsymbol\sigma^2 & -\boldsymbol{\mu} & - \mathbf{1} \\ - \boldsymbol\mu^T & 0 & 0 \\ -\mathbf{1}^T & 0 & 0 \end{bmatrix} \begin{bmatrix} \mathbf{w}^* \\ a \\ b \end{bmatrix} = \begin{bmatrix} \mathbf{0} \\ -\mu \\ -1 \end{bmatrix}$$

Without any risk-free asset, the covariance matrix is non-singular, and thus invertible. (Formally) solving the first equation for $\mathbf{w}$,

$$\mathbf{w} = \boldsymbol\sigma^{-2} \boldsymbol\mu a + \boldsymbol\sigma^{-2} \mathbf{1} b \ ,$$

a system of 2 equations in 2 unknowns $a$, $b$ reads

$$\begin{bmatrix}
 \boldsymbol{\mu}^T \boldsymbol\sigma^{-2} \boldsymbol{\mu} & \boldsymbol{\mu}^T \boldsymbol\sigma^{-2} \mathbf{1}       \\
      \mathbf{1 }^T \boldsymbol\sigma^{-2} \boldsymbol{\mu} &       \mathbf{1}^T \boldsymbol\sigma^{-2} \mathbf{1}
\end{bmatrix}\begin{bmatrix} a \\ b \end{bmatrix} = \begin{bmatrix} \mu \\ 1 \end{bmatrix} \ .$$

and thus

$$\begin{aligned}
  \begin{bmatrix} a \\ b \end{bmatrix}
  & = \frac{1}{A_{11}A_{22} - 2 A_{12}} \begin{bmatrix} A_{22} & -A_{12} \\ - A_{12} & A_{11} \end{bmatrix} \begin{bmatrix} \mu \\ 1 \end{bmatrix} \\
  & = \frac{1}{\Delta} \left( \begin{bmatrix} A_{22} \\ -A_{12} \end{bmatrix} \mu + \begin{bmatrix} -A_{12} \\ A_{11} \end{bmatrix} \right) \ .
\end{aligned}$$

Thus, the optimal asset allocation is a 1-degree function of $\mu$,

$$\mathbf{w}^* = \mathbf{w}_0 + \mathbf{w}_{/\mu} \mu \ .$$

and its variance is a 2-degree function of $\mu$,

$$\begin{aligned}
  \sigma^{2 *} 
  & = \mathbf{w}^{* T} \boldsymbol\sigma^2 \mathbf{w}^* = \sigma^2_{0} + \sigma^2_1 \mu + \sigma^2_2 \mu^2 = \\
  & = \left( a \boldsymbol\mu^T + b \mathbf{1}^T \right) \boldsymbol\sigma^{-2} \, \underbrace{ \boldsymbol\sigma^2 \, \boldsymbol\sigma^{-2} }_{ =  \mathbf{I}} \left( \boldsymbol\mu a + \mathbf{1} b \right) = \\
  & = a^2 \boldsymbol\mu^T \boldsymbol\sigma^{-2} \boldsymbol\mu + 2 a b \mathbf{1}^T \boldsymbol\sigma^2 \boldsymbol\mu + b^2 \mathbf{1}^T \boldsymbol\sigma^{-2} \mathbf{1} = \\
  & = \left( \frac{1}{\Delta} \left( A_{22} \mu - A_{12}  \right)  \right)^2 A_{11} + 2 \frac{1}{\Delta^2} \left(  A_{22}\mu - A_{12} \right) \frac{1}{\Delta} \left( -A_{12} \mu + A_{11} \right) A_{12} + \left(  \frac{1}{\Delta} \left( -A_{12} \mu + A_{11}  \right) \right)^2 A_{22} = \\
  & = \frac{1}{\Delta^2} \left( \mu^2 \left( A_{22}^2 A_{11} - 2 A_{22} A_{12}^2 + A_{12}^2 A_{22} \right) + \mu \cdot 2 \left(- A_{11}A_{22}A_{12} + A_{22} A_{11} A_{12} + A_{12}^3 - A_{11}A_{22}A_{12} \right) + \left( A_{12}^2 A_{11} - 2 A_{12}^2 A_{11} + A_{11}^2 A_{22}  \right) \right) = \\
  & = \frac{1}{\Delta^2} \left[ \mu^2 A_{22} \left( A_{11} A_{22} - A_{12} \right) - 2 \mu A_{12} \left( A_{11} A_{22} - A_{12}^2 \right) + A_{11} \left( A_{11} A_{22} - A_{12}^2 \right) \right] = \\
  & = \frac{1}{\Delta} \left( \mu^2 A_{22} - 2 \mu A_{12} + A_{11} \right) = \\
  & = \begin{bmatrix} \mu & 1 \end{bmatrix} \mathbf{A}^{-1} \begin{bmatrix} \mu \\ 1 \end{bmatrix} \ .
\end{aligned}$$

As the matrix $\mathbf{A}$ is definite positive (its inverse is definite positive as well?), it follows that $\sigma^2 > 0$ for any value of $\mu$, as expected for the value of a variance.

**Some analytic geometry.** The function 

$$\begin{aligned}
  \text{Var}[r](\mu)
  & = \frac{1}{\Delta} \left( A_{22} \mu^2 - 2 A_{12} \mu + A_{11} \right) = \\
  & = \frac{A_{22}}{\Delta} \left( \mu   - \frac{A_{12}}{A_{22}} \right)^2 + \frac{A_{11}}{\Delta} - \frac{A_{12}^2}{A_{22} \, \Delta} = \\
  & = \frac{A_{22}}{\Delta} \left( \mu   - \frac{A_{12}}{A_{22}} \right)^2 + \frac{1}{A_{22}}  \ .
\end{aligned}$$

is the function of a parabola, with vertex in 

$$\begin{aligned}
  \mu_v & = \frac{A_{12}}{A_{22}} \\
  \text{Var}[r]_v & = \text{Var}[r](\mu_v) = \frac{1}{\Delta} \left( \frac{-A_{12}^2 + A_{11}A_{22}}{A_{22}} \right) = \frac{1}{A_{22}} \ .
\end{aligned}$$

Using $\sigma$ as an independent coordinate (and not $\text{Var}[r] = \sigma^2$)...

```{dropdown} Properties of matrix $\ \mathbf{A}$

Is it positive definite? Covariance matrix is positive matrix, so for $\forall \mathbf{v}$

$$ 0 < \mathbf{v} \boldsymbol\sigma^2 \mathbf{v} \ ,$$

and choosing $\mathbf{v} = \begin{bmatrix} \boldsymbol\mu & \mathbf{1} \end{bmatrix} \begin{bmatrix} a \\ b \end{bmatrix}$, for $\forall a, b$, it immediately follows

$$\begin{aligned}
  0 
  & < \mathbf{v} \boldsymbol\sigma^2 \mathbf{v} = \\
      & = \begin{bmatrix} a & b \end{bmatrix} \begin{bmatrix} \boldsymbol\mu^T \\ \mathbf{1}^T \end{bmatrix} \boldsymbol\sigma^2 \begin{bmatrix} \boldsymbol\mu & \mathbf{1} \end{bmatrix} \begin{bmatrix} a & b \end{bmatrix} = \\
      & = \begin{bmatrix} a & b \end{bmatrix} \begin{bmatrix} \boldsymbol\mu^T \boldsymbol\sigma^2 \boldsymbol\mu & \boldsymbol\mu^T \boldsymbol\sigma^2 \mathbf{1} \\  \mathbf{1}^T \boldsymbol\sigma^2 \boldsymbol\mu & \mathbf{1}^T \boldsymbol\sigma^2 \mathbf{1}\end{bmatrix} \begin{bmatrix} a & b \end{bmatrix} \ ,
    \end{aligned}$$

and thus matrix $\mathbf{A}$ is definite positive.

```

## CAPM
Analytical solution of the MPT-CAPM optimization problem, with a risk-free asset. If a risk-free asset exists, the covariance matrix is singular. However, the risk-free asset can be partitioned from the risky assets, so that the covariance matrix of the return of the risky asset is non-singular. The problem becomes

$$( \mathbf{w}, w_0 )^* = \text{argmin}_{()} \sigma^2 \quad \text{s.t} \quad \dots $$

...

$$
\begin{bmatrix}
  \boldsymbol\sigma^2 & \mathbf{0} &  -\boldsymbol{\mu} & - \mathbf{1} \\
  \mathbf{0}^T & 0 & -\mu_0 & -1 \\
  - \boldsymbol\mu^T & -\mu_0 & 0 & 0 \\
  -\mathbf{1}^T & -1 & 0 & 0
\end{bmatrix}
\begin{bmatrix} \mathbf{w}^* \\ w_0^* \\ a \\ b \end{bmatrix} =
\begin{bmatrix} \mathbf{0} \\ 0 \\ -\mu \\ -1 \end{bmatrix}
$$


From the second and the fourth equation,

$$\begin{aligned}
  b & = - \mu_0 a \\
  w^*_0 & = - \mathbf{1}^T \mathbf{w}^* + 1
\end{aligned}$$

and thus

$$
\begin{bmatrix}
  \boldsymbol\sigma^2 & -\boldsymbol{\mu} + \mu_0 \mathbf{1} \\
  - \boldsymbol\mu^T + \mu_0 \mathbf{1}^T & 0 \\
\end{bmatrix}
\begin{bmatrix} \mathbf{w}^* \\ a \end{bmatrix} =
\begin{bmatrix} \mathbf{0} \\ - \left( \mu - \mu_0 \right) \end{bmatrix}
$$

whose solution reads

$$\begin{aligned}
  a & = \frac{\mu_e}{\boldsymbol\mu_e^T \boldsymbol\sigma^{-2} \boldsymbol\mu_e} \\
  \mathbf{w}^* & = \frac{\mu_e \boldsymbol\sigma^{-2} \boldsymbol\mu_e}{ \boldsymbol\mu_e^T \boldsymbol\sigma^{-2} \boldsymbol\mu_e }
\end{aligned}$$

and the relationship between the variance and the expected value of the optimal portfolios,

$$
  \sigma^2 = \frac{\mu_e^2}{ \boldsymbol\mu_e^T \boldsymbol\sigma^{-2} \boldsymbol\mu_e }
$$

or the linear relation between the standard deviation of the portoflio $\sigma$ and the excess return $\mu_e$ of the portfolio w.r.t. the risk-free asset,

$$\sigma = \frac{\mu_e}{\sqrt{ \boldsymbol\mu_e^T \boldsymbol\sigma^{-2} \boldsymbol\mu_e }} \ .$$

```{dropdown} Solution of the linear system - details

$$\mathbf{w}^* = \boldsymbol\sigma^{-2} \left( \boldsymbol\mu - \mu_0 \mathbf{1} \right) a \ ,$$

$$\begin{aligned}
  \mu-\mu_0 
  & = \left( \boldsymbol\mu - \mu_0 \mathbf{1} \right)^T \mathbf{w}^* = \\
  & = \left( \boldsymbol\mu - \mu_0 \mathbf{1} \right)^T \boldsymbol\sigma^{-2} \left( \boldsymbol\mu - \mu_0 \mathbf{1} \right) a \ ,
\end{aligned}$$

$$a = \frac{\mu_e}{\boldsymbol\mu_e^T \boldsymbol\sigma^{-2} \boldsymbol\mu_e} \ ,$$

and thus

$$\mathbf{w}^* = \frac{\mu_e \boldsymbol\sigma^{-2} \boldsymbol\mu_e}{\boldsymbol\mu_e^T \boldsymbol\sigma^{-2} \boldsymbol\mu_e} \ .$$

Eventually, the variance of the portfolio reads

$$\begin{aligned}
  \sigma^2
  & = \mathbf{w}^{* \ T} \boldsymbol\sigma^{2} \mathbf{w} = \\
  & = \mu_e^2 \dfrac{ \boldsymbol\mu_e^T \boldsymbol\sigma^{-2} \boldsymbol\sigma^{2} \boldsymbol\sigma^{-2} \boldsymbol\mu_e}{\left( \boldsymbol\mu_e^T \boldsymbol\sigma^{-2} \boldsymbol\mu_e \right)^2} = \\
  & = \frac{\mu_e^2}{ \boldsymbol\mu_e^T \boldsymbol\sigma^{-2} \boldsymbol\mu_e } \ ,
\end{aligned}$$

with $\mu_e := \mu - \mu_0$ the excess desired return of the portfolio w.r.t. the risk-free asset, and $\boldsymbol\mu_e := \boldsymbol\mu - \mu_0 \mathbf{1}$ the vector of the excess returns of each risky asset w.r.t. the risk-free asset. Taking the square root of the last relation, a 1-degree function relates the standard deviation and the return of the portfolio,

$$\sigma = \frac{\mu_e}{\sqrt{ \boldsymbol\mu_e^T \boldsymbol\sigma^{-2} \boldsymbol\mu_e }} \ .$$

```

**Tangency condition** as a maximization of a measure of [risk-adjusted return](fin-edu:principles:rr), namely **Sharpe ratio** comparing the excess return and the variance of the portfolio w.r.t. a risk-free (zero variance) asset $(\cdot)_0$ used as a benchmark $(\cdot)_b$

$$S := \frac{\mathbb{E}[ r - r_b ]}{\sqrt{\text{Var}[ r - r_b ]}} = \frac{\mathbf{w}^{T} \boldsymbol\mu - \mu_0}{\sqrt{\mathbf{w}^{T} \boldsymbol\sigma^2 \mathbf{w}}}$$

as the variance reads

$$\begin{aligned}
  \text{Var}[ r - r_0 ]
  & = \dots \\
\end{aligned}$$

```{dropdown} Tangency condition between optimal portfolio lines w/ and w/o risk-free asset
:open:

W/o risk-free asset

$$\sigma_{r}(\mu) = \sqrt{ \frac{A_{22} \mu^2 - 2 \mu A_{12} + A_{11}}{\Delta} } \ ,$$

with $A_{22} = \mathbf{1}^T \boldsymbol\sigma^{-2} \mathbf{1}$, $\mathbf{A}_{11} = \boldsymbol\mu^T \boldsymbol\sigma^{-2} \boldsymbol\mu$, $A_{12} = \boldsymbol\mu^T \boldsymbol\sigma^{-2} \mathbf{1}$, and $\Delta = A_{11} A_{22} - A_{12}$

W/ risk-free asset

$$\sigma_f(\mu) = \frac{\mu - \mu_0}{\sqrt{ \left( \boldsymbol\mu - \mu_0 \mathbf{1} \right)^T \boldsymbol\sigma^{-2} \left( \boldsymbol\mu - \mu_0 \mathbf{1} \right) }} \ .$$

Tangency condition

$$\begin{aligned}
  & \sigma_{r}(\overline{\mu}) = \sigma_{f}(\overline{\mu}) \\
  & \sigma'_{r}(\overline{\mu}) = \sigma'_{f}(\overline{\mu}) \\
\end{aligned}$$

or with the variance,

...

$$
 0 = \mu^2 \left( \frac{A_{22}}{\Delta} - \frac{1      }{\boldsymbol\mu_e^T \boldsymbol\sigma^{-2} \boldsymbol\mu_e} \right) 
   -2\mu   \left( \frac{A_{12}}{\Delta} - \frac{\mu_0  }{\boldsymbol\mu_e^T \boldsymbol\sigma^{-2} \boldsymbol\mu_e} \right)
   +       \left( \frac{A_{11}}{\Delta} - \frac{\mu_0^2}{\boldsymbol\mu_e^T \boldsymbol\sigma^{-2} \boldsymbol\mu_e} \right)
$$


```


