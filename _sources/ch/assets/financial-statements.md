(fin-edu:financial-statements)=
# Three Financial Statements

Financial statements are written records that illustrates the business activities and the financial performance of a company. In most cases they are audited to ensure accuracy for tax, financing, or investing purposes.

**Uses.** *Management* uses them for decision-making, budgeting and performance evaluation. *Investors* use them to asses profitability, financial health, future performance, and creditworthiness (especially *lenders*).

- **Income statement**: company performance (profit and loss) over a period. Broadly speaking: 

    $$\text{net earnings} = ( \text{revenues} - \text{total expenses} ) \times ( 1 - \text{tax rate} ) , $$

    with total expenses = operative (labor + non-labor + DA) + Interest (due to debt holders), and "partial earnings" EBITDA, EBIT, EBT with trivial definition (Earnings Before: I:interest, DA: depreciation and amortization, T: tax)

- **Balance sheet**: financial position at a specific point in time, in terms of:
   - assets: cash and equivalent + acc.receiv. + inventory + PPE (Plant property and equipment, subject to CapEx and depreciation, $PPE(n) = PPE(n-1) + \text{CapEx}(n) + \text{DA}(n)$
   - liabilities: debt + acc.pay.
   - equity: 
     
     $$\begin{aligned}
       \text{retained earnings}(n) & = \text{retained earnings}(n-1) + \text{net earnings}(n) - \text{dividends}(n) \\
       \text{shareholder equity}(n) & = \text{equity capital}(n) + \text{retained earnings}(n) \ ,
     \end{aligned}$$

     being $\text{retained earnings}(n)$ the **cumulative** retained earnings not distributed to shareholders.

     The 2 contributions $\text{shareholder equity}$, $\text{total liabilities}$ shows how the  compnay's asset are financed: either through capital raised or retained earnings (equity), or through debt (liabilities). The **identity**

     $$\text{total liabilities} + \text{shareholders equity} = \text{total asset}$$

     must hold in a proper filled balance.

- **Cash flow statement** tracks the flows of cash in and out of the business over a period. Cashflows over a period modifies cash,

  $$\begin{aligned}
    \text{closing cash}(n) & = \text{opening cash}(n) + \text{total cashflow}(n) \\
    \text{opening cash}(n) & = \text{closing cash}(n-1)
  \end{aligned}$$

  Cashflows are usually classified as:
  - operating CF (DA is added back to net income, since it's not a cashflow going anywhere; it lowers income, but it's not a cashflow)
  - investing CF
  - financing CF
   
    $$\begin{aligned}
      \text{ Op.CF}(n) & = \text{net earnings}(n) + \text{DA}(n) - \Delta \text{WC}(n) \\
      \text{Inv.CF}(n) & = \text{investment in PPE}(n) \\
      \text{Fin.CF}(n) & = \text{issuance of debt}(n) + \text{issuance of equity}(n) - \text{dividends}(n) \\
    \end{aligned}$$

    being $\text{WC}(n) = \text{acc.rec}(n) + \text{inventory}(n) - \text{acc.pay}(n)$ the **working capital**.
