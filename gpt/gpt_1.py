import tkinter as tk
import math

root = tk.Tk()
root.geometry("1000x1000")

C = tk.Canvas(root, bg="black", height=900, width=900)

# Define coordinates for arcs
center_x = 450
center_y = 450
radius = 400
arc_width = 30

for i in range(10):
    start_angle = math.radians(36 * i + 9)
    extent_angle = math.radians(18)

    # Outer double arcs
    outer_x1 = center_x + radius * math.cos(start_angle)
    outer_y1 = center_y + radius * math.sin(start_angle)
    outer_x2 = center_x + radius * math.cos(start_angle + extent_angle)
    outer_y2 = center_y + radius * math.sin(start_angle + extent_angle)
    C.create_arc(outer_x1, outer_y1, outer_x2, outer_y2, start=0, extent=360, outline="red", width=arc_width)

    outer_x3 = center_x + (radius + arc_width) * math.cos(start_angle)
    outer_y3 = center_y + (radius + arc_width) * math.sin(start_angle)
    outer_x4 = center_x + (radius + arc_width) * math.cos(start_angle + extent_angle)
    outer_y4 = center_y + (radius + arc_width) * math.sin(start_angle + extent_angle)
    C.create_arc(outer_x3, outer_y3, outer_x4, outer_y4, start=0, extent=360, outline="green", width=arc_width)

    # Inner triple arcs
    inner_x1 = center_x + (radius - 2 * arc_width) * math.cos(start_angle)
    inner_y1 = center_y + (radius - 2 * arc_width) * math.sin(start_angle)
    inner_x2 = center_x + (radius - 2 * arc_width) * math.cos(start_angle + extent_angle)
    inner_y2 = center_y + (radius - 2 * arc_width) * math.sin(start_angle + extent_angle)
    C.create_arc(inner_x1, inner_y1, inner_x2, inner_y2, start=0, extent=360, outline="red", width=arc_width)

    inner_x3 = center_x + (radius - 3 * arc_width) * math.cos(start_angle)
    inner_y3 = center_y + (radius - 3 * arc_width) * math.sin(start_angle)
    inner_x4 = center_x + (radius - 3 * arc_width) * math.cos(start_angle + extent_angle)
    inner_y4 = center_y + (radius - 3 * arc_width) * math.sin(start_angle + extent_angle)
    C.create_arc(inner_x3, inner_y3, inner_x4, inner_y4, start=0, extent=360, outline="green", width=arc_width)

C.pack(side="top", padx=50, pady=50)
root.mainloop()
