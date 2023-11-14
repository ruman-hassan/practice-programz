import cairo
import math

 # Set up surface
surface = cairo.ImageSurface(cairo.FORMAT_RGB24, 600, 400)
ctx = cairo.Context(surface)
ctx.set_source_rgb(0,0,0)
ctx.paint()

def redarc(ctx):
   ctx.arc(200, 300, 50, 3*math.pi/2, math.pi/2)
   ctx.new_sub_path()
   ctx.arc(250, 250, 50, 0*math.pi, math.pi)
   ctx.set_source_rgb(1, 0, 0)
   ctx.stroke()

def bluearc(ctx):
    ctx.arc_negative(300, 300, 50, math.pi/2, 3*math.pi/2)
    ctx.new_sub_path()
    ctx.arc(250, 350, 50, math.pi, 0*math.pi)
    ctx.set_source_rgb(0,0,1)
    ctx.stroke()
   
redarc(ctx)
bluearc(ctx)
ctx.set_line_width(3)
surface.write_to_png("colourarc.png")