import cairo
import numpy as np

from arrow import Arrow
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

    def shear_stress(self, position):
        return np.piecewise(position, [position < 0, position >= 0], [0, self._force])


class RenderablePointLoad(PointLoad, Renderable):
    def __init__(self, force: np.float64):
        super().__init__(force)

    def render(self, context: cairo.Context, position: np.float64 = 0, scale: np.float64 = 1.0):
        Arrow.draw_arrow(context, position, 0.35, position, 0.45)
