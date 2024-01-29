import tkinter as tk

#Werte der Felder gegen den Uhrzeigersinn, startet bei 13 da dort der Startwinkel für die Arcerstellung = 0 ist
Board_Numbers = ["13","4","18","1","20","5","12","9","14","11","8","16","7","19","3","17","2","15","10","6"]

#Funktion um das gesamte Board zu verschieben
def move_items(canvas, dx, dy):
    items = canvas.find_all()
    for item in items:
        canvas.move(item, dx, dy)

#Buttonfunktion für die Felder
def check_click(event):
    output_label.config(text="You've hit a " + event.widget.gettags("current")[0])
    
#erstellt Tkinter Objekt
root = tk.Tk()
window_height = 800
window_width = 800
root.geometry(f'{window_height}x{window_width}')

#Hauptwert, soll Ausgangswert für Berechnung aller anderen Werte werden
dartboard_width = 600

#Canvasobjekt, in dem das Board gebaut wird
C = tk.Canvas(root,bg="white", height=dartboard_width+10, width=dartboard_width+10)

#Koordinaten für die jeweiligen Ringe: Doppel, Äußerer Single, Triple, Innerer Single
coord_double = 10, 10, 590, 590
coord_triple = 140, 140, 460, 460
coord_outer = 75, 75, 525, 525
coord_inner = 205, 205, 395, 395 

#erstellt die 20 Felder mit Doppeln und Trippeln, pro Iteration 2 Felder, startet bei der 13
for i in range(10):
    #erstellt die Doppelfelder
    C.create_arc(coord_double, start=36*i+9, extent=18, outline="red", style=tk.ARC, width=20, tags="D"+Board_Numbers[2*i])
    C.create_arc(coord_double, start=36*i+18+9, extent=18, outline="green", style=tk.ARC, width=20, tags="D"+Board_Numbers[2*i+1])

    #erstellt die äußeren Singlefelder
    C.create_arc(coord_outer, start=36*i+9, extent=18, outline="black", style=tk.ARC, width=110,tags=Board_Numbers[2*i])
    C.create_arc(coord_outer, start=36*i+18+9, extent=18, outline="white", style=tk.ARC, width=110, tags=Board_Numbers[2*i+1])

    #erstellt die Triplefelder
    C.create_arc(coord_triple, start=36*i+9, extent=18, outline="red", style=tk.ARC, width=20,tags="T"+Board_Numbers[2*i])
    C.create_arc(coord_triple, start=36*i+18+9, extent=18, outline="green", style=tk.ARC, width=20,tags="T"+Board_Numbers[2*i+1])

    #erstellt die inneren Singlefelder
    C.create_arc(coord_inner, start=36*i+9, extent=18, outline="black", style=tk.ARC, width=110,tags=Board_Numbers[2*i])
    C.create_arc(coord_inner, start=36*i+18+9, extent=18, outline="white", style=tk.ARC, width=110,tags=Board_Numbers[2*i+1])
    
#erstellt das single und full Bullseye, leider bei extent=360 kein Bogen mehr vorhanden, daher Näherung
C.create_arc(270,270,330,330,start=0,extent=359.9999, outline="green",style=tk.ARC, width=20,tags="25")
C.create_arc(290,290,310,310,start=0,extent=359.9999, outline="red",style=tk.ARC, width=20,tags="D25") #Zu groß, lieber 10px kleiner

C.pack(side="top", padx=50, pady=50)
#Da die Arcs über die Outline definiert werden, diese allerdings nicht zur Ausmaße des Objektes an sich zählt, gibt es einen leichten Überlapp mit dem Rand, der hiermit gefixt wird.
move_items(C,10,10)

#Definiert das Outputfeld
output_label = tk.Label(root, text="Hey")
output_label.pack()
C.bind("<Button-1>", check_click)

root.mainloop()