(fin-edu:investing:mpt)=
# Modern Portfolio Theory

Modern portfolio theory results in a strategy of asset allocation minimizing portfolio risk - measured as volatility - for a given value of the portfolio expected return.

```{dropdown} Asset Modeling
:open:

A set of $N$ assets is available. Their return (over a defined period)[^return-estimation] is represented by a multi-dimensional random variable, $\mathbf{X}$, with expected value and variance

$$\begin{aligned}
  \overline{\mathbf{X}} & := \mathbb{E}\left[ \mathbf{X} \right] \\
  \boldsymbol{\sigma}^2 & := \mathbb{E}\left[ \Delta \mathbf{X} \, \Delta \mathbf{X}^T \right] \\
\end{aligned}$$

with $\Delta \mathbf{X} := \mathbf{X} - \overline{\mathbf{X}}$.

[^return-estimation]: How to estimate asset return, at least in terms of expected value and variance? And how to estimate correlation of the random variables?
```

```{dropdown} Asset allocation. Constraints
:open:

A portfolio, without short or leverage positions on these assets, can be represented with the set of weights (proportion) of the assets $\mathbf{w}$, with 

$$\begin{aligned}
  & \sum_n w_n = 1 \\
  & 0 \le w_n \le 1 \quad , \qquad \forall n = 1:N  \\
\end{aligned}$$
```

```{dropdown} Portfolio return
:open:

Portfolio return is

$$\mathbf{X} = \mathbf{w}^T \mathbf{X} \ ,$$

From linearity, its expected value reads

$$\begin{aligned}
  \overline{X} = \mathbb{E} \left[ X \right] =  \mathbb{E} \left[ \mathbf{w}^T \mathbf{X} \right] = \mathbf{w}^T \, \overline{\mathbf{X}} 
\end{aligned}$$

and its variance

$$\begin{aligned}
  \sigma^2
  & = \mathbb{E} \left[ (X-\overline{X})^2 \right]      
    = \mathbb{E} \left[ \mathbf{w}^T \left( \mathbf{X} - \overline{\mathbf{X}} \right)\left( \mathbf{X} - \overline{\mathbf{X}} \right)^T \mathbf{w}  \right] = \\
  & = \mathbf{w}^T \mathbb{E} \left[ \Delta \mathbf{X} \, \Delta \mathbf{X}^T \right] \mathbf{w}
    = \mathbf{w}^T \boldsymbol{\sigma}^2 \, \mathbf{w}
\end{aligned}$$
```

```{prf:example} Properties of variance matrix
:class: dropdown

Covariance matrix is symmetric definite positive. Symmetry readily follows

$$\sigma_{ij} = \mathbb{E}\left[ \Delta X_i \, \Delta X_j \right]$$

The matrix is definite positive as

...

```

```{dropdown} Modern Portfolio Theory, as a constrained optimization problem
:open:

Modern portfolio theory has its own "optimal" asset allocation $\mathbf{w}^*\left(\overline{X}\right)$ - with the desired expected return as the parameter, fixed during the optimization - as the asset allocation for which

$$
  \min_{\mathbf{w}} \sigma^2 \quad \text{s.t.}
\begin{aligned}
  & \qquad \mathbf{w}^T \, \overline{\mathbf{X}} = \overline{X} \\
  & \qquad \mathbf{w}^T \, \mathbf{1} = 1 \\
  & \qquad 0 \le w_i \le 1
\end{aligned}$$

```





