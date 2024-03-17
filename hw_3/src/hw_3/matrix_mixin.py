from typing import Any, Iterable, Protocol
import numpy as np


class MatrixProtocol(Protocol):
    @property
    def _data(self) -> list[list]: ...
    @property
    def _width(self) -> int: ...
    @property
    def _height(self) -> int: ...


class MatrixToFileMixin:
    def save_to_file(self: MatrixProtocol, filename) -> None:
        with open(filename, "w") as f:
            for row in self._data:
                for v in row:
                    f.write(str(v))
                    f.write(" ")
                f.write("\n")


class MatrixDisplayMixin:
    def __str__(self: MatrixProtocol) -> str:
        return "\n".join(["\t".join(map(str, row)) for row in self._data])


class MatrixPropertiesMixin:
    @property
    def width(self: MatrixProtocol) -> int:
        return self._width

    @property
    def height(self: MatrixProtocol) -> int:
        return self._height


class MatrixFromMixin(
    np.lib.mixins.NDArrayOperatorsMixin, MatrixDisplayMixin, MatrixToFileMixin, MatrixPropertiesMixin
):
    def __init__(self, inner: Iterable[Iterable[Any]]):
        self._data = list(list(row) for row in inner)
        self._width = len(self._data[0]) if len(self._data) > 0 else 0
        self._height = len(self._data) if self._width > 0 else 0

    def __array_ufunc__(self, ufunc, method, *inputs, **kwargs):
        for x in inputs:
            if not isinstance(x, MatrixFromMixin):
                return NotImplemented
        inputs = tuple(x._data for x in inputs)
        result = getattr(ufunc, method)(*inputs, **kwargs)
        return type(self)(result)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({repr(self._data)})"
