import cairo
import numpy as np
from load import Load
from renderable import Renderable


class PointLoad(Load):
    _force: np.float64

    def __init__(self, force: np.float64):
        self._force = force

    @property
    def load(self, position: np.float64):
        if position == 0:
            return self._force


class RenderablePointLoad(PointLoad, Renderable):
    def __init__(self, force: np.float64):
        super().__init__(force)

    def render(self, c: cairo.Context, position: np.float64):
        c.move_to(position, 10)
        c.line_to(position, 1)
