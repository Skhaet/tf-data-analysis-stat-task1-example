import pandas as pd
import numpy as np

import statistics as st

chat_id = 270620880 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:

    line = st.median(x)
    n = 0
    s = 0
    for i in range (len(x)):
        if x[i]<=line:
            s = s +x[i]
            n = n+1
    k = (s/n)/(58**2)
    return k # Ваш ответ
