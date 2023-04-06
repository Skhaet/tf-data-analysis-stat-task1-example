import pandas as pd
import numpy as np


chat_id = 270620880 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    x.sort()
    l = len(x)
    
    if l%2 == 0:
        k = ((x[l//2]+x[l//2 + 1])/2)/(58**2)
    else: k = (x[l//2])/(58**2)
    #for i in range (l):
    #    x[i] = (k)/(58**2)
    
    
    return k # Ваш ответ
