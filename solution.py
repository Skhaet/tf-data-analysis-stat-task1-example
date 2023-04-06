import pandas as pd
import numpy as np


chat_id = 270620880 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    for i in range (len(x)):
        x[i] = (x[i])/(58**2)
    return x.mean() # Ваш ответ
