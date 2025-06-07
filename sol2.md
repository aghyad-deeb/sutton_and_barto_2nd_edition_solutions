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

This can be found be spreading out th terms of $(2.6)$ but with replacing 
$\alpha$ with the $\alpha_i$ for each timestep $i$.
