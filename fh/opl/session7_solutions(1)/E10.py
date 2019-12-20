from graphics import GraphicsWindow
from math import sqrt

def sierpinski(canvas, x, y, size, depth = 8, encompass = False):
    if encompass:
        # Draw encompassing triangle
        canvas.setColor("black")
        points = [x, y, x + size / 2, y + size * sqrt(3) / 2, x - size / 2, y + size * sqrt(3) / 2]
        canvas.drawPoly(*points)

    if depth == 0:
        return

    # Draw inner triangle
    points = [ x - (size / 4), y + size / 2 * sqrt(3) / 2,
               x + (size / 4), y + size / 2 * sqrt(3) / 2,
               x, y + size * sqrt(3) / 2 ]
    canvas.setFill("white")
    canvas.drawPoly(*points)

    # Recursive calls
    sierpinski(canvas, x - size / 4, y + size / 2 * sqrt(3) / 2, size / 2, depth - 1)
    sierpinski(canvas, x + size / 4, y + size / 2 * sqrt(3) / 2, size / 2, depth - 1)
    sierpinski(canvas, x, y, size / 2, depth - 1 )

def start_sierpinski(window, depth = 8):
    canvas = window.canvas()
    canvas.setBackground("white")
    size = min(canvas.width(), canvas.height() * 2 / sqrt(3))
    x = size / 2
    y = (canvas.height() - size * sqrt(3) / 2 ) / 2


    sierpinski(canvas, x, y, size, depth, True)

win = GraphicsWindow(800, 800)
start_sierpinski(win)
win.wait()
