(fin-edu:investing:rebalancing)=
# Rebalancing

**Reasons.**
- risk management:
  - adjust risk for the period of life, and risk-level
  - correct drift towards the asset with highest return, as it affects the 

**Strategies.**
In a passive investment strategy, rebalancing shoudl be triggered by some rules, to be applied automatically. As an example:
- periodic rebalancing: rebalancing with constant time interval
- deviation-triggered: rebalancing when asset allocation deviation from the traget allocation exceeds a prescribed threshold. E.g. approximately 10% of a 60-40 portfolio going to 65-35 (introduction of episode **152**, as a summary of episode **117**)
- using contributions/withdrawals

**Effects of rebalancing.** In different situations one of the following effects occurs:
- Volatility is reduced
- Risk-adjusted return improves
- Return of the portfolio is increased

Often, a rebalanced-portfolio return is larger than the weighted average of the returns of the assets of the portfolio. Shannon demon is the mathematical reason for that, *for creating return "out of thin air"*.

```{prf:example} Shannon demon - on a coin flip
:label: shannon-demon

Starting with $100$€, and a fair coin with $50\%$ probability of for each outcome, either $H$:head or $T$:tail. If outcome is $H$ you gain $50 \%$, if outcome is $T$ you lose $33.3 \%$. 

- If I play with all the money I have, what is the expected amount at the end of the game, for a sufficiently large number of toss?

Now, let's change the strategy: I bet only $50 \%$ of the amount I have. What's the expected amount at the end of the game?

```

```{prf:example} Nassin Taleb, is the coin fair?
:label: taleb-fair-coin

After 10 tosses with 10 heads, how would you bet on the next toss?

```

```{prf:example} Kelly criterion
:label: kelly

*bla bla bla*

```

```{prf:example} Does rebalancing improve return, thanks to Shannon demon?
:label: shannon-demon-rebalancing

Yes, for a portfolio with 2 assets with similar returns and low correlation. 
E.g.:
- **S&P500** and **gold** (50%-50%) from 1972 to 2008 (cherry-picking?): CAGR with annual rebalancing: 10.3%, while S&P: 9.4% and gold: 8.2%.
- S&P500 and gold (50%-50%) from 1972 to 2023 (cherry-picking?): CAGR with annual rebalancing: 10.2%, while S&P: 10.5% and gold: 7.5%, but with lower volatility, lower max drawdown and a better Sharpe ratio
- S&P500 and Treasury (50%-50%) from 1972 to 2023 (cherry-picking?): CAGR with annual rebalancing: 9.3%, while S&P: 10.5% and gold: 6.4%, but with lower volatility, lower max drawdown and a better Sharpe ratio. Without rebalancing: 9.6% (higher!) as equity has much higher return and drift occurs over 50-year period.
- MSCI World and FTSE G7...

No, with 2 assets with 2 assets with very different returns. Anyways, if they have low correlation, rebalancing (may?) reduce volatility, improves risk-adjusted return, or both.

```


## Resources
- [The Bull](fin-edu:resources:the-bull)
  - **217.** Il modo migliore per Ribilanciare il portafoglio
  - **152.** La magia del ribilanciamento e il demone di Shannon
  - **117.** Come ribilanciare il portafoglio (e previsioni per i prossimi 10 anni)
- [R.Arnott](fin-edu:resources:people:arnott). Over-rebalancing

- [market sentiment about Shannon demon](https://www.marketsentiment.co/p/shannons-demon)

