import numpy as np
point = np.zeros((3, 3), int)
k = 0
for i in range(3):
    for j in range(3):
        point[i][j] = k
        k = k + 1
print(point)
point = np.rot90(point, k = 2)
print(point)