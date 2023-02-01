import numpy as np
import pandas as pd

def read_data(filepath):
    """Read data from csv
    Args:
        filepath: path of file
        
    Return:
        array of cpu and memory
    """
    with open(filepath) as f:
        r = pd.read_csv(f, delimiter=",")
        cpu_memory_array = np.array(r[["cpus", "memory"]])
    return cpu_memory_array


def cal_reward(cur_state_cpu, cur_state_memory, cur_act_cpu, cur_act_memory):
    """Get current state cpu/memory of request, current machine cpu/memory of request
    Args:
        cur_state_cpu: CPU of request in the current state
        cur_state_memory: memory of request in the current state
        cur_act_cpu: CPU of capacity in the current action
        cur_act_memory: memory of capacity in the current action
    
    Return:
        reward
    """
    per_cpu = cur_state_cpu / cur_act_cpu
    per_memory = cur_state_memory / cur_act_memory
    reward = 0
    
    if per_cpu > 1 or per_memory > 1:
        reward = -1
    else:
        reward = per_cpu + per_memory
    
    return reward
    