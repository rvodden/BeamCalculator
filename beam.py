import abc
from typing import TypeVar, Generic

import cairo
import numpy as np
from collections import deque
from load import Load
from renderable import Renderable


class Beam:
    _loads: deque
    _supports: deque
    _length: np.float64

    def __init__(self, length: np.float64):
        self._loads = deque()
        self._length = length

    def add_load(self, load: Load, position: np.float64):
        self._loads.append(Positional(load, position))

    def shear_stress(self, position: np.float64):
        stress = 0
        for positional_load in self._loads:
            stress += positional_load.thing.shear_stress(position - positional_load.position)
        return stress


class RenderableBeam(Beam, Renderable):
    def render(self, context: cairo.Context, position: np.float64 = 0.0, scale: np.float64 = 1.0):
        context.rectangle(0, 0.45, 1, 0.1)
        for positional_load in self._loads:
            load = positional_load.thing
            if issubclass(load.__class__, Renderable):
                load.render(context, positional_load.position / self._length, 1 / self._length)


T = TypeVar('T')


class Positional(Generic[T]):
    _position: np.float64
    _thing: T

    def __init__(self, thing: T, position: np.float64):
        self._thing = thing
        self._position = position

    @property
    def position(self):
        return self._position

    @property
    def thing(self) -> T:
        return self._thing
