import tkinter as tk

finestraX = 1024
finestraY = 768

finestra = tk.Tk()
finestra.title("Aventura grafica RPG")
finestra.geometry(f"{finestraX}x{finestraY}")

canvasX = finestraX / 1.25
canvasY = finestraY / 1.25
print(canvasX)
print(canvasY)

LlistaMapa = [[1,2,3],[4,5,6],[7,8,9]]

posMapX = 1
posMapY = 1



canvas = tk.Canvas(finestra, width=canvasX, height=canvasY, bg="lightblue")

image1 = tk.PhotoImage(file="img/PobleInicial.png")
novaEscena = image1
img_escena_id = canvas.create_image(finestraX / 2, finestraY / 2, image = novaEscena)

x_center = (finestraX - canvasX) / 2
y_center = (finestraY - canvasY) / 2
canvas.place(x=x_center, y=y_center)


finestra.mainloop()