expressions for each. We express the revenues as functions of $x_{1,2}$ and $x_{2,1}$.

$$
\begin{align*}
& r_{1}\left(x_{1,2}, x_{2,1}\right)=\frac{m_{2} R_{1}+x_{1,2}\left(R_{1}+R_{2}\right)}{m_{1} m_{2}+m_{1} x_{1,2}+m_{2} x_{2,1}} \\
& r_{2}\left(x_{2,1}, x_{1,2}\right)=\frac{m_{1} R_{2}+x_{2,1}\left(R_{1}+R_{2}\right)}{m_{1} m_{2}+m_{1} x_{1,2}+m_{2} x_{2,1}} \tag{11}
\end{align*}
$$

Each pool controls only its own infiltration rate. In each round of the pool game, each pool will optimize its infiltration rate of the other. If pool 1 acts at step $t$, it optimizes its revenue with

$$
\begin{equation*}
x_{1,2}(t) \leftarrow \arg \max _{x^{\prime}} r_{1}\left(x^{\prime}, x_{2,1}(t-1)\right) \tag{12}
\end{equation*}
$$

and if pool 2 acts at step $t$, it optimizes its revenue with

$$
\begin{equation*}
x_{2,1}(t) \leftarrow \arg \max _{x^{\prime}} r_{2}\left(x^{\prime}, x_{1,2}(t-1)\right) \tag{13}
\end{equation*}
$$

An equilibrium exists where neither pool 1 nor pool 2 can improve its revenue by changing its infiltration rate. That is, any pair of values $x_{1}^{\prime}, x_{2}^{\prime}$ such that

$$
\left\{\begin{array}{l}
\arg \max _{x_{1,2}} r_{1}\left(x_{1,2}, x_{2,1}^{\prime}\right)=x_{1,2}^{\prime}  \tag{14}\\
\arg \max _{x_{2,1}} r_{2}\left(x_{1,2}^{\prime}, x_{2,1}\right)=x_{2,1}^{\prime}
\end{array}\right.
$$

under the constraints

$$
\begin{align*}
& 0<x_{1}^{\prime}<m_{1} \\
& 0<x_{2}^{\prime}<m_{2} \tag{15}
\end{align*}
$$

The feasible region for the pool sizes is $m_{1}>0, m_{2}>0$, and $m_{1}+m_{2} \leq m$. The revenue function for $r_{i}$ is concave in $x_{i}$ for all feasible values of the variables $\left(\partial^{2} r_{i} / \partial x_{i}^{2}<0\right)$. Therefore the solutions for equations 12 and 13 are unique and are either at the borders of the feasible region or where $\partial r_{i} / \partial x_{i, j}=0$.

From Section V we know that no-attack is not an equilibrium point, since each pool can increase its revenue by choosing a strictly positive infiltration rate, that is, $x_{1,2}=$ $x_{2,1}=0$ is not a solution to Equations 14-15.

Nash equilibrium therefore exists with $x_{1,2}, x_{2,1}$ values where

$$
\left\{\begin{array}{l}
\frac{\partial r_{1}\left(x_{1,2}, x_{2,1}\right)}{\partial x_{1,2}}=0  \tag{16}\\
\frac{\partial r_{2}\left(x_{2,1}, x_{1,2}\right)}{\partial x_{2,1}}=0
\end{array}\right.
$$

Using symbolic computation tools, we see that there is a single pair of values for which Equation 16 holds for any feasible choice of $m_{1}$ and $m_{2}$.

## A. Numerical Analysis

A numerical analysis confirms these observations. We simulate the pool game for a range of pool sizes. For each choice of pool sizes, we start the simulation when both pools do not infiltrate each other, $x_{1,2}=x_{2,1}=0$, and the revenue densities are $r_{1}=r_{2}=1$. At each round one pool chooses its optimal infiltration rate based on the pool sizes and the rate with which it is infiltrated, and we calculate the revenue after convergence with Equation 11. Recall the players in the pool game are chosen with the Round Robin policy, so the pools take turns, and we let the game run until convergence. The results are illustrated in Figure 7.

Each run with some $m_{1}, m_{2}$ values results in a single point in each graph in Figure 7. We depict the infiltration rates of both pools $x_{1,2}, x_{2,1}$ in Figures 7a-7b and the pools' revenue densities $r_{1}, r_{2}$ in Figures 7c-7d. So, for each choice of $m_{1}$ and $m_{2}$, the values of $x_{1,2}, x_{2,1}, m_{1}$ and $m_{2}$ are the points in each of the graphs with the respective coordinates.

For the $x_{i, j}$ graphs we draw a border around the region where there is no-attack by $i$ in equilibrium. For the $r_{i}$ graphs we draw a line around the region where the revenue is the same as in the no-attack scenario, namely 1.

We first observe that only in extreme cases a pool does not attack its counterpart. Specifically, at equilibrium a pool will refrain from attacking only if the other pool is larger than about $80 \%$ of the total mining power.

But, more importantly, we observe that a pool improves its revenue compared to the no-pool-attacks scenario only when it controls a strict majority of the total mining power. These are the small triangular regions in Figures 7c and 7d. In the rest of the space, the trapezoids in the figures, the revenue of the pool is inferior compared to the no-poolattacks scenario.

## B. The Prisoner's Dilemma

In a healthy Bitcoin environment, where neither pool controls a strict majority of the mining power, both pools will earn less at equilibrium than if both pools ran without attacking. We can analyze in this case a game where each pool chooses either to attack and optimize its revenue, or to refrain from attacking.

Consider pool 1 without loss of generality. As we have seen in Section V, if pool 2 does not attack, pool 1 can increase its revenue above 1 by attacking. If pool 2 does attack but pool 1 does not, we denote the revenue of pool 1 by $\tilde{r}_{1}$. The exact value of $\tilde{r}_{1}$ depends on the values of $m_{1}$ and $m_{2}$, but it is always smaller than one. As we have seen above, if pool 1 does choose to attack, its revenue increases, but does not surpass one. The game is summarized in Figure 9.

When played once, this is the classical prisoner's dilemma. Attack is the dominant strategy: Whether pool 2 chooses to attack or not, the revenue of pool 1 is larger when attacking than when refraining from attack, and the same for pool 2. At equilibrium of this attack-or-don't game, when both pools attack, the revenue of each pool is smaller than its revenue if neither pool attacked.

However, the game is not played once, but rather continuously, forming a super-game, where each pool can change its strategy between attack and no-attack. The pools can agree (even implicitly) to refrain from attacking, and in each round

