import abc

import cairo
import numpy as np
from collections import deque
from load import Load
from renderable import Renderable


class Beam:
    _loads: deque
    _length: np.float64

    def __init__(self, length: np.float64):
        self._loads = deque()
        self._length = length

    def add_load(self, load: Load, position: np.float64):
        self._loads.append(self.LoadPosition(load, position))

    class LoadPosition:
        _position: np.float64
        _load: Load

        def __init__(self, load: Load, position: np.float64):
            self._load = load
            self._position = position

        @property
        def position(self):
            return self._position

        @property
        def load(self):
            return self._load


class RenderableBeam(Beam, Renderable):
    def render(self, c: cairo.Context):
        c.rectangle(-1.0, -0.1, self._length, 0.1)
        for loadposition in self._loads:
            load = loadposition.load
            if issubclass(load.__class__, Renderable):
                load.render(c, loadposition.position)
