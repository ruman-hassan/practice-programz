import cairo
import math

 # Set up surface
surface = cairo.ImageSurface(cairo.FORMAT_RGB24, 600, 400)
ctx = cairo.Context(surface)
ctx.set_source_rgb(0.8, 0.8, 0.8)
ctx.paint()


def diamond1(ctx):
    ctx.new_sub_path()
    ctx.arc(105, 95, 25, math.pi/2, math.pi)
    ctx.arc(55, 95, 25, 0*math.pi,math.pi/2 )
    ctx.arc(55, 145, 25, 3*math.pi/2,0*math.pi )
    ctx.arc(105, 145, 25, math.pi, 3*math.pi/2)
    ctx.set_source_rgb(1, 0, 0)
    ctx.fill()
    ctx.stroke()


def diamond2(ctx): 
    ctx.new_sub_path()   
    ctx.arc(245, 300, 25, math.pi/2, math.pi)
    ctx.arc(195, 300, 25, 0*math.pi,math.pi/2 )
    ctx.arc(195, 350, 25, 3*math.pi/2,0*math.pi )
    ctx.arc(245, 350, 25, math.pi, 3*math.pi/2)
    ctx.set_source_rgb(1, 0, 0)
    ctx.fill()
    ctx.stroke()

def bigdiamond(ctx): 
    ctx.new_sub_path()   
    ctx.arc(190, 180, 35, math.pi/2, math.pi)
    ctx.arc(120, 180, 35, 0*math.pi,math.pi/2 )
    ctx.arc(120, 250, 35, 3*math.pi/2,0*math.pi )
    ctx.arc(190, 250, 35, math.pi, 3*math.pi/2)
    ctx.set_source_rgb(1, 0, 0)
    ctx.fill()
    ctx.stroke()
    

def roundrect(ctx, x, y, width, height, r):
    ctx.new_sub_path()
    ctx.arc(x+r, y+r, r, math.pi, 3*math.pi/2)
    ctx.arc(x+width-r, y+r, r, 3*math.pi/2, 0)
    ctx.arc(x+width-r, y+height-r, r, 0, math.pi/2)
    ctx.arc(x+r, y+height-r, r, math.pi/2, math.pi)
    ctx.close_path()
    ctx.set_source_rgb(0, 0, 0)
    ctx.stroke()

def letter_A(ctx):
    ctx.move_to(210,350)
    ctx.line_to(220,390)
    ctx.line_to(230,350)
    ctx.new_sub_path()
    ctx.move_to(215,365)
    ctx.line_to(225,365)
    ctx.set_source_rgb(1, 0, 0)
    ctx.stroke()

def letter_B(ctx):
    ctx.move_to(70,90)
    ctx.line_to(80,50)
    ctx.line_to(90,90)
    ctx.new_sub_path()
    ctx.move_to(75,75)
    ctx.line_to(85,75)
    ctx.set_source_rgb(1, 0, 0)
    ctx.stroke()


    

ctx.set_line_width(3)

roundrect(ctx, 50, 40, 200, 360, 25)
diamond1(ctx)
diamond2(ctx)
bigdiamond(ctx)
letter_A(ctx)
letter_B(ctx)



surface.write_to_png("roundrect.png")
