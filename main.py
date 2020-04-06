import cairo
import numpy as np
import matplotlib.pyplot as plt
from beam import Beam, RenderableBeam
from point_load import RenderablePointLoad
from uniform_distributed_load import RenderableUniformDistributedLoad

LENGTH = 10


def main() -> int:
    beam: RenderableBeam = RenderableBeam(LENGTH)
    beam.add_load(RenderablePointLoad(5.0), 5)
    beam.add_load(RenderableUniformDistributedLoad(2.0, 5.0), 2)

    __HEIGHT: int = 768
    __WIDTH: int = 768

    surface = cairo.ImageSurface(cairo.Format.RGB24, __WIDTH, __HEIGHT)
    context = cairo.Context(surface)
    context.set_source_rgb(1, 1, 1)
    context.set_line_width(0.001)

    scale_factor = min(__WIDTH, __HEIGHT) * 0.8
    context.scale(scale_factor, scale_factor)
    context.translate(0.1, 0.1)

    beam.render(context)
    context.stroke()
    surface.write_to_png("example.png")

    fig: plt.Figure = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')

    x = np.linspace(0, LENGTH, 10 * LENGTH)
    y = np.array(beam.shear_stress(x))
    plt.plot(x, y, 'r')
    plt.show()

    return 0


if __name__ == "__main__":
    main()
