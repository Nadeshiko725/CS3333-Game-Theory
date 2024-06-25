| Pool 1 | no attack | attack |
| :--- | :---: | :---: |
| Pool 2 | $\left(r_{1}=1, r_{2}=1\right)$ | $\left(r_{1}>1, r_{2}=\tilde{r}_{2}<1\right)$ |
| no attack | $\left(r_{1}=\tilde{r}_{1}<1, r_{2}>1\right)$ | $\left(\tilde{r}_{1}<r_{1}<1, \tilde{r}_{2}<r_{2}<1\right)$ |
| attack |  |  |

Figure 9. Prisoner's Dilemma for two pools. The revenue density of each pool is determined by the decision of both pools whether to attack or not. The dominant strategy of each player is to attack, however the payoff of both would be larger if they both refrain from attacking.

a pool can detect whether it is being attacked and deduce that the other pool is violating the agreement. In this supergame, cooperation where neither pool attacks is a possible stable state [25], [26] despite the fact that the single Nash equilibrium in every round is to attack.

## C. Test-case

As an example we take again the pool sizes shown in Figure 6, and study the case where the two largest pools, DiscusFish and AntPool, attack one another. The optimal infiltration rates (out of the total system mining power) are $8 \%$ and $12 \%$, respectively, and the pools would lose $4 \%$ and $10 \%$ of their revenues, respectively, compared to the no-attack scenario.

## VII. $q$ IDENTICAL POOLS

Let there be $q$ pools of identical size that engage in block withholding against one another. Other miners neither attack nor are being attacked. In this case there exists a symmetric equilibrium. Consider, without loss of generality, a step of pool 1. It controls its attack rates each of the other pools, and due to symmetry they are all the same. Denote by $x_{1, \neg 1}$ the attack rate of pool 1 against any other pool. Each of the other pools can attack its peers as well. Due to symmetry, all attack rates by all attackers are identical. Denote by $x_{\neg 1, *}$ the attack rate of any pool other than 1 against any other pool, including pool 1 .

Denote by $R_{1}$ the direct revenue (from mining) of pool 1 and by $R_{\neg 1}$ the direct revenue of each of the other pools. Similarly denote by $r_{1}$ and $r_{\neg 1}$ the revenue densities of pool 1 and other pools, respectively.

The generic equations 3 and 4 are instantiated to

$$
\begin{align*}
& R_{1}=\frac{m_{i}-(q-1) x_{1, \neg 1}}{m-(q-1)(q-1) x_{\neg 1, *}-(q-1) x_{1, \neg 1}} \\
& R_{\neg 1}=\frac{m_{i}-(q-1) x_{\neg 1, *}}{m-(q-1)(q-1) x_{\neg 1, *}-(q-1) x_{1, \neg 1}} \tag{17}
\end{align*}
$$

and

$$
\begin{align*}
& r_{1}=\frac{R_{1}+(q-1) x_{1, \neg 1} r_{\neg 1}}{m_{i}+(q-1) x_{\neg 1,1}} \\
& r_{\neg 1}=\frac{R_{\neg 1}+(q-2) x_{\neg 1, *} r_{\neg 1}+x_{\neg 1, *} r_{1}}{m_{i}+(q-2) x_{\neg 1, *}+x_{1, \neg 1}} \tag{18}
\end{align*}
$$

Substituting Equations 17 in Equation 18 and solving we obtain a single expression for any $r_{i}$, since in the symmetric case we have $r_{1}=r_{\neg 1}$. The expression is shown in Equation 18 (Figure 10).

Given any value of $q$ and $m_{i}$ (where $q m_{i}<1$ ), the feasible range of the infiltration rates is $0 \leq x_{i, j} \leq m_{i} / q$. Within this range $r_{i}$ is continuous, differentiable, and concave in $x_{1, \neg 1}$. Therefore, the optimal point for pool 1 is where $\partial r_{1} / \partial x_{1, \neg 1}=0$. Since the function is concave the equation yields a single feasible solution, which is a function of the attack rates of the other pools, namely $x_{\neg 1,1}$ and $x_{\neg 1, *}$.

To find a symmetric equilibrium, we equate $x_{1, \neg 1}=$ $x_{\neg 1,1}=x_{\neg 1, *}$ and obtain a single feasible solution. The equilibrium infiltration rate and the matching revenues are shown in Equation 20 (Figure 11).

As in the two-pool scenario, the revenue at the symmetric equilibrium is inferior to the no-one-attacks non-equilibrium strategy.

## VIII. PraCTICALITIES

## A. Ramp-up

Our analysis addresses the eventual revenue of the pools, assuming the mining difficulty is set based on the effective mining power, not including mining power used for withholding. However, difficulty is updated only periodically every 2016 blocks in Bitcoin. When mining power in the system is regularly increasing, which has been true for the majority of Bitcoin's history [27], no adjustment may be necessary. Specifically, if an attacker purchases new mining hardware and employs it directly for block withholding, this mining power is never included in the difficulty calculation - the system is never aware of it. The difficulty is therefore already correctly calculated and the attack is profitable immediately.

However, if the mining power is static, the attack becomes profitable only after the Bitcoin system has normalized the revenues by adjusting difficulty. Before the adjustment, the revenue of an attacking pool is reduced due to the reduction in block generation of both the attacking and attacked pools.

## B. Pool Knowledge

In order to choose its optimal infiltration rate, a pool has to know the rate at which it is attacked, and the revenue density of potential victim pools. A pool can estimate the rate with which it is attacked by comparing the rates of partial and full proofs of work it receives from its miners, as explained in Section II-C. In order to estimate the revenue densities of the other pools, a pool can use one of two methods. First, pools

