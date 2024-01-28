import tkinter as tk

def draw_arcs(canvas, coord, colors, widths):
    for i in range(10):
        for j, color in enumerate(colors):
            start_angle = 36 * i + 9 + 18 * j
            canvas.create_arc(coord, start=start_angle, extent=18, outline=color, style=tk.ARC, width=widths[j])

def main():
    root = tk.Tk()
    root.geometry("1000x1000")
    root.title("Optimized Ring Drawing")

    canvas = tk.Canvas(root, bg="black", height=900, width=900)
    canvas.pack(side="top", padx=50, pady=50)

    coord_double = 15, 15, 885, 885
    coord_triple = 195, 195, 705, 705
    coord_outer = 105, 105, 795, 795
    coord_inner = 305, 305, 595, 595 

    colors = ["red", "green", "red", "green"]
    widths = [30, 150, 30, 190]

    draw_arcs(canvas, coord_double, colors, widths)
    draw_arcs(canvas, coord_outer, colors, widths)
    draw_arcs(canvas, coord_triple, colors, widths)
    draw_arcs(canvas, coord_inner, colors, widths)

    root.mainloop()

if __name__ == "__main__":
    main()
