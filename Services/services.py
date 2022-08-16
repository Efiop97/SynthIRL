import numpy as np

def Lin_interpolation(x, y):
    truncated_y = int(np.floor(y))
    next_y = (truncated_y + 1) % x.shape[0]

    next_y_weight = y - truncated_y
    truncated_y_weight = 1 - next_y_weight

    return truncated_y_weight * x[truncated_y] + next_y_weight * x[next_y]







