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