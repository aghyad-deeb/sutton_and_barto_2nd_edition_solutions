# Chapter 2 solutions
## 2.1 
If we explore we pick greedy arm with probability half and if we exploit we pick
it for sure.

$1/2 * 1 + 1/2 * 1/2 = 3/4$

## 2.2
Could be exploration: $A_1, A_2, A_3, A_4, A_5$
(all actions could be exploration)

Must be exploration (picked suboptimal arm): $A_4, A_5$

## 2.3
$\varepsilon = 0.01$ because it will (a) find the optimal action with very
high probability (since we're considering the long run case), (b) choose it with
very high probability (since it has lower probability of exploring than the 
other $\varepsilon-greedy$ algorithm).

In the long run, we can assume that the sample average of each arm will converge
to its true average by Law of Large Numbers.
Quantitavely, $\varepsilon=0.01$ would pick the optimal action
$0.99 * 1 + 0.01 *1/10 = 0.991$ fraction of the time, while $\varepsilon=0.1$
would pick the optimal action $0.9*1 + 0.1 * 1/10 = 0.91$ fraction of the time.

Plain greedy would stick with the arm it chose in the long run as it the sample
average converges to the true average for the arm that is picked repeatidly but
not for the other arms as they may not be picked enough, so we expect it to
stick with the optimal arm if it picked it early on (~35% of the time based on
Figure 2.2) but also totally avoid it if it's not picked early on.

## 2.4
For $n$ steps, the weighting of the reward $R_i$, which we'll call $w_i$ is
$$w_i = \alpha_i \; \Pi_{j=i+1}^n \,(1- \alpha_j)$$

This can be found be spreading out the terms of $(2.6)$ but with replacing 
$\alpha$ with the $\alpha_i$ for each timestep $i$.

## 2.5
See the script `2_5.py`

## 2.6
The fraction of optimal action starts at around $1/10$ which is expected given
that we have $10$ arms for the bandit. After trying all the different arms, we
the value estimates of all arms to go down as the initial values were most 
likely much higher than the true values. The do, however, go down in different
amounts, and it is expected that the arm with the highest reward will go down
less than others, which leads to the it being picked repeatidly. This explains
the upward spike we see in the early steps. However, after picking the optimal
arm repeatidly, it's estimated value will continue to fall down and eventually
we expect it to fall down more than the estimated values of other arms which
were not sampled as much and therefore are more affected by the initial
optimistic values, which explains the downward spike right after the upward one.

## 2.7
Starting from $(2.6)$:
$$\begin{aligned}
Q_{n + 1} &= Q_n + \beta_n (R_n - Q_n)\\
&= \beta_n R_n + (1 - \beta_n) Q_n \\
&= \beta_n R_n + (1- \beta_n) \beta_{n - 1} R_{n - 1} + (1- \beta_n) ( 1- \beta_{n - 1}) Q_{n - 1} \\
&= Q_1 \prod_{i = 1}^n (1 - \beta_i) + \sum_{j = 1}^n R_j \left[ \beta_j  \prod_{i = j + 1}^n ( 1 - \beta_i) \right]
\end{aligned}$$
In order for the value estimate to be unbiased, the coeffecient of $Q_1$ should
be $0$:
$$
\begin{aligned}
    \prod_{i = 1}^n (1 - \beta_i) &= \left[ (1 - \beta_1) (1- \beta_2) \dots \right] \\
    &= \left[ \left(1 - \frac{\alpha}{\alpha}\right) (1- \beta_2) \dots \right] \\
    &= 0
\end{aligned}
$$

## 2.7
We note that, as mentioned in the chapter, when $N_t(a) = 0$, the action $a$
maximizes the term $(2.10)$ which means that we expect the average reward for
the first 10 steps as not all actions are picked yet (the average reward is 
around 0 based on the design of the bandits). However, at the 11th step, UCB
starts actually using the information it collected and picks the top estimated
action (note that it exactly picks the top estimated action at step 11 as the
uncertainties are equal at that point); let's call this action $a_{11}$. After
the 11th step, however, the uncertainty for $a_{11}$ will decrease which will
decrease the upper confidence bound for it while other actions have more
uncertainty, leading to other actions, often with lower point-estimate of
reward, being picked. When averaging over 1000 runs, we expect the point
estimates to be often correct, even when the sample size is 1 before step 11.

## 2.9
The logistic funciton has the form:
$$
\sigma(x) = \frac{e^x}{1 + e^x}
$$
In the case of two actions $a_1, a_2$, we have the softmax mass function:
$$\begin{aligned}
    P(A_t = a_1) &= \frac{e^{H_t(a_1)}}{e^{H_t(a_1)} + e^{H_t(a_2)}} \\
    &= \frac{e^{H_t(a_1) - H_t(a_2)}}{1 + e^{H_t(a_1) - H_t(a_2)}} \\
\end{aligned}$$
Which is the same as the logitistic/sigmoid function when the input is $H_t(a_1) - H_t(a_2)$