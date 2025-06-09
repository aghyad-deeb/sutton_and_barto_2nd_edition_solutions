# %%
import numpy as np
from enum import Enum
import matplotlib.pyplot as plt

class StepSizeType(Enum):
    SAMPLE_AVERAGE = 0
    CONSTANT = 1

class ActionValueMethod(Enum):
    GREEDY = 0
    EPSILON_GREEDY = 1

seed = 42
G = np.random.default_rng(seed=seed)

def sample_normal(mean, std):
    return G.normal(loc=mean, scale=std)

def greedy(qs):
    # `qs` is the updated step-size parameter
    qs_np = np.array(qs)
    max_arr = qs_np.argmax(axis=-1, keepdims=True)
    return G.choice(max_arr)

def epsilon_greedy(qs, epsilon=0.1):
    # `qs` is the updated step-size parameter
    if G.binomial(n=1, p=epsilon) == 1:
        return G.choice(list(range(len(qs))))
    else:
        qs_np = np.array(qs)
        max_arr = qs_np.argmax(axis=-1, keepdims=True)
        return G.choice(max_arr)

def update_stepsize_sample_average(
        qs, action, reward, num_action_picks
    ):
    qs[action] += 1/num_action_picks[action] * (reward - qs[action])
    return qs

def update_stepsize_constant(qs, action, reward, factor):
    qs[action] += factor * (reward - qs[action])
    return qs

def update_q_stars(q_stars):
    for i, elm in enumerate(q_stars):
        q_stars[i] += sample_normal(mean=0, std=0.01)
    return q_stars

def step(
        qs, q_stars, step_size_type: StepSizeType, num_action_picks,
        constant_stepsize_factor, action_value_method: ActionValueMethod
    ):
    if action_value_method == ActionValueMethod.GREEDY:
        action = greedy(qs)
    elif action_value_method == ActionValueMethod.EPSILON_GREEDY:
        action = epsilon_greedy(qs)
    num_action_picks[action] += 1
    # reward = sample_normal(mean=q_stars[action], std=1)
    #!
    reward = sample_normal(mean=q_stars[action], std=0.0000001)
    optimal = greedy(q_stars)
    if q_stars[optimal] == q_stars[action]:
        optimal = action
    if step_size_type == StepSizeType.SAMPLE_AVERAGE:
        qs = update_stepsize_sample_average(
            qs, action, reward, num_action_picks
        )
    elif step_size_type == StepSizeType.CONSTANT:
        qs = update_stepsize_constant(
            qs, action, reward, constant_stepsize_factor
        )
    #!
    q_stars = update_q_stars(q_stars)
    return dict(
        qs=qs.copy(), q_stars=q_stars.copy(), action=action, reward=reward, optimal=optimal
    )

def plot_reward(results):
    for action_value_method in [ActionValueMethod.GREEDY, ActionValueMethod.EPSILON_GREEDY]:
        for step_size_type in [StepSizeType.SAMPLE_AVERAGE, StepSizeType.CONSTANT]:
            runs = np.array(results[action_value_method][step_size_type])
            rewards_list = [[step["reward"] for step in run] for run in runs]
            rewards = np.array(rewards_list)
            rewards_averages = rewards.mean(axis=0)
            plt.plot(rewards_averages, label=f"{step_size_type.name}")
        plt.title(f"Rewards over Time {action_value_method.name}")
        plt.xlabel("Timestep")
        plt.ylabel("Reward")
        plt.legend()
        plt.show()

def plot_optimal(results):
    for action_value_method in [ActionValueMethod.GREEDY, ActionValueMethod.EPSILON_GREEDY]:
        for step_size_type in [StepSizeType.SAMPLE_AVERAGE, StepSizeType.CONSTANT]:
            runs = np.array(results[action_value_method][step_size_type])
            is_optimal_arr = np.array([
                [step["action"] == step["optimal"] for step in run]
                for run in runs
            ])
            is_optimal_avg = is_optimal_arr.mean(axis=0)
            plt.plot(is_optimal_avg, label=f"{step_size_type.name}")
        plt.title(
            f"Fraction of optimal action over Time {action_value_method.name}"
        )
        plt.xlabel("Timestep")
        plt.ylabel("Fraction of Optimal Action")
        plt.legend()
        plt.show()


def main():
    results = dict()
    runs = 10*4
    for action_value_method in [ActionValueMethod.GREEDY, ActionValueMethod.EPSILON_GREEDY]:
    # for action_value_method in [ActionValueMethod.EPSILON_GREEDY]:
        results[action_value_method] = dict()
        for step_size_type in [StepSizeType.SAMPLE_AVERAGE, StepSizeType.CONSTANT]:
        # for step_size_type in [StepSizeType.SAMPLE_AVERAGE]:
            results[action_value_method][step_size_type] = list()
            for i in range(runs):
                q_stars = [0 for _ in range(10)]
                #!
                # q_stars = [0.2, 0.3, 0.5, 0.1, 0.2, -1, -0.1, -0.3, 0.25, 0.49]
                qs = [0 for _ in range(10)]
                num_action_picks = [0 for _ in range(10)]
                num_steps = 10**4 
                constant_stepsize_factor = 0.1
                results[action_value_method][step_size_type].append(list())
                curr_list = results[action_value_method][step_size_type][i]
                for i in range(1, num_steps + 1):
                    curr_list.append(
                        step(
                            qs, q_stars, step_size_type, num_action_picks,
                            constant_stepsize_factor, action_value_method
                        )
                    )
    # display(results.keys())
    # display([results[key].keys() for key in results.keys()])
    plot_reward(results)
    plot_optimal(results)
    return

if __name__ == "__main__":
    main()
# %%
