import cairo
import numpy as np


class Arrow:
    _ARROW_LENGTH = 0.01
    _ARROW_ANGLE = np.deg2rad(15)

    @staticmethod
    def draw_arrow(context: cairo.Context, xs: np.float64, ys: np.float64, xe: np.float64, ye: np.float64):
        angle = np.arctan2(ye - ys, xe - xs)

        x1 = xe + Arrow._ARROW_LENGTH * np.cos(angle - Arrow._ARROW_ANGLE)
        y1 = ye - Arrow._ARROW_LENGTH * np.sin(angle - Arrow._ARROW_ANGLE)
        x2 = xe + Arrow._ARROW_LENGTH * np.cos(angle + Arrow._ARROW_ANGLE)
        y2 = ye - Arrow._ARROW_LENGTH * np.sin(angle + Arrow._ARROW_ANGLE)

        context.move_to(xs, ys)
        context.line_to(xe, ye)
        context.line_to(x1, y1)
        context.move_to(xe, ye)
        context.line_to(x2, y2)
