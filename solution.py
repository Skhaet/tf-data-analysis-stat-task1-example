import pandas as pd
import numpy as np

import statistics as s

chat_id = 270620880 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:

    return s.median(x)/(58**2)
