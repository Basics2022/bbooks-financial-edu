(fin-edu:principles)=
# Principles of investing

Investing is a core part of personal financial management—it's how individuals navigate uncertainty to meet their financial goals under real-world constraints. The most basic objective is to preserve the real value of wealth, protecting it against [inflation](fin-edu:inflation); more ambitious goals include growing capital to fund retirement, education, or other life plans.

Sound investing requires understanding [return](fin-edu:principles:return) and [risk](fin-edu:principles:risk) of available assets, and the fundamental [R/R trade off](fin-edu:principles:rr). It also demands attention to **constraints** such as *liquidity* needs, *time horizon*, *acceptable volatility*, and *risk tolerance*. One of the main principle is [diversification](fin-edu:principles:diversification) - which can reduce risk and, in some cases, enhance returns. <!--Key tools include [diversification](fin-edu:principles:diversification) - which can reduce risk and, in some cases, enhance returns - and the disciplined use of strategies like recurring investment plans (PIC/PAC) and long-term portfolio management.
-->

This section introduces the core concepts needed to build a robust investment strategy: how [compound returns](fin-edu:principles:time:compunding) shape long-term growth, how [volatility drag](fin-edu:principles:time:volatility-drag) reduces expected performance, and how a clear, principle-based approaches - like [rebalancing](fin-edu:principles:rebalancing) - may improve performance under uncertainties.

Given its set of constraints, an informed and intelligent agent, see [Portfolio construction](fin-edu:principles:asset-allocation) would take actions that try to maximise return for a given accepted risk, or minimize risk for a given desired return: this behavior can be summarized in choosing actions on a *Pareto front*, i.e. within the set of all Pareto efficient solutions.

```{dropdown} Sections

| **Section**                                                          | **Key Concepts**                    | 
| -------------------------------------------------------------------- | ----------------------------------- | 
| **1. [Return](fin-edu:principles:return)**                           |                                     | 
| **2. [Risk](fin-edu:principles:risk)**                               |                                     | 
| **3. [Risk-Return Trade-Off](fin-edu:principles:rr)**                |                                     | 
| **4. [Diversification](fin-edu:principles:diversification)**         |                                     | 
| **5. [Portfolio Construction](fin-edu:principles:asset-allocation)** |                                     | 
| **6. [Time and Compounding](fin-edu:principles:time)**               | Compounding and volatility drag     | 
| **7. [Disciplined Investing](fin-edu:principles:investing)**         | PIC/PAC, rebalancing,...            |
```

(fin-edu:principles:return)=
## Return

Return is the reward for investing. It can come from **capital gain** (price increase of assets bought), or **periodic cashflows**, like interest (from bonds), or dividends (from stocks). Some assets produce predictable return (either nominal, or real), other assets have less predictable returns. Any asset has some level of uncertainty, or [risk](fin-edu:principles:rr)[^risk-rare-events]. 

[^risk-rare-events]: Even the most safe assets could undergo some (really) **rare**, but usually (really) **catastrophic events**. Just as an example, it's hard to imagine what could happen even to bonds issued by the most (perceived and priced) safe government or institution, in case of its participation in a war.

Most returns are quoted on a **per-period** basis - usually annually - and expressed as the percentage of the reward over the initial amount of the investment.

```{prf:example} 1-period returns
An amount of $1000$€ in saving account returning $2\%$ per year, returns $0.02 \cdot 1000\text{€} = 20$€ at the end of the year, so that the amount in the saving account becomes $1000\text{€} \cdot 1.02 = 1020\text{€}$. Usually some [costs](fin-edu:principles:return:costs) must be also considered.

...

```

```{prf:example} 1-period return of equity investment
:class: dropdown

...given costs, dividends, taxes, buying and selling prices, evaluate return...

```

For a many-year investment, single-period returns [**compound**](fin-edu:principles:time:compunding) over time.

<!--
    Example: A savings account may return 2% per year. A stock portfolio might average 7% per year, but one year it could return –10%, another year +20%. That variability is why understanding risk is essential.
-->

(fin-edu:principles:return:costs)=
### Costs

While return are uncertain, at least to a certain level, usually costs - fees, expenses, taxes - or part of them, are certain. With equal other conditions, the intelligent investor should reduce costs (known), as higher costs reduce returns w/o changing the level of risk.

(fin-edu:principles:risk)=
## Risk

