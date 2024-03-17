import numpy as np

from hw_3.matrix import Matrix

A = Matrix([[1, 2], [1, 2]])
C = Matrix([[6, 0], [0, 0]])
B = Matrix([[1, 2], [3, 4]])
D = B


def print_info():
    print(f"A:\n{A}")  
    print(f"B:\n{B}")  
    print(f"C:\n{C}")  
    print(f"D:\n{D}")  
    print(f"A@B:\n{A@B}")  
    print(f"C@D:\n{C@D}")  
    print(f"A@B hash: {hash(A@B)}")  
    print(f"C@D hash: {hash(C@D)}")  

print("With caching")
print_info()
print("\nWithout caching")
Matrix.is_hashing = False
print_info()

print(f"\n(hash(A) == hash(C)) and (A != C) and (B == D) and (AB != CD): {(hash(A) == hash(C)) and (A != C) and (B == D) and (A@B != C@D)}")
