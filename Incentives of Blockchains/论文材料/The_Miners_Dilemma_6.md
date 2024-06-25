are oblivious to their role and they operate as regular honest miners, working on tasks.

## B. Revenue Convergence

Note that pool $j$ sends its revenue to infiltrators from pool $i$ at the end of the step, and this revenue is calculated in pool $i$ at the beginning of the subsequent step. If there is a chain of pools of length $\ell$ where each pool infiltrates the next, the pool revenue will not be static, since the revenue from infiltration takes one step to take each hop. If $\ell_{\max }$ is the longest chain in the system, the revenue stabilizes after $\ell_{\max }$ steps. If there are loops in the infiltration graph, the system will converge to a certain revenue, as stated in the following lemma.

Lemma 1 (Revenue convergence). If infiltration rates are constant, the pool revenues converge.

Proof: Denote the revenue density of pool $i$ at the end of step $t$ by $r_{i}(t)$, and define the revenue density vector

$$
\mathbf{r}(\mathbf{t}) \triangleq\left(r_{1}(t), \ldots, r_{p}(t)\right)^{T}
$$

In every round, pool $i$ uses its mining power of $m_{1}-\sum_{j} x_{1, j}$ used for direct mining (and not attacking), and shares it among its $m_{1}+\sum_{j} x_{j, 1}$ members, including malicious infiltrators (all sums are over the range $1, \ldots, p$ ). Denote the direct mining revenue density of each pool (ignoring normalization, which is a constant factor) with the vector

$$
\mathbf{m} \triangleq\left(\frac{m_{1}-\sum_{j} x_{1, j}}{m_{1}+\sum_{j} x_{j, 1}}, \ldots, \frac{m_{p}-x_{p, j}}{m_{p}+\sum_{j} x_{j, p}}\right)^{T}
$$

The revenue of Pool $i$ in step $t$ taken through infiltration from pool $j$ 's revenue in step $t-1$ is $x_{i, j} r_{j}(t-1)$. Pool i distributes this revenue among its $m_{i}+\sum_{k} x_{k, i}$ members loyal and infiltrators. Define the $p \times p$ infiltration matrix by its $i, j$ element

$$
\mathbf{G} \triangleq\left[\frac{x_{i, j}}{m_{i}+\sum_{k} x_{k, i}}\right]_{i j}
$$

And the revenue vector at step $t$ is

$$
\begin{equation*}
\mathbf{r}(t)=\mathbf{m}+\mathbf{G r}(t-1) \tag{1}
\end{equation*}
$$

Since the row sums of the infiltration matrix are smaller than one, its largest eigenvalue is smaller than 1 according to the Perron-Frobenius theorem. Therefore, the revenues at all pools converge as follows:

$$
\begin{equation*}
\mathbf{r}(t)=\left(\sum_{t^{\prime}=0}^{t-1} G^{t^{\prime}}\right) \mathbf{m}+G^{t} \mathbf{r}(0) \xrightarrow{t \rightarrow \infty}(1-\mathbf{G})^{-1} \mathbf{m} \tag{2}
\end{equation*}
$$

## C. The Pool Game

In the pool game pools try to optimize their infiltration rates of other pools to maximize their revenue. The overall number of miners and the number of miners loyal to each pool remain constant throughout the game.

Time progresses in rounds. Let $s$ be a constant integer large enough that revenue can be approximated as its convergence limit. In each round the system takes $s$ steps and then a single pool, picked with a round-robin policy, may change its infiltration rates of all other pools. The total revenue of each step is normalized to $1 / s$, so the revenue per round is one.

The pool taking a step knows the rate of infiltrators attacking it (though not their identity) and the revenue rates of each of the other pools. This knowledge is required to optimize a pool's revenue, as we see next. We explain in Section VIII how a pool can technically obtain this knowledge.

## D. General Analysis

Recall that $m_{i}$ is the number of miners loyal to pool $i$. and $x_{i, j}(t)$ is the number of miners used by pool $i$ to infiltrate pool $j$ at step $t$.

The mining rate of pool $i$ is therefore the number of its loyal miners minus the miners it uses for infiltration. This effective mining rate is divided by the total mining rate in the system, namely the number of all miners that do not engage in block withholding ${ }^{4}$. Denote the direct mining rate of pool $i$ at step $t$ by

$$
\begin{equation*}
R_{i} \triangleq \frac{m_{i}-\sum_{j=1}^{p} x_{i, j}}{m-\sum_{j=1}^{p} \sum_{k=1}^{p} x_{j, k}} \tag{3}
\end{equation*}
$$

The revenue density of pool $i$ at the end of step $t$ is its revenue from direct mining together with its revenue from infiltrated pools, divided by the number of its loyal miners together with block-withholding infiltrators that attack it:

$$
\begin{equation*}
r_{i}(t)=\frac{R_{i}(t)+\sum_{j=1}^{p} x_{i, j}(t) r_{j}(t)}{m_{i}+\sum_{j=1}^{p} x_{j, i}(t)} \tag{4}
\end{equation*}
$$

Hereinafter we move to a static state analysis and omit the $t$ argument in the expressions.

## No attack

If no pool engages in block withholding,

$$
\forall i, j: x_{i, j}=0
$$

and we have

$$
\forall i: r_{i}=1 / m
$$

that is, each miner's revenue is proportional to its power, be it in a pool or working solo.[^0]


[^0]:    ${ }^{4}$ Recall that difficulty is only adjusted periodically, and there are transient effects that are not covered by this stable-state analysis. We discuss this in Section VIII.

