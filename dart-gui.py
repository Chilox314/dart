import tkinter as tk

root = tk.Tk()

root.geometry("1000x1000")

C = tk.Canvas(root,bg="black", height=900, width=900)

coord_double = 15, 15, 885, 885
coord_triple = 195, 195, 705, 705
coord_outer = 105, 105, 795, 795
coord_inner = 305, 305, 595, 595 

for i in range(10):
    C.create_arc(coord_double, start=36*i+9, extent=18, outline="red", style=tk.ARC, width=30)
    C.create_arc(coord_double, start=36*i+18+9, extent=18, outline="green", style=tk.ARC, width=30)

    C.create_arc(coord_outer, start=36*i+9, extent=18, outline="black", style=tk.ARC, width=150)
    C.create_arc(coord_outer, start=36*i+18+9, extent=18, outline="white", style=tk.ARC, width=150)

    C.create_arc(coord_triple, start=36*i+9, extent=18, outline="red", style=tk.ARC, width=30)
    C.create_arc(coord_triple, start=36*i+18+9, extent=18, outline="green", style=tk.ARC, width=30)

    C.create_arc(coord_inner, start=36*i+9, extent=18, outline="black", style=tk.ARC, width=195)
    C.create_arc(coord_inner, start=36*i+18+9, extent=18, outline="white", style=tk.ARC, width=195)
     
C.create_arc(415,415,485,485,start=0,extent=359.9999, outline="green",style=tk.ARC, width=30)
C.create_oval(430,430,470,470,fill="red")

C.pack(side="top", padx=50, pady=50)

root.mainloop()