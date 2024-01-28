import tkinter as tk
import math

def draw_ring(canvas, center_x, center_y, radius, num_arcs, arc_width):
    arc_angle = 360 / num_arcs
    start_angle = 0
    for _ in range(num_arcs):
        canvas.create_arc(center_x - radius, center_y - radius, center_x + radius, center_y + radius,
                          start=start_angle, extent=arc_angle, outline="red", width=arc_width)
        start_angle += arc_angle

root = tk.Tk()
root.geometry("1000x1000")

C = tk.Canvas(root, bg="black", height=900, width=900)

# Define parameters for the ring
center_x = 450
center_y = 450
radius = 400
num_arcs = 10
arc_width = 30

# Draw the ring
draw_ring(C, center_x, center_y, radius, num_arcs, arc_width)

C.pack(side="top", padx=50, pady=50)
root.mainloop()
