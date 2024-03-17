from operator import add, eq, mul
from typing import Any, Callable, Iterable
from pprint import pformat

class Matrix:
    def __init__(self, inner: Iterable[Iterable[Any]]):
        self._data = list(list(row) for row in inner)
        self._width = len(self._data[0]) if len(self._data) > 0 else 0
        self._height = len(self._data) if self._width > 0 else 0

    @property
    def height(self):
        return self._height

    @property
    def width(self):
        return self._width

    @classmethod
    def _bin_op(cls, x: list[list], y: list[list], value_op: Callable[[Any, Any], Any]) -> list[list]:
        res_inner = [[value_op(x_v, y_v) for x_v, y_v in zip(x_row, y_row)] for x_row, y_row in zip(x, y)]
        return res_inner

    def __add__(self, other: "Matrix") -> "Matrix":
        if self.height != other.height or self.width != other.width:
            raise ValueError()
        return Matrix(self.__class__._bin_op(self._data, other._data, add))

    def __mul__(self, other: "Matrix") -> "Matrix":
        if self.height != other.height or self.width != other.width:
            raise ValueError()
        return Matrix(self.__class__._bin_op(self._data, other._data, mul))

    def __matmul__(self, other: "Matrix") -> "Matrix":
        if self.width != other.height:
            raise ValueError(f"{self.width} != {other.height}")
        result = [[0 for _ in range(other.width)] for _ in range(self.height)]
        for i in range(self.height):
            for j in range(other.width):
                for k in range(self.width):
                    result[i][j] += self._data[i][k] * other._data[k][j]
        return Matrix(result)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Matrix) or self.width != other.width or self.height != other.height:
            return False
        return all(all(row) for row in self.__class__._bin_op(self._data, other._data, eq))

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({repr(self._data)})"
    
    
    def __str__(self) -> str:
        return "\n".join("\t".join(map(str, row)) for row in self._data)
