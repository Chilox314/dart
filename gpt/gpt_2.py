import tkinter as tk
import math

def draw_arc(canvas, center_x, center_y, radius, start_angle, end_angle, outline, width):
    start_x = center_x + radius * math.cos(math.radians(start_angle))
    start_y = center_y + radius * math.sin(math.radians(start_angle))
    end_x = center_x + radius * math.cos(math.radians(end_angle))
    end_y = center_y + radius * math.sin(math.radians(end_angle))
    canvas.create_arc(center_x - radius, center_y - radius, center_x + radius, center_y + radius,
                      start=start_angle, extent=end_angle - start_angle, outline=outline, width=width)

root = tk.Tk()
root.geometry("1000x1000")

C = tk.Canvas(root, bg="black", height=900, width=900)

# Define coordinates for arcs
center_x = 450
center_y = 450
radius = 400
arc_width = 30
angle_increment = 36

for i in range(10):
    start_angle = i * angle_increment + 9
    end_angle = start_angle + 18

    # Draw outer double arcs
    draw_arc(C, center_x, center_y, radius, start_angle, end_angle, "red", arc_width)
    draw_arc(C, center_x, center_y, radius, start_angle + 18, end_angle + 18, "green", arc_width)

    # Draw inner triple arcs
    draw_arc(C, center_x, center_y, radius - arc_width, start_angle, end_angle, "red", arc_width)
    draw_arc(C, center_x, center_y, radius - 2 * arc_width, start_angle, end_angle, "green", arc_width)

C.pack(side="top", padx=50, pady=50)
root.mainloop()
