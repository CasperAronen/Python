import math
import random


def monteCarloPii(n_piste):
    ympyrän_sisä = 0

    for _ in range(n_piste):
        x, y = random.uniform(-1, 1), random.uniform(-1, 1)
        if x**2 + y**2 <= 1:
            ympyrän_sisä += 1
    return 4 * ympyrän_sisä / n_piste

n_piste = 5000000

print(monteCarloPii(n_piste))
print((math.pi))