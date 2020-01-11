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



window.mainloop()
