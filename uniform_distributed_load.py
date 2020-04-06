import cairo
import numpy as np
from load import Load
from renderable import Renderable


class UniformDistributedLoad(Load):
    _length: np.float64
    _force: np.float64

    def __init__(self, length: np.float64, force: np.float64):
        self._length = length
        self._force = force

    def load(self, position):
        return np.piecewise(position,
                            [position < 0, 0 < position <= self._length, position > self._length],
                            [0, self._force, 0]
                            )


class RenderableUniformDistributedLoad(UniformDistributedLoad, Renderable):
    def render(self, context: cairo.Context, position: np.float64 = 0.0, scale: np.float64 = 1.0):
        context.rectangle(position, 0.4, self._length * scale, 0.05)
