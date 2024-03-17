from operator import add, eq, mul
from typing import Any, Callable, Dict, Iterable, Tuple
from hw_3.matrix_mixin import MatrixProtocol


def _bin_op(x: list[list], y: list[list], value_op: Callable[[Any, Any], Any]) -> list[list]:
    res_inner = [[value_op(x_v, y_v) for x_v, y_v in zip(x_row, y_row)] for x_row, y_row in zip(x, y)]
    return res_inner


class MatrixHashMixin:
    def __hash__(self: MatrixProtocol) -> int:
        """sum all elements"""
        hash_sum = sum(sum(row) for row in self._data)
        return hash(hash_sum)

    def __eq__(self: MatrixProtocol, other: object) -> bool:
        if not isinstance(other, Matrix) or self._width != other.width or self._height != other.height:
            return False
        return all(all(row) for row in _bin_op(self._data, other._data, eq))

    def __neq__(self: MatrixProtocol, other: object) -> bool:
        return not (self == other)


class Matrix(MatrixHashMixin):
    is_hashing = True
    mul_cache: Dict[Tuple[int, int], "Matrix"] = dict()

    def __init__(self, inner: Iterable[Iterable[Any]]):
        self._data = list(list(row) for row in inner)
        self._width = len(self._data[0]) if len(self._data) > 0 else 0
        self._height = len(self._data) if self._width > 0 else 0
        self.__hash__ = super().__hash__

    @property
    def height(self):
        return self._height

    @property
    def width(self):
        return self._width

    def __add__(self, other: "Matrix") -> "Matrix":
        if self.height != other.height or self.width != other.width:
            raise ValueError()
        return Matrix(_bin_op(self._data, other._data, add))

    def __mul__(self, other: "Matrix") -> "Matrix":
        if self.height != other.height or self.width != other.width:
            raise ValueError()
        return Matrix(_bin_op(self._data, other._data, mul))

    def _matmul(self, other: "Matrix") -> "Matrix":
        if self.width != other.height:
            raise ValueError(f"{self.width} != {other.height}")
        result = [[0 for _ in range(other.width)] for _ in range(self.height)]
        for i in range(self.height):
            for j in range(other.width):
                for k in range(self.width):
                    result[i][j] += self._data[i][k] * other._data[k][j]
        return Matrix(result)
    
    def __matmul__(self, other: "Matrix") -> "Matrix":
        if self.__class__.is_hashing:
            key = (hash(self), hash(other))
            mul_cache = self.__class__.mul_cache
            if key not in mul_cache:
                value = self._matmul(other)
                mul_cache[key] = value
            else:
                value = mul_cache[key]
            return value
        return self._matmul(other)
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({repr(self._data)})"

    def __str__(self) -> str:
        return "\n".join("\t".join(map(str, row)) for row in self._data)
