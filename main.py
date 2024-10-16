from graphics import *

def main():
    win = Window(800, 600)
    line = Line(Point(300, 300), Point(500,200))
    win.draw_line(line, "#cbff2c")
    win.wait_for_close()



main()