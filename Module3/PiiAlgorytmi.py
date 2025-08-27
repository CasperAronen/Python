import random

num_points = int(input("Anna pisteiden määrä: "))

n_circle = 0

for _ in range(num_points):
    x = random.uniform(0, 1)
    y = random.uniform(0, 1)
    dx = x - 0.5
    dy = y - 0.5
    if dx * dx + dy * dy <= 0.25:
        n_circle += 1

pi = 4 * n_circle / num_points
print(f"{pi:.6f}")