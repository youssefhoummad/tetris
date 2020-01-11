import tkinter as tk
from const import *

window = tk.Tk()
window.title("Tetris")
window.geometry("400x600")
window.resizable(0, 0)


canvas = tk.Canvas(window, width=SURFACE_WIDTH, height=SURFACE_HEIGHT, bg='gray')
canvas.pack()

for i in range(20):
    canvas.create_line(BLOCK_SIZE * i, 0, BLOCK_SIZE * i, SURFACE_HEIGHT, fill='white')
for i in range(30):
    canvas.create_line(0, BLOCK_SIZE * i, SURFACE_WIDTH, BLOCK_SIZE * i, fill='white')

# test
points = [0, 0, B, 0, B, B, 2*B, B, 2*B, 2*B, 3*B, 2*B, 0, 2*B] 
shape = canvas.create_polygon(points, fill=SHAPES_FILL[3])
print(shape)

def draw_shape(shape):
    global canvas
    
   
    
    return shape


window.mainloop()
