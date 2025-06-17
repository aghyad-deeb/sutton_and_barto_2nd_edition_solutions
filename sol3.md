## 3.1
1. Consider an agent trying to manage a company. The reward could be the stock
options value. The state could be the budget for each part of the company. The
actions could be increasing or decreasing the budget for each sector (a vector
of the change in each sector's budget).
2. Consider an agent representing a person trying to quit smoking. The reward
could be time since last smoked. The state could be the last couple of thoughts
(say 5) the person had, which the person does not have complete control over.
The action could be one active thought that the person can think of.
3. The agent can represent a person deciding whether to vote red or blue in the
next election. The reward is how satisfied they are with the policies being
issued. The state is the result of the election (since it's out of the control
of the agnet) and the policies.

## 3.2
Problems where the state space is infinite. For example, when the state is a location in a continous environment. Yet, it's still possible to discretize the space. 

## 3.3 
I think that a good place to draw the line is the highest level place where the agent has a lot of control. For example, if we were to choose the framing of where to drive, we would be missing out on the fact that where we drive is not completely in our control; the car may break down. Howover, nothing is really fully under control, and if we were to got to a level like the muscle twitches, it becomes less helpful as the action space is much larger. There's a tradeoff between how much control you have and how small the action space is.

## 3.4
(It's unclear to me if this is intended, bu I decided to do my own example here since Example 3.3 has an infinte number of possible rewards and therefore the table would have an infinite number of rows. Example 3.3 also has no indication of the probabilities of different rewards.)
Consider a simplified version of Example 3.3 where the robot gets 2 cans if actively searching and 1 can if waiting.

|s | a | s' | r |p(s', r\| s, a) | 
|--|-- |----|---|-----------------------| 
| high | search | high | 2 | $\alpha$ |
| high | search | low | 2 | $1 - \alpha$ |
| high | wait | high | 1 | 1 |
|low | search | high | -3 | $1 - \beta$ |
|low | search | low | 2 | $\beta$ |
|low | wait| low | 1 | 1| 
| low | recharge | high | 0 | 1

## 3.5
We need to make sure the terminal state is included:
$$
\sum_{s' \in \mathcal{S^+}} \, \sum_{r \in \mathcal{R}}
p(s', r | s, a) = 1, \; \text{for all} \, s, s
\in \mathcal{S}, \, a \in \mathcal{A}(s).
$$

## 3.6
In a discounted episodic case, the return is:
$$
G_t = - \gamma^{T - t}
$$
It differs from the discounted continuing case in that it does not include
failures after the first one, so the return is strictly larger in the episodic
case.

## 3.7
We note that with such a design, the expected reward is always the same: 1. The agent is not incentivized to finish early since it doesn't give it more rewards, so the agent does not learn to try to escape as experiments where it escapes early or takes arbitrarly long to escape give the same reward.

## 3.8
We have an episodic, discounted case. 
$$
\begin{aligned}
G_5 &= 0 \\
G_4 &= 2 \\
G_3 &= 3 + 0.5 * 2 = 4 \\
G_2 &= R_3 + \gamma G_3 = 6 + 0.5 * 4 = 8 \\
G_1 &= 2 + 0.5 * 8 = 6 \\
G_0 &= -1 * 0.5 * 6 = 2
\end{aligned}
$$

## 3.9
$$
G_1 = 7 \, \sum_{i = 0}^{\infty} \gamma^i = \frac{7}{1 - \gamma}  = 70
$$
$$
G_0 = 2 + 0.9 * 70 = 65 
$$

## 3.10
The equality follows immediatly from the sum of terms of a geometric series.

## 3.11
$$
E[R_{t + 1} | S_t = s] = \sum_{a \in \mathcal{A}(s)} \pi (a | s) 
\sum_{s' \in \mathcal{S}} \sum_{r \in \mathcal{R}} p(s', r | a, s) \; r
$$

## 3.12
$$
\begin{aligned}
v_{\pi} (s) &= E_{\pi}[G_t | S_t = s] \\
&= E_{\pi}[E_{\pi}[G_t | S_t = s, A_t = a]] \\
&= E_{\pi}[q_{\pi}(s, a)] \\
&= \sum_{a \in \mathcal{A}} q_{\pi}(s, a) \pi(a)
\end{aligned}
$$

## 3.13
$$
\begin{align*}
q_{\pi} (s, a)
    &= E_{\pi} [\sum_{k = 0}^{\infty} \gamma^k R_{t + k + 1} | S_t= s, A_t = a]\\
    &= E_{\pi} [R_{t + 1} | S_t=s, A_t=a]
        + E_{\pi} [\sum_{k = 1}^{\infty} \gamma^k R_{t + k + 1} | S_t= s, A_t = a] \\
\end{align*}
\\
\text{
    Expanding the expectation for the first term and using the law of total 
    expectation for the second term
}\\
\begin{align*}
q_{\pi} (s, a)
    &= \sum_{r \in \mathcal{R}} p(r | S_t = s, A_t=a) \;r\;
        + E_{\pi} [E_{\pi} [\sum_{k = 1}^{\infty} \gamma^k R_{t + k + 1} | S_t= s, A_t = a, S_{t+1} = s'']]
\end{align*}
\\
\text{Using the law of total probability for the second term, and using
the Markov property on the second term}
\\
q_{\pi} (s, a)
    = \sum_{r \in \mathcal{R}} \sum_{s' \in \mathcal{S}} p(r, s' | S_t = s, A_t=a) \;r\;
        + E_{\pi} [E_{\pi} [\sum_{k = 1}^{\infty} \gamma^k R_{t + k + 1} |  S_{t+1} = s'']]
\\
q_{\pi} (s, a)
    = \sum_{r \in \mathcal{R}} \sum_{s' \in \mathcal{S}} p(r, s' | S_t = s, A_t=a) \;r\;
        + E_{\pi} [\gamma \, v(s'')]
\\
q_{\pi} (s, a)
    = \sum_{r \in \mathcal{R}} \sum_{s' \in \mathcal{S}} p(r, s' | S_t = s, A_t=a) \;r\;
        + \gamma \, v(s'')
$$

When important step is the use of the law of total expectation, when going from
$E_{\pi} [\sum_{k = 1}^{\infty} \gamma^k R_{t + k + 1} | S_t= s, A_t = a]$ to
$E_{\pi} [E_{\pi}[\sum_{k = 1}^{\infty} \gamma^k R_{t + k + 1} | S_t= s, A_t = a, S_{t + 1} = s'']]$
we need to make sure that $\pi$ captures the randomness that leads to the
choice of $s''$. We note that the choice, by the definition in the book,
the subscript $\pi$ means the randomness when the agent follows policy $\pi$.
This captures two sorts of randomness; randomness due to the policy itself
(how the agent chooses the next action given the current state), and randomness
due to the dynamic (given a state and an action, what is the next state).
The second source of randomness is the one we use in our application of the law
of total expectation; given state $S_t = s$ and action $A_t = a$, the
randonmness of the dynamics dictates what $S_{t + 1}$ should be.

## 3.14

$$
v_{\pi}(s) = \sum_a \pi(a|s) \sum_{s', r} p(s', r | s, a) [r + \gamma v_{\pi}(s')]
$$
$$
0.7 = \frac{1}{4} * 1 (0 + 0.9 * 2.3) + \frac{1}{4} * 1 (0 + 0.9 * 0.4)
    + \frac{1}{4} * 1 (0 + 0.9 *0.7) + \frac{1}{4} * 1 * (0 + 0.9 * (-0.4))
    = 0.675
$$