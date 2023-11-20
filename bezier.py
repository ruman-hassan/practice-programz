import cairo


#Setting up the interface
surface = cairo.ImageSurface(cairo.FORMAT_RGB24, 600, 400)
ctx = cairo.Context(surface)
ctx.set_source_rgb(0.8, 0.8, 0.8)
ctx.paint()

ctx.move_to(300, 250)
ctx.curve_to(100, 150, 400, 150, 200, 250)
ctx.line_to(200, 160)
ctx.line_to(300, 160)

ctx.set_line_width(8)
ctx.set_source_rgb(1, 0, 0)

ctx.stroke()

surface.write_to_png("bezier.png")