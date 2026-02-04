import tkinter as tk

finestraX = 1024
finestraY = 768

finestra = tk.Tk()
finestra.title("Aventura grafica RPG")
finestra.geometry(f"{finestraX}x{finestraY}")

canvasX = finestraX // 2
canvasY = finestraY // 2
print(canvasX)
print(canvasY)

LlistaMapa = [[1,2,3],[4,5,6],[7,8,9]]

posMapX = 1
posMapY = 1

canvas = tk.Canvas(finestra, width=canvasX, height=canvasY, bg="lightblue")

image1 = tk.PhotoImage(file="img/PobleInicial.png")
image2 = tk.PhotoImage(file="img/Prado.png")

novaEscena = image1
img_escena_id = canvas.create_image(finestraX // 4, finestraY // 4, image = novaEscena)

x_center = (finestraX - canvasX) // 2
y_center = (finestraY - canvasY) // 2
canvas.place(x=x_center, y=y_center)

posicionMapa = LlistaMapa[posMapY][posMapX]
def actualitzaEscena(escena):
    global posMapX, posMapY, image1, image2, novaEscena

    match posicionMapa:

        case 1:
            print ("estas a l'escena 1")
        
        case 2:
            print ("estas a l'escena 2")
        
        case 3:
            print ("estas a l'escena 3")

        case 4:
            print ("estas a l'escena 4")
            novaEscena = image2
            actualitzaEscena(LlistaMapa[posMapY][posMapX])
        
        case 5:
            print ("estas a l'escena 5")
        
        case 6:
            print ("estas a l'escena 6")
        
        case 7:
            print ("estas a l'escena 7")

        case 8:
            print ("estas a l'escena 8")
        
        case 9:
            print ("estas a l'escena 9")
        
    canvas.itemconfig(img_escena_id, image= novaEscena)


entrada = tk.Entry(finestra,font=("Arial", 14))
entrada.place(x=x_center * 1.4, y=y_center * 3.2)

def moviment(event=None):
    global posMapY, posMapX, posicionMapa
    
    text = entrada.get()
    match text:
        case "nord":
            posMapY -= 1
            actualitzaEscena(LlistaMapa[posMapY][posMapX])
    
        case "sud":
            posMapY += 1
        
        case "est":
            posMapX += 1

        case "oest":
            posMapX -= 1

    posicionMapa = LlistaMapa[posMapY][posMapX]
    entrada.delete(0, tk.END)

    print (posicionMapa)

def main():
    actualitzaEscena(LlistaMapa[posMapY][posMapX])
    entrada.bind("<Return>", moviment)

print (posicionMapa)




finestra.mainloop()