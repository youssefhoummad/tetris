import tkinter as tk
import time
from const import *


window = tk.Tk()
window.title("Tetris")
window.geometry("400x600")
window.resizable(0, 0)


canvas = tk.Canvas(window, width=SURFACE_WIDTH, height=SURFACE_HEIGHT, bg='gray')
canvas.pack()

def draw_grid():
    for i in range(20):
        canvas.create_line(BLOCK_SIZE * i, 0, BLOCK_SIZE * i, SURFACE_HEIGHT, fill='white')
    for i in range(30):
        canvas.create_line(0, BLOCK_SIZE * i, SURFACE_WIDTH, BLOCK_SIZE * i, fill='white')

def draw_shape(shape):
    "shape is int from 0 to 5"
    global canvas
    fill = SHAPES_FILL[shape]
    shape = SHAPES[shape][0]
    for x, row in enumerate(shape):
        for y, col in enumerate(row):
            if col == '0':
                canvas.create_rectangle(y*B, x*B, B + B*y, B + B*x, fill=fill,
                tags='current')
    return

def rotate_shape(shape, angle=90):
    "shape is obj canavas"
    return

def move_shape(speed=0.5):
    "shape is obj canavas"
    locked = False
    for _ in range(30):
        canvas.move("current", 0, B)
        canvas.update()
        time.sleep(speed)
        # some condition
        if _ == 15:
            locked = True
        if locked:
            break


draw_grid()
draw_shape(5)
move_shape()


window.mainloop()
