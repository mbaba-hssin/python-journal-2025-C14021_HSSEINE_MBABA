# Exercice 3.5 : Moyenne mobile
import numpy as np

def moving_average(u):
    return (u[:-2] + u[1:-1] + u[2:]) / 3

# Test
print(moving_average(np.array([10, 20, 30, 40, 50])))  # [20. 30.]
