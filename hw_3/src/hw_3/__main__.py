import numpy as np

from hw_3.matrix import Matrix

np.random.seed(0)
x = Matrix(np.random.randint(0, 10, (10, 10)).tolist())
y = Matrix(np.random.randint(0, 10, (10, 10)).tolist())

print(f"x:\n{x}")
print(f"y:\n{y}")
print(f"x + y:\n{x + y}")
