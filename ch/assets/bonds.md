(fin-edu:assets:bonds)=
# Bonds

...


Here the most general expression for nominal and real **yield** are derived as a function of prices, face value of coupon, taxation and year to maturity, both in case of coupon reinvestment or not (reinvestment not always possible); a closed form solution is then derived under some assumptions, like constant (or average) rates; the effect on price and yield of credit rating and rating change, coupon, year to maturity are discussed on both examples and real-world cases.

Extra:
- definition of duration
- risks: inflation; reinvesment (at lower rates) for bonds with same maturity and different coupons
- inflation linked

## Constant coupon bonds

### W/o reinvestment

At time $t_0$ the unit price of a bond is $p_0$; investing $Y_0$ allows to buy $N_0 = \frac{Y_0}{p_0}$ titles; each title has the right of receiving net coupon $C (1 - t)$, with $t$ taxation rate, per period (here assumed 1-year coupon range).


$$N_0 = \dfrac{Y_0}{p_0} = \dfrac{Y_0}{p_{in}} \dfrac{p_{in}}{p_0}$$

W/o reinvestment, the number of titles hold is constant and equal to $N_0$. As capital $Y_i$ can be written as the product of unit price and number of bond in portfolio, the DCF of a bond w/o coupon reinvestment reads

$$\begin{aligned}
  \widetilde{DCF} =
  & = - Y_0 + Y_N \prod_{k=1}^N ( 1 + r_k )^{-1} + \sum_{k=1}^{N} N_0 C (1-t) \prod_{j=1}^{k} (1 + r_j )^{-1} \\ 
  & = N_0 \left[ - p_0 + p_N \prod_{k=1}^N ( 1 + r_k )^{-1} + C (1-t) \sum_{k=1}^{N} \prod_{j=1}^{k} (1 + r_j )^{-1} \right] \ , 
\end{aligned}$$

This DCF must be corrected a CF at time $t_N$ corresponding to tax on capital gain if $p_n > p_0$, discounted as

$$- N_0( p_N  - p_0) \,  t \,  \prod_{k=1}^{N} (1+r_k)^{-1}  \qquad  (\text{only if $p_N > p_0$})$$


The cumulative real return (if the discount ratio is inflation) is the ratio between the $DCF$ and the actual value of the investment $Y_0$,

$$\widetilde{\dfrac{DCF}{Y_0}} = - 1 + \dfrac{p_N}{p_0} \prod_{k=1}^N ( 1 + r_k )^{-1} + \dfrac{C}{p_0} (1-t) \sum_{k=1}^{N} \prod_{j=1}^{k} (1 + r_j )^{-1}  $$

If the discount rate is constant, or the average (which average) discount rate is used, the expression of the cumulative return reads

$$\begin{aligned}
  \dfrac{\widetilde{DCF}}{Y_0} = - 1 + \dfrac{p_N}{p_0} ( 1 + r )^{-N} + \dfrac{C}{p_0} (1-t) \sum_{k=1}^{N} (1 + r )^{-k}  
\end{aligned}$$


### W/ reinvestment

| Time       | Cashflows                    | $\Delta$Quantity                               | Quantity                           | DF                               |
| :--------: | :--------------------------: | :--------------------------------------------: | :--------------------------------: | :------------------------------: | 
| $0$        | $-Y_0$                       | $N_0 = \frac{Y_0}{p_0}$                        | $N_0 = \frac{Y_0}{p_0}$            | 1                                | 
| $1$        | $+N_0 C ( 1-t )$             |                                                |                                    | $(1+r_1)^{-1}$                   | 
| $1$        | $-N_0 C ( 1-t )$             | $N_1 = \frac{N_0 C (1-t)}{p_1}$                | $N_{0:1} = N_0+N_1$                | $(1+r_1)^{-1}$                   | 
| $2$        | $+N_{0:1} C ( 1-t )$         |                                                |                                    | $(1+r_1)^{-1} (1+r_2)^{-1}$      | 
| $2$        | $-N_{0:1} C ( 1-t )$         | $N_2 = \frac{N_{0:1} C (1-t)}{p_2}$            | $N_{0:2} = N_0+N_1 + N_2$          | $(1+r_1)^{-1} (1+r_2)^{-1}$      | 
| ...        |                              |                                                |                                    |                                  | 
| $T-1$      | $+N_{0:T-2} C ( 1-t )$       |                                                |                                    | $\prod_{k=1}^{T-1} (1+r_k)^{-1}$ |
| $T-1$      | $-N_{0:T-2} C ( 1-t )$       | $N_{T-1} = \frac{N_{0:T-2} C (1-t)}{p_{T-1}}$  | $N_{0:T-1} = \sum_{k=0}^{T-1} N_k$ | $\prod_{k=1}^{T-1} (1+r_k)^{-1}$ |
| $T$        | $+N_{0:T-1} C ( 1-t )$       |                                                |                                    | $\prod_{k=1}^{T  } (1+r_k)^{-1}$ |
| $T$        | $+N_{0:T-1} p_T$             |                                                |                                    | $\prod_{k=1}^{T  } (1+r_k)^{-1}$ |

All the cashflows from coupons are immediately reinvested so the DCF is

$$\begin{aligned}
  DCF 
  & = - Y_0 + \underbrace{N_{0:T-1} \left( p_T + C (1-t)\right)}_{Y_T} \, \underbrace{ \prod_{k=1}^T (1+r_k)^{-1} }_{DF_T} = \\
  & = - Y_0 + Y_T \,  DF_T \ ,
\end{aligned}$$

with 

$$\begin{aligned}
  N_{0:T-1}
  & = N_{0:T-2} + N_{T-1} =  N_{0:T-2} + N_{0:T-2} \frac{ C (1-t)}{p_{T-1}} = N_{0:T-2} \left[ 1 + \frac{ C (1-t)}{p_{T-1}} \right] = \\
  & = N_{0:T-3} \left[ 1 + \frac{ C (1-t)}{p_{T-2}} \right] \left[ 1 + \frac{ C (1-t)}{p_{T-1}} \right] = \\
  & = \dots = \\
  & = N_{0:1} \prod_{k=2}^{T-1} \left[ 1 + \frac{ C (1-t)}{p_{k}} \right] = \\ 
  & = N_{0  } \prod_{k=1}^{T-1} \left[ 1 + \frac{ C (1-t)}{p_{k}} \right] \ .
\end{aligned}$$

Cumulative discounted return reads

$$\begin{aligned}
  \dfrac{DCF}{Y_0} 
  & = - 1 + \dfrac{Y_T}{Y_0} DF_{T} = \\
  & = - 1 + \dfrac{N_0}{N_0 \, p_0} \prod_{k=1}^{T-1} \left( 1+ \dfrac{C(1-t)}{p_k} \right) \, ( p_T + C(t-1) ) \, DF_T \\
  & = - 1 + \dfrac{p_T}{p_0} \prod_{k=1}^{T} \left( 1+ \dfrac{C(1-t)}{p_k} \right) \, DF_T \\
  & = - 1 + \dfrac{p_T}{p_0} \prod_{k=1}^{T} \left( \dfrac{ 1+ \frac{C(1-t)}{p_k} }{1+r_k} \right) \ .
\end{aligned}$$

Composite discounted return is obtained, after writing the diiscounted cashflow as the difference between discounted cashflow at time $t_T$ and $t_0$, $DCF = Y_T \ DF_T - T_0$,

$$(1 + DCAGR)^T = \dfrac{Y_T \, DF_T}{Y_0} = \dfrac{DCF}{Y_0} + 1 = \dfrac{p_T}{p_0} \, \prod_{k=1}^{T} \left( \dfrac{ 1+ \frac{C(1-t)}{p_k} }{1+r_k} \right)$$

$$DCAGR = \left( \dfrac{p_T}{p_0} \, \prod_{k=1}^{T}  \dfrac{ 1+ \frac{C(1-t)}{p_k} }{1+r_k} \right)^{\frac{1}{T}} - 1$$

**If**[^bond-const-price-hp] price of the bond is constant throughout its whole life, $p_k = 1$, $\forall k=0:T$, and discount rate $r$ is constant, the number of held bonds at time $T-1$ is

$$N_{0:T-1} = N_0 \left( 1 + C(1-t) \right)^{T-1} \ ,$$

the discounted cashflow is

$$\begin{aligned}
  DCF 
  & = - N_0 + N_0 \left( 1 + C(1-t) \right)^{T-1} ( 1 + C(1-t) ) \left( 1 + r \right)^{-T} = \\
  & = N_0 \left[ - 1 +  \left( \dfrac{ 1 + C(1-t) }{ 1 + r } \right)^{T} \right] \ ,
\end{aligned}$$

cumulative discounted return

$$\dfrac{DCF}{Y_0} = - 1 + \left( \dfrac{ 1 + C(1-t) }{ 1 + r } \right)^{T}$$

and the composite discounted return reads

$$DCAGR = \dfrac{1 + C(1-t)}{1+r} - 1 \ .$$

[^bond-const-price-hp]: It's a big if. Even if credit rating and inflation are constant throughout the life of the bond, years to maturity decreases and thus - usually - the required rate decreases as well.
