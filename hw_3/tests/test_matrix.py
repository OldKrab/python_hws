from hw_3.matrix import Matrix
import numpy as np
import unittest
import logging

class Test_Matrix(unittest.TestCase):
    def test_simple_add(self):
        x = Matrix([[1]])
        y = Matrix([[2]])
        assert x + y == Matrix([[3]])

    def test_complex_add(self):
        x = Matrix(
            [
                [1, 2, 3],
                [-1, -2, -3],
            ]
        )
        y = Matrix(
            [
                [-1, -2, -3],
                [1, 2, 3],
            ]
        )

        res = Matrix(
            [
                [0, 0, 0],
                [0, 0, 0],
            ]
        )
        self.assertEqual(x + y, res)

    def test_wrong_dims_add(self):
        x = Matrix([[1, 2]])
        y = Matrix([[-1, -2, -3]])

        with self.assertRaises(ValueError):
            _ = x + y

        x = Matrix([[1, 2]])
        y = Matrix(
            [
                [-1, -2],
                [-1, -2],
            ]
        )

        with self.assertRaises(ValueError):
            _ = x + y

    def test_simple_mul(self):
        x = Matrix([[2]])
        y = Matrix([[2]])
        self.assertEqual(x * y, Matrix([[4]]))

    def test_complex_mul(self):
        x = Matrix(
            [
                [1, 2, 3],
                [-1, -2, -3],
            ]
        )
        y = Matrix(
            [
                [-1, -2, -3],
                [1, 2, 3],
            ]
        )

        res = Matrix(
            [
                [-1, -4, -9],
                [-1, -4, -9],
            ]
        )
        self.assertEqual(x * y, res)

    def test_wrong_dims_mul(self):
        x = Matrix([[1, 2]])
        y = Matrix([[-1, -2, -3]])

        with self.assertRaises(ValueError):
            _ = x * y

        x = Matrix([[1, 2]])
        y = Matrix(
            [
                [-1, -2],
                [-1, -2],
            ]
        )

        with self.assertRaises(ValueError):
            _ = x * y

    def test_matmul(self):
        x = Matrix(
            [
                [1, 2, 3],
                [4, 5, 6],
            ]
        )
        y = Matrix(
            [
                [7, 8],
                [9, 10],
                [11, 12],
            ]
        )
        res = Matrix(
            [
                [58, 64],
                [139, 154],
            ]
        )
        self.assertEqual(x @ y, res)

    def test_empty_matmul(self):
        self.assertEqual(Matrix([[]]) @ Matrix([[]]), Matrix([[]]))

    def test_wrong_dims_matmul(self):
        x = Matrix(
            [
                [1, 2, 3],
                [4, 5, 6],
            ]
        )
        y = Matrix(
            [
                [1, 2, 3],
                [4, 5, 6],
            ]
        )
        with self.assertRaises(ValueError):
            _ = x @ y

if __name__ == "__main__":
    unittest.main()
