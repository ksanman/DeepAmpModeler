import numpy as np

# dataset creation function
def create_dataset(source: np.ndarray, target: np.ndarray, lookback = 1):
    data_x, data_y = [], []
    for i in range(len(source) - lookback - 1):
        a = source[i:(i + lookback), 0]
        data_x.append(a)
        data_y.append(target[i + lookback, 0])
    return np.array(data_x), np.array(data_y)