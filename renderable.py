from abc import abstractmethod
import numpy as np
import cairo


class Renderable:
    @abstractmethod
    def render(self, context: cairo.Content, position: np.float64 = 0.0, scale: np.float64 = 1.0):
        pass
