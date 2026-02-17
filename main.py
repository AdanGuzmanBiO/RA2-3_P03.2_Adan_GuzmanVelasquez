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
LlistaInventari = ["claus", "pá", "roba"]

posMapX = 1
posMapY = 1

canvas = tk.Canvas(finestra, width=canvasX, height=canvasY, bg="lightblue")

image1 = tk.PhotoImage(file="img/PobleInicial.png")
image2 = tk.PhotoImage(file="img/ZonaAventura001.png")
image3 = tk.PhotoImage(file="img/EntradaMazmorra02.png")
image4 = tk.PhotoImage(file="img/CasaMaga.png")
image5 = tk.PhotoImage(file="img/CampoEntrenamiento.png")
image6 = tk.PhotoImage(file="img/GremioAventureros.png")
novaEscena = image1
img_escena_id = canvas.create_image(finestraX // 4, finestraY // 4, image = novaEscena)

x_center = (finestraX - canvasX) // 2
y_center = (finestraY - canvasY) // 2
canvas.place(x=x_center, y=y_center)


def investigarZona():

    zona = LlistaMapa[posMapY][posMapX]

    match zona:

        case 2:
            print("Enemic trobat!!")
        
        case 3:
                if "ClausMazmorra" in LlistaInventari:
                    print ("Porta oberta!!")
                    
                else:
                    print("Necessites les claus!")
        
        case 5:
            print("No s'ha trobat res")
            
def sortirJoc():
    finestra.destroy()

#Botons
botonInvestigarZona = tk.Button(finestra, text="Investigar zona", command=investigarZona)
botonInvestigarZona.place(x=x_center*3.15, y=y_center*2.75)

botonInvestigarZona = tk.Button(finestra, text="Sortir del joc", command=sortirJoc)
botonInvestigarZona.place(x=x_center*3.15, y=y_center*3)

#Descripcions
descripcio2 = "Prado"
descripcio3 = "Mazmorra"
descripcio4 = "Zona d'entrenament"
descripcio5 = "Poble inicial"
descripcio6 = "Casa de la maga"
descripcio8 = "Gremi d'aventurers"

# Creació labels
label_coordenadores = tk.Label(finestra, text="Coordenades: ", font=("Arial", 16))
label_coordenadores.place(x=x_center * 0.1, y=y_center * 0.1)

label_coordenadores = tk.Label(finestra, text=LlistaMapa[posMapY][posMapX], font=("Arial", 16))
label_coordenadores.place(x=x_center * 0.65, y=y_center * 0.1)

label_titol_escena = tk.Label(finestra, text=descripcio5, font=("Arial", 16))
label_titol_escena.place(x=x_center * 1.75, y=y_center * 0.75)

label_accio = tk.Label(finestra, text="Acció: ", font=("Arial", 16))
label_accio.place(x=x_center * 1.15, y=y_center * 3.2)

label_inventari = tk.Label(finestra, text="Inventari: ", font=("Arial", 16))
label_inventari.place(x=x_center * 0.15, y=y_center * 1)


objecte_text = "\n".join(LlistaInventari)
label_objectes = tk.Label(finestra, text=objecte_text, font=("Arial", 16), justify="left")
label_objectes.place(x=x_center * 0.15, y=y_center * 1.15)

entrada = tk.Entry(finestra,font=("Arial", 14))
entrada.place(x=x_center * 1.4, y=y_center * 3.2)
entrada.focus_set()


def actualitzaEscena(escena):
    global posMapX, posMapY, image1, image2, novaEscena, novaDescripcio

    match escena:

        case 1:
            print ("estas a l'escena 1")
        
        case 2:
            print ("estas a l'escena 2")
            novaEscena = image2
            novaDescripcio = descripcio2
        
        case 3:
            print ("estas a l'escena 3")
            novaEscena = image3
            novaDescripcio = descripcio3

        case 4:
            print ("estas a l'escena 4")
            novaEscena = image5
            novaDescripcio = descripcio4
            
        
        case 5:
            print ("estas a l'escena 5")
            novaEscena = image1
            novaDescripcio = descripcio5
            
        
        case 6:
            print ("estas a l'escena 6")
            novaEscena = image4
            novaDescripcio = descripcio6
        
        case 7:
            print ("estas a l'escena 7")

        case 8:
            print ("estas a l'escena 8")
            novaEscena = image6
            novaDescripcio = descripcio8
        
        case 9:
            print ("estas a l'escena 9")
        
    canvas.itemconfig(img_escena_id, image= novaEscena)
    label_titol_escena.config(text=novaDescripcio)


def moviment(event=None):
    global posMapY, posMapX
    
    text = entrada.get()
    match text:
        case "nord":
            posMapY -= 1
            if posMapY < 0:
                print("No pots anar cap allá")
                posMapY += 1

        case "sud":
            posMapY += 1
            if posMapY > 2:
                print("No pots anar cap allá")
                posMapY -= 1

        case "est":
            posMapX += 1
            if posMapX > 2:
                print("No pots anar cap allá")
                posMapX -= 1

        case "oest":
            posMapX -= 1
            if posMapX < 0:
                print("No pots anar cap allá")
                posMapX += 1
    
        case _:
            print("Moviment no vàlid")
        
    actualitzaEscena(LlistaMapa[posMapY][posMapX])
    entrada.delete(0, tk.END)

    label_coordenadores.config(text=LlistaMapa[posMapY][posMapX])

def main():
    actualitzaEscena(LlistaMapa[posMapY][posMapX])
    entrada.bind("<Return>", moviment)

main()



finestra.mainloop()