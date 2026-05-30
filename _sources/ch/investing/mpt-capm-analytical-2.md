(fin-edu:investing:mpt-capm:analytical-2)=
# MPT and CAPM: Analytical Solutions

This section details the closed-form matrix derivations for Modern Portfolio Theory (MPT) and the Capital Asset Pricing Model (CAPM).

## 1. MPT: Fully Invested Portfolio with No Risk-Free Asset

When short-selling and leverage are allowed without limits, the optimization problem can be solved exactly using the method of **Lagrange Multipliers**.

### Problem Setup
$$\min_{\mathbf{w}} \frac{1}{2} \mathbf{w}^T \boldsymbol\sigma^2 \mathbf{w} \quad \text{s.t.} \quad \mathbf{w}^T \boldsymbol\mu = \overline{\mu}, \quad \mathbf{w}^T \mathbf{1} = 1$$

### Objective Function Definition
We set up the Lagrangian dual function $\widetilde{J}$ using multipliers $a$ and $b$:
$$\widetilde{J}(\mathbf{w}; a, b) = \frac{1}{2} \mathbf{w}^T \boldsymbol\sigma^2 \mathbf{w} - a ( \mathbf{w}^T \boldsymbol\mu - \overline{\mu} ) - b ( \mathbf{w}^T \mathbf{1} - 1 )$$

### Deriving First-Order Conditions (FOC)
Taking the vector gradients with respect to $\mathbf{w}$, $a$, and $b$, and setting them to zero:
1. $\nabla_{\mathbf{w}} \widetilde{J} = \boldsymbol\sigma^2 \mathbf{w} - a \boldsymbol\mu - b \mathbf{1} = \mathbf{0}$
2. $\frac{\partial \widetilde{J}}{\partial a} = \boldsymbol\mu^T \mathbf{w} - \overline{\mu} = 0$
3. $\frac{\partial \widetilde{J}}{\partial b} = \mathbf{1}^T \mathbf{w} - 1 = 0$

From condition (1), assuming the covariance matrix $\boldsymbol\sigma^2$ is non-singular and invertible:
$$\mathbf{w}^* = a \boldsymbol\sigma^{-2} \boldsymbol\mu + b \boldsymbol\sigma^{-2} \mathbf{1}$$

### Solving for Constants $a$ and $b$
Define the information matrix constants to simplify notation:
* $A_{11} = \boldsymbol\mu^T \boldsymbol\sigma^{-2} \boldsymbol\mu$
* $A_{12} = \boldsymbol\mu^T \boldsymbol\sigma^{-2} \mathbf{1} = \mathbf{1}^T \boldsymbol\sigma^{-2} \boldsymbol\mu$
* $A_{22} = \mathbf{1}^T \boldsymbol\sigma^{-2} \mathbf{1}$
* $\Delta = A_{11} A_{22} - A_{12}^2$

By substituting $\mathbf{w}^*$ back into constraints (2) and (3), we get a system of linear equations:
$$\begin{aligned}
a A_{11} + b A_{12} &= \overline{\mu} \\
a A_{12} + b A_{22} &= 1
\end{aligned}$$

Solving via Cramer’s rule yields:
$$a = \frac{A_{22} \overline{\mu} - A_{12}}{\Delta}, \quad b = \frac{A_{11} - A_{12}\overline{\mu}}{\Delta}$$

### Final Analytical Weights and Frontier Volatility
Substituting $a$ and $b$ back gives the precise allocation vector:
$$\mathbf{w}^*(\overline{\mu}) = \frac{1}{\Delta} \left[ (A_{22}\overline{\mu} - A_{12})\boldsymbol\sigma^{-2}\boldsymbol\mu + (A_{11} - A_{12}\overline{\mu})\boldsymbol\sigma^{-2}\mathbf{1} \right]$$

The algebraic expression for the portfolio variance ($\sigma_p^2 = \mathbf{w}^{*T}\boldsymbol\sigma^2\mathbf{w}^*$) tracks a hyperbola in the expected return-volatility space:
$$\sigma_{r}(\overline{\mu}) = \sqrt{ \frac{A_{22} \overline{\mu}^2 - 2 \overline{\mu} A_{12} + A_{11}}{\Delta} }$$

---

## 2. CAPM: Introduction of a Risk-Free Asset


When a risk-free asset with guaranteed return $\mu_0$ is introduced, the constraint that risky asset weights must sum to 1 disappears because the remainder allocation $(1 - \mathbf{1}^T\mathbf{w})$ is implicitly placed in cash/risk-free asset.

### Maximizing the Sharpe Ratio (Tangency Condition)
The objective switches to finding the line of maximum slope emanating from $\mu_0$ on the vertical axis. This slope is the Sharpe Ratio:
$$\max_{\mathbf{w}} \frac{\mathbf{w}^T \boldsymbol\mu - \mu_0}{\sqrt{\mathbf{w}^T \boldsymbol\sigma^2 \mathbf{w}}}$$

Because this ratio is invariant to the scale of $\mathbf{w}$, we can set the premium constraint arbitrarily to solve the unscaled system:
$$\mathbf{w}_f^* \propto \boldsymbol\sigma^{-2} \left( \boldsymbol\mu - \mu_0 \mathbf{1} \right)$$

### The Capital Market Line (CML)
The resulting efficient frontier turns from a hyperbola into a straight line equation known as the Capital Market Line:
$$\sigma_f(\overline{\mu}) = \frac{\overline{\mu} - \mu_0}{\sqrt{ \left( \boldsymbol\mu - \mu_0 \mathbf{1} \right)^T \boldsymbol\sigma^{-2} \left( \boldsymbol\mu - \mu_0 \mathbf{1} \right) }}$$

### Tangency Condition Match
To confirm mathematical alignment, setting $\sigma_{r}(\overline{\mu}) = \sigma_f(\overline{\mu})$ determines the exact return coordinate of the **Market Portfolio** ($\mu_M$), showing where the risky-only hyperbola and the risk-free line graze tangentially:
$$\mu_M = \frac{A_{11} - \mu_0 A_{12}}{A_{12} - \mu_0 A_{22}}$$
