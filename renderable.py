from abc import abstractmethod
import numpy as np
import cairo


class Renderable:
    @abstractmethod
    def render(self, c: cairo.Content):
        pass
