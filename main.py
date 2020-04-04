import cairo
from beam import Beam, RenderableBeam
from point_load import RenderablePointLoad


def main() -> int:
    beam = RenderableBeam(2.0)
    beam.add_load(RenderablePointLoad(5.0), 0.5)

    __HEIGHT: float = 768
    __WIDTH: float = 1024

    surface = cairo.ImageSurface(cairo.Format.RGB24, __WIDTH, __HEIGHT)
    context = cairo.Context(surface)
    context.set_source_rgb(1,1,1)
    context.set_line_width(0.001)

    scale_factor = min(__WIDTH,__HEIGHT)
    context.translate(__WIDTH/2,__HEIGHT/2)
    context.scale(scale_factor * 0.9, scale_factor * 0.9)

    beam.render(context)
    context.stroke()
    surface.write_to_png("example.png")
    return 0


if __name__ == "__main__":
    main()
