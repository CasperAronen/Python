import numpy as np

import math
#Tehtävä 1

#Tehtävä 1.1
a = 2.493

b = 0.911
print("Tehtävä 1.1 a ja b")
print(np.radians(a))
print(np.radians(b))
print("")
#Tehtävä 1.2

Trad = np.array([137.7, 62.3])

print("Tehtävä 1.2 a ja b")
for i in Trad:
    print(np.radians(i))
print("")
#Tehtävä 1.3

kulmat = [30, 45, 60, 90, 120, 135, 180, 270, 360]
radiaanit = ["π/6", "π/4", "π/3","π/2", "2*π/3", "3*π/4", "π" "3*π/2", "2*π"]

print("Tehtävä 1.3")
for i in kulmat:
    print(f"{i:^9}", end=" ")
print("")
for j in radiaanit:
    print(f"{j:^9}", end=" ")
print("")

#Tehtävä 2

#Tehtävä 2.1
print("")
print("Tehtävä 2 hypotenuusa")
Ak = 1.6
Bk = 2.3

Ck = (Ak ** 2)+(Bk**2)

SqrtCk = math.sqrt(Ck)

print(SqrtCk)