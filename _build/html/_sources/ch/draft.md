(fin-edu:draft)=
# 1-Page Draft

## Inflation and the need for investing

In contemporary economic systems, institutions targets a low non-zero inflation, usually $2\%$. Thus, the protection fo real valu of money is the bare minimum goal of investing.

Thus, need for investing
- starting from personal goals and constraints (saving rate, risk tolerance,...)
- knowing the available assets and their properties, e.g. 1-period &mdash; usually 1-year &mdash; return probability distribution
- knowing the fundamentals of composition of returns, and math facts about multi-period performances

First, analysis of 1-asset over 1-period, and eventually multi-asset over many periods of time.

## Return, risk, and risk-adjusted return

### Single asset, single period

The single period return of an asset $X$ over period $i$ from time $i-1$ and $i$ is defined as

$$r_t := \dfrac{X_{t} - X_{t-1}}{X_{t-1}} = \frac{X_t}{X_{t-1}} - 1 \ ,$$

being $X_t$ the value of the asset $X$ at time $t$. A 1-period return of an asset $X$ can be usually modelled as a random variable with probability distribution $p_t(r)$.

### Single asset, multiple periods

The return compounds over many periods,

$$X_t = ( 1 + r_t ) X_{t-1} = ( 1 + r_t ) \dots ( 1 + r_1 ) X_0 = \prod_{i=1}^{t} ( 1 + r_i ) X_0 = \prod_{i=1}^t \frac{X_{i}}{X_{i-1}} \ .$$

The compund average return (usually called *Compound Annual Growth Rate*, if the reference period is a year) can be defined as the constant return $r_i = r$ for all $i = 1:t$ producing the actual result, and thus

$$X_t = \left( 1 + r \right)^t X_0 \ ,$$

or 

$$r = \left(\frac{X_t}{X_0}\right)^{\frac{1}{t}} - 1 \ .$$

```{dropdown} Log-return.

$$\begin{aligned}
  \log \frac{X_t}{X_0} 
  & = \sum_{i=1}^t \log \frac{X_{i}}{X_{i-1}} = \sum_i \log \left( 1 + r_i \right) \\
  & = t \log ( 1 + r ) \ ,
\end{aligned}$$

so that 

$$\log ( 1 + r ) = \frac{1}{t} \sum_i \log \left( 1 + r_i \right) \ .$$

```

```{dropdown} Probability distribution, expected value and variance

Skewness of the probability density of the result $\frac{X_t}{X_0}$, typically producing *median value* $lt$ *expected value*. Under some assumptions (...) the expected value of the log-return has expected value that is smaller than the 1-period expected return due to dispersion (**volatility drag**)

$$\mathbb{E}[ r ] \sim \mathbb{E}[ r_i ] - \frac{\text{Var}[r_i]}{2} \ ,$$

and variance

$$\text{Var}[ r ] \sim \frac{\text{Var}[r_i]}{t} \ .$$


```

### Multiple assets, single period

Given a portfolio  with many assets of value $X_{t-1}$ at time $t-1$, with weights 

$$w_{i,t-1} := \frac{X_{i,t-1}}{X_{t-1}} = \frac{X_{i,t-1}}{\sum_{i} X_{i,t-1}} \ ,$$

and constant composition in time until $t$, the value of the final portfolio becomes

$$X_{t} = \sum_{i} X_{i,t} = \sum_i ( 1 + r_{i,t} ) X_{i,t-1} = \sum_i r_{i,t} X_{i,t-1} + X_{t-1}, $$

and the return

$$r_t := \frac{X_t}{X_{t-1}} - 1 = \dfrac{\sum_i r_{i,t} X_{i,t-1}}{X_{t-1}} = \sum_i r_{i,t} w_{i,t-1} = \mathbf{w}_{t-1}^T \mathbf{r}_t \ .$$

The return of the assets $\mathbf{r}$ can be modelled as a (vector) random variable. The expected value and the variance of the 1-period return of the portfolio with weights $\mathbf{w}$ read

$$\mu_r := \mathbb{E}[ r ] = \mathbb{E}\left[ \mathbf{w}^T \mathbf{r} \right] = \mathbf{w}^T \mathbb{E}\left[ \mathbf{r} \right] = \mathbf{w}^T \boldsymbol\mu_{\mathbf{r}} \ ,$$

and

$$\begin{aligned}
 \sigma^2_r := \text{Var}[ r ]
  & = \mathbb{E}\left[ ( r - \mathbb{E}[r] )^2  \right] = \\
  & = \mathbb{E}\left[ \mathbf{w}^T ( \mathbf{r} - \boldsymbol\mu ) ( \mathbf{r} - \boldsymbol\mu )^T \mathbf{w}  \right] = \\
  & = \mathbf{w}^T \boldsymbol\sigma^2_{\mathbf{r}} \mathbf{w} \ .
\end{aligned}$$

### Multiple assets, multiple periods

**Without rebalancing.** No action is taken. Every individual asset of the portfolio evolves indipendently. At time $0$

$$X_0 = \sum_i X_{i,0} = \sum_i w_{i,0} X_0 \ .$$

At successive times,

$$X_t = \sum_i X_{i,t} = \sum_i X_{i,0} \prod_{\tau=1}^{t} ( 1 + r_{i,\tau} ) = X_0 \sum_i w_{i,0} \prod_{\tau=1}^{t} ( 1 + r_{i,\tau} ) \ .$$

**With rebalancing (assuming no cost...).** At the end of each period, weights of individual assets are set back to the original desired value. Following this strategy, under the assumption of stationariety, the 1-period performance of the portfolio is constant, with 1-period return

$$r_1 = \mathbf{w}^T \mathbf{r} \ ,$$

and expected value and variance

$$
\mu_{(1)} = \mathbf{w}^T \boldsymbol{\mu}_{\mathbf{r}}
\quad , \quad
\sigma_{(1)}^2 = \mathbf{w}^T \boldsymbol\sigma^2_{\mathbf{r}} \mathbf{w} \ .
$$

Under the assumption of "small" 1-period returns, the geometric average return reads

$$\overline{r} \sim \mathscr{N} \left( \mu_{(1)} - \dfrac{\sigma_{(1)}^2}{2}, \dfrac{\sigma_{(1)}^2}{N} \right) \ .$$

```{prf:example} Shannon demon and the rebalancing premium: 2-asset portfolio

A 2-asset portfolio is determined by the weights $\mathbf{w} = ( w_1, w_2 )$ of the two assets. One-period return of the 2 assets is modeleld as a multidimensional random variable $\mathbf{r}$, whose expected value and variance read

$$\boldsymbol\mu_{(1)} = \mathbb{E}[ \mathbf{r} ] = \begin{bmatrix} \mu_1 \\ \mu_2 \end{bmatrix}$$

and

$$\boldsymbol\sigma^2_{(1)} = \mathbb{E}[ \Delta \mathbf{r} \Delta \mathbf{r}^T ] = \begin{bmatrix} \sigma^2_{11} & \sigma^2_{12} \\ \sigma^2_{12} & \sigma^2_{22} \end{bmatrix} = \begin{bmatrix} \sigma^2_1 & \rho_{12} \sigma_1 \sigma_2  \\ \rho_{12} \sigma_1 \sigma_2 & \sigma_2^2 \end{bmatrix} \ .$$

Under certain conditions, the expected value of the multi-period return of the diversified and rebalanced portfolio may exceed the largest expected value of multi-period returns from individual assets, i.e.

$$\mu - \dfrac{\sigma^2}{2} > \mu_i - \dfrac{\sigma_i^2}{2} \ .$$

```

```{dropdown} Some algebra
:open:

Let's evaluate the conditions for $i = 1$

$$\begin{aligned}
  0
  & < w_1 \mu_1 + w_2 \mu_2 - \dfrac{w_1^2 \sigma_1^2 + 2 \rho_{12} \sigma_1 \sigma_2 w_1 w_2 + w_2^2 \sigma_2^2}{2} - \mu_1 + \dfrac{\sigma_1^2}{2} = \\
  & = c(w_1, w_2)
\end{aligned}$$

Given the properties $\mu_i$, $\sigma_i$, $\rho_{12}$, the equation $c(w_1, w_2) = 0$ is the equation of a conic section in the plane $w_1-w_2$.


```


---

At the end of any period, weights are set back to the desired fractions. At time $0$

$$X_0 = \sum_i X_{i,0} = \sum_{i} w_{i} X_0 \ ,$$

At time $1$ before rebalancing

$$X_1 = \sum_i X_{i,1}^- = \sum_i X_{i,0} ( 1 + r_{i,0} ) = X_0 \left( 1 + \sum_i w_i r_{i,0} \right) \ .$$

At time $1$ after rebalancing

$$X_1 = \sum_i X_{i,1}^+ = \sum_i w_i X_1 $$

At time $2$ before rebalancing

$$X_2 = \sum_i X_{i,1}^+ ( 1 + r_{i,1} ) = X_1 \sum_i w_i ( 1 + r_{i,1} ) \ . $$

and thus

$$\frac{X_t}{X_0} = \prod_{\tau=1}^{t} \left( 1 + \mathbf{w}^T \mathbf{r}_{\tau} \right) \ .$$

The log-return comes from

$$\begin{aligned}
\log \frac{X_t}{X_0}
 & = \sum_{\tau=1}^{t} \log ( 1 + \mathbf{w}^T \mathbf{r}_{\tau} ) = \\
 &\sim \sum_{\tau=1}^{t} \left( 1 + \mathbf{w}^T \mathbf{r}_{\tau} + \dfrac{1}{2} \mathbf{w}^T \mathbf{r}_{\tau} \mathbf{r}_{\tau}^T \mathbf{w}  \right)
\end{aligned}$$

The expected value and the variance read...








