import pandas as pd
import numpy as np

import statistics as st

chat_id = 270620880 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    n = len(x)
    er = np.random.laplace(0, 1, n)
    new = x + er
    return new.mean()/(58**2)
