import cairo
from beam import Beam, RenderableBeam
from point_load import RenderablePointLoad


def main() -> int:
    beam = RenderableBeam(10.0)
    beam.add_load(RenderablePointLoad(5.0), 5.0)
    surface = cairo.ImageSurface(cairo.Format.RGB24, 1024, 768)
    context = cairo.Context(surface)
    context.set_source_rgb(1,1,1)
    context.set_line_width(0.1)

    context.scale(12, 12)

    beam.render(context)
    context.stroke()
    surface.write_to_png("example.png")
    return 0


if __name__ == "__main__":
    main()
