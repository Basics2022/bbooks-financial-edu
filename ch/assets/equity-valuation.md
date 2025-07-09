(fin-edu:assets:equity:valuation)=
# Equity Valuation

```{dropdown} Detailed introduction
Equity valuation blends common sense, mathematics, expectations, estimation—and a bit of art. Buying shares in a company, whether directly or through a fund, means owning a (tiny) stake in a real business that produces goods and/or services and has the potential to generate earnings or free cash flows. As a shareholder, you are not just investing in market prices—you’re becoming a part-owner of the enterprise. This ownership entitles you to a share of the company’s profits through dividends or capital appreciation. It also comes with certain rights and responsibilities, especially during difficult periods.

When companies face financial stress or pursue growth opportunities, they may issue new shares to raise capital. This can lead to dilution, reducing the percentage ownership of existing shareholders. However, shareholders often have preemptive rights, allowing them to participate in new issuances to maintain their ownership stake. Moreover, owning equity means having a claim on the residual value of the company—what’s left after all debts are paid—in both prosperous and challenging times. Understanding these dynamics is crucial to valuing equity: you're not just buying into today’s performance, but into a stream of future cash flows and the complex, evolving structure of ownership.

```

**Sensitivity analysis** could provide an estimate of the effects of different parameters/assumptions on the final result. 

**Different valuation methods** exist, and can be broadly classified in 
- **comparison** approach: P/E, EV/EBITDA, or other indices used to compare companies of the same sector, marked, dimension,...[^comparison]
- **intrinsic value** approach, based on **DCF**
- ...other methods for general firms (cost approach,...); valuation of financials;...

[^comparison]: It's not always possible to find "equivalent" companies for the comparison...; P/E, EV/EBITDA,... whould be projected into the future to keep into account future in the value of a firm.


(fin-edu:assets:equity:valuation:comparison)=
## Comparison

(fin-edu:assets:equity:valuation:intrinsic)=
## Intrinsic value

- Future cash flows are estimated, 
- CFs are discounted, usually for the $WACC$ (Weighted Average Cost of Capital) to find the $NPV$ (net present value) of the **enterprise value** $EV$
- Cash and equivalents are added to the $NPV$ to find the **equity value**


```{admonition} $WACC$
:class: tip
  $$WACC = \dfrac{E}{V} R_e + \dfrac{D}{V} R_d (1 - t)$$

  being $R_e$ the **cost of equity** and $R_d$ the **cost of debt** (maybe the easiest part to estimated accurately, since the debt structure is usually known/programmed). The factor $(1-t)$ usually appears as interest payments are tax-deductible.
```

```{admonition} Equity Risk Premium $R_e$ - Sharpe
:class: tip

Following W.Sharpe, equity risk premium can be estimated as

$$R_e = R_f + (R_m + R_f) \beta \ ,$$

being $R_f$ the risk-free rate (usaully 10Y US Treasuries), and $R_m$ the annual return of the market/sector of the investment, $\beta$ is a measure of risk or stock volatility of returns of the investment relative to that of the market/sector.

```