Risk measures uncertainty and its effects, combining probability of events and consequences of specific events. *All the assets have some systematic and some specific risks*
.
<!-- Some risks are systematic (like market crashes); others are specific (like a company going bankrupt).-->
Key measures (*should give info about magnitude, frequency/probability, and duration*) include:
- standard deviation or **volatility**: how much returns may deviate from their expected value),
- max loss (usually 100% can't be neglected for catastrophic although rare events), value at risk (VaR, max loss with a given probability), drawdown (maximum peak-to-trough loss)
- time-to-recover (time to recover drawdowns, in a temporal perspective)

Usually, risk metrics measure uncertainty, without discerning from positive and negative events: these metrics perceive a higher-than-expected return as a risk as well. Some metrics instead, see *Sortino ratio* in [risk-return](fin-edu:principles:rr) section, aims at quantifying only negative events as risk.

```{prf:example} Value at Risk

A 1-year 5% VaR of $1000\text{€}$ of an investment it means that there's 5% probability of losing at least $1000\text{€}$ in a year with that investment.

```


(fin-edu:principles:rr)=
## Risk-Return Trade Off

```{admonition} "There's no free lunch"
:class: tip

Higher expected returns usually come with higher risk.
```

```{admonition} ...but high risk doesn't imply high expected return
:class: warning

Very stupid actions usually implies poor return with high risk. Just as an example, playing Russian roulette for fun implies an expected return worse than an alternative "do-nothing and have an ice-cream instead" scenario (at least, if your goal is not to kill yourself, and your return function does not positively weight this outcome) with higher uncertainty on the final status of your health.

Sometimes the same could happen if one plays doing trading with some random meme-stocks or shit-coins.

```


**Risk-adjusted return** provides an indication of the expected return per unit of risk. Common metrics are:
- **Sharpe ratio**, comparing excess return and volatility compared with a "risk-free" asset - or a benchmark

  $$S := \dfrac{\mathbb{E}[R-R_b]}{\sqrt{\text{var}[R-R_b]}}$$

- **Sortino ratio**
  
  $$So := \dfrac{\mathbb{E}[R] - T}{\text{DR}} \ ,$$

  with $T$ target return, and $\text{DR}$ the downside deviation, i.e. the deviation w.r.t the target return evaluated only for returns $r$ lower than the target return $T$

  $$\text{DR}^2 = \int_{r=-\infty}^{T} (T-r)^2 \, f(r) \, dr \ ,$$

  being $f(r)$ the probability density function of the (continuous) random variable $R$ representing return


```{prf:example}

```

(fin-edu:principles:diversification)=
## Diversification

Diversification spreads risk across different investments so no single event can ruin your portfolio. Diversification works well with assets that are not - or at least they're loosely - correlated: in this case, diversification could increase return per unit of risk.

(fin-edu:principles:asset-allocation)=
## Portfolio Construction


(fin-edu:principles:time)=
## Time

(fin-edu:principles:time:compunding)=
### Compound Return

(fin-edu:principles:time:volatility-drag)=
#### Volatility Drag

**todo**
- *"Time and risk?" Listen to The Logic of Risk*

(fin-edu:principles:investing)=
## Disciplined Investing

(fin-edu:principles:rebalancing)=
### Rebalancing


<!--
| **Section**                   | **Focus**                                                          | **Key Concepts**                                                   | **Core Takeaways**                                                                       |
| ----------------------------- | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ---------------------------------------------------------------------------------------- |
| **0. Introduction**           | Framing investing as goal-driven decision-making under constraints | Goals, constraints, uncertainty, real return                       | Investing is about making rational choices to reach personal goals in an uncertain world |
| **1. Understanding Return**   | What you earn from investing                                       | Nominal vs. real return, capital gains, dividends, expected return | Return is the reward for investing; understanding sources helps set realistic goals      |
| **2. Understanding Risk**     | What can go wrong and why                                          | Market risk, credit risk, liquidity, volatility, drawdown          | Risk is the variability of outcomes; measuring and understanding it is essential         |
| **3. Risk-Return Trade-Off**  | Balancing reward and uncertainty                                   | Sharpe ratio, efficient trade-offs                                 | Higher return = higher risk; what matters is return *per unit* of risk                   |
| **4. Time and Compounding**   | How time affects outcomes                                          | Compound return, volatility drag, geometric vs. arithmetic return  | Time magnifies effects—both positive (compounding) and negative (volatility)             |
| **5. Disciplined Investing**  | Reducing behavioral mistakes                                       | PAC/PIC, rebalancing, automation                                   | Regular investing and rebalancing reduce timing risk and keep portfolios aligned         |
| **6. Diversification**        | Risk management through variety                                    | Correlation, asset classes, efficient frontier (conceptually)      | Diversification can reduce risk and improve consistency of outcomes                      |
| **7. Portfolio Construction** | Building toward your goals                                         | Asset allocation, risk profile, lifecycle, core-satellite          | A good portfolio matches your needs, constraints, and time horizon                       |
-->

<!--
**Goals:** personal wealth management, to reach personal (reasonable) goals. Person-dependent goals; minimal reasonablle goal: preseve real value of personal wealth (purchasing power)

Human beings usually tend to behave to optimize a personal "utility function".

**Some principles:**
- Return
- No return w/o risk
- Assets usually show auto-correlation in the short-, mid-, regression towards the mean in the long-term
- If one is buying, someonelse is selling

Random topics:
- real vs. nominal: inflation
- Risk/Reward
- diversification
- volatility drag
- PIC vs. PAC

(fin-edu:principles)=
## Return

- Compound return and the exponential function
- Randomness and volatility drag on return

**Compound Actual Growth Rate** over a multi-period time range is the **geometric average** of the single period-return.

```{prf:example} Geometric average is never larger than the aritmetic average

```

````{prf:example} Volatility drag - Geometric Brownian motion

Under the (strong and usually wrong!) assumption of normal distribution of increment of a portfolio NAV, the amount of NAV can be described as a [geometric Brownian motion](https://basics2022.github.io/bbooks-statistics/ch/prob/processes-calculus.html#geometric-brownian-motion)

$$d X_t = \mu X_t dt + \sigma X_t d W_t$$

```{dropdown} Euristic derivation of logarithmic return
:open:

Using $(d W_t)^2 = dt$, and the SDE of the Geometric Brownian motion, Taylor series of $\ln X_{t+dt}$ up to the second order in $dt$ - since $dW \sim dt^2$ - reads

$$\begin{aligned}
  \ln X_{t+dt}
  & = \ln X_{t} + \dfrac{1}{X_{t}} d X_t - \dfrac{1}{2}\dfrac{1}{X^2_t} d X_t^2 + o( d X_t^2 ) = \\
  & = \ln X_{t} + \dfrac{1}{X_{t}} X_t ( \mu dt + \sigma d W_t )- \dfrac{1}{2} \dfrac{1}{X_t^2} X_t^2 ( \mu^2 dt^2 + 2 \mu \sigma dt dW_t + \sigma^2 d W_t^2 ) = \\
  & = \ln X_{t} + \left( \mu dt - \dfrac{1}{2} \sigma^2 d W_t \right) + \sigma d W_t + o(dt) \\
\end{aligned}$$

and thus

$$d \ln X_t = \left( \mu - \dfrac{\sigma^2}{2} \right) dt + \sigma d W_t \ .$$

```

````

```{prf:example} Volatility drag - arbitrary i.i.d. 1-period returns

1-period increment reads

$$\begin{aligned}
  \Delta X_{i,i+1} & = X_i \cdot r_{i,i+1} \\
  X_{i+1} & = X_i + \Delta X_{i,i+1} = X_i \left( 1 + r_{i,i+1} \right) \
\end{aligned}$$

with $r_{i,i+1}$ 1-period return. Thus, the $n$-period return reads

$$\begin{aligned}
  X_{n} 
  & = X_{n-1} \cdot ( 1 + r_{n-1,n} ) = \\
  & = X_{n-2} \cdot ( 1 + r_{n-2,n-1} )( 1 + r_{n-1,n} ) = \\
  & = \dots = \\
  & = X_{0} \prod_{k=1}^n ( 1 + r_{k-1,k} ) \ .
\end{aligned}$$

Evaluating the logarithm of this expression, "multiplication becomes summations" and thus

$$\ln \dfrac{X_n}{X_0} = \sum_{k=1}^{n} ( 1 + r_{k-1,k} ) \ .$$

If $r_{k-1,k}$ are i.i.d. random variables with expected value $\mu$ and variance $\sigma^2$, it follows[^central-limit-thm] that

$$\ln \dfrac{X_n}{X_0} = \sum_{k=1}^{n} ( 1 + r_{k-1,k} ) \rightarrow \mathscr{N} \left( n (1+\mu), n \sigma^2 \right)$$

[^central-limit-thm]: [**central limit theorem**]() $\dfrac{1}{n} \sum_{k=1}^{n} ( 1 + r_{k-1,k} ) \rightarrow \mathscr{N}\left( 1 + \mu, \dfrac{\sigma^2}{n} \right)$.



```

-->


