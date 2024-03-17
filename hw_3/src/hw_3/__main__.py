import numpy as np

from hw_3.matrix_mixin import MatrixFromMixin

np.random.seed(0)
x = MatrixFromMixin(np.random.randint(0, 10, (10, 10)).tolist())

print(f"x:\n{x}")
print(f"str(x):\n{str(x)}")
print(f"x.width: {x.width}")
print(f"x.height: {x.height}")

x.save_to_file("temp.txt")