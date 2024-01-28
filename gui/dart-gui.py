import tkinter as tk

#Werde der Felder gegen den Uhrzeigersinn
Board_Numbers = ["13","4","18","1","20","5","12","9","14","11","8","16","7","19","3","17","2","15","10","6"]

def move_items(canvas, dx, dy):
    items = canvas.find_all()
    for item in items:
        canvas.move(item, dx, dy)

def check_click(event):
    output_label.config(text="You've hit a " + event.widget.gettags("current")[0])
    

root = tk.Tk()

window_height = 800
window_width = 800

root.geometry(f'{window_height}x{window_width}')

dartboard_width = 600

C = tk.Canvas(root,bg="white", height=dartboard_width+10, width=dartboard_width+10)

coord_double = 10, 10, 590, 590
coord_triple = 140, 140, 460, 460
coord_outer = 75, 75, 525, 525
coord_inner = 205, 205, 395, 395 

for i in range(10):
    C.create_arc(coord_double, start=36*i+9, extent=18, outline="red", style=tk.ARC, width=20, tags="D"+Board_Numbers[2*i])
    C.create_arc(coord_double, start=36*i+18+9, extent=18, outline="green", style=tk.ARC, width=20, tags="D"+Board_Numbers[2*i+1])

    C.create_arc(coord_outer, start=36*i+9, extent=18, outline="black", style=tk.ARC, width=110,tags=Board_Numbers[2*i])
    C.create_arc(coord_outer, start=36*i+18+9, extent=18, outline="white", style=tk.ARC, width=110, tags=Board_Numbers[2*i+1])

    C.create_arc(coord_triple, start=36*i+9, extent=18, outline="red", style=tk.ARC, width=20,tags="T"+Board_Numbers[2*i])
    C.create_arc(coord_triple, start=36*i+18+9, extent=18, outline="green", style=tk.ARC, width=20,tags="T"+Board_Numbers[2*i+1])

    C.create_arc(coord_inner, start=36*i+9, extent=18, outline="black", style=tk.ARC, width=110,tags=Board_Numbers[2*i])
    C.create_arc(coord_inner, start=36*i+18+9, extent=18, outline="white", style=tk.ARC, width=110,tags=Board_Numbers[2*i+1])
     
C.create_arc(270,270,330,330,start=0,extent=359.9999, outline="green",style=tk.ARC, width=20,tags="25")
C.create_arc(290,290,310,310,start=0,extent=359.9999, outline="red",style=tk.ARC, width=20,tags="D25")


C.pack(side="top", padx=50, pady=50)
move_items(C,10,10)

output_label = tk.Label(root, text="Hey")
output_label.pack()
C.bind("<Button-1>", check_click)

root.mainloop()