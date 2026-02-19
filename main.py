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
LlistaInventari = []
Missions = ["Ves al gremi"]
MissionsCompletades = []

posMapX = 1
posMapY = 1

canvas = tk.Canvas(finestra, width=canvasX, height=canvasY, bg="lightblue")

image1 = tk.PhotoImage(file="img/PobleInicial.png")
image2 = tk.PhotoImage(file="img/ZonaAventura001.png")
image3 = tk.PhotoImage(file="img/EntradaMazmorra02.png")
image4 = tk.PhotoImage(file="img/CasaMaga.png")
image5 = tk.PhotoImage(file="img/CampoEntrenamiento.png")
image6 = tk.PhotoImage(file="img/GremioAventureros.png")
image7 = tk.PhotoImage(file="img/ZonaMazmorra002.png")
image8 = tk.PhotoImage(file="img/ZonaAventura002.png")
novaEscena = image1

ZonaActualMazmorra = image3
portaMazmorraOberta = False

img_escena_id = canvas.create_image(finestraX // 4, finestraY // 4, image = novaEscena)

x_center = (finestraX - canvasX) // 2
y_center = (finestraY - canvasY) // 2
canvas.place(x=x_center, y=y_center)

#Enemics
enemic1_viu = True
enemic2_viu = True

def mostrarMissatge(text, duracio=5000, color = "red"):
    label_Missatge.config(text=text, fg=color)
    finestra.after(duracio, lambda:label_Missatge.config(text=""))

def investigarZona():
    global novaEscena, portaMazmorraOberta

    zona = LlistaMapa[posMapY][posMapX]

    match zona:

        case 2:
            if "Ves al pantà" in Missions:
                mostrarMissatge(text="Enemic trobat!!", color="red")
                Missions.pop()
                Missions.append("Elimina l'enemic")
                actualitzaHUD()
            elif "Ves al prado" in Missions:
                mostrarMissatge(text="Enemic trobat!!", color="red")
                Missions.pop()
                Missions.append("Elimina l'enemic")
                actualitzaHUD()
            else:
                mostrarMissatge(text="No pots fer res encara aquí", color="red")

        
        case 3:
                if "Claus de la Mazmorra" in LlistaInventari:
                    mostrarMissatge(text="Porta oberta!!", color="green")

                    novaEscena = image7
                    canvas.itemconfig(img_escena_id, image= novaEscena)
                    portaMazmorraOberta = True
                    LlistaInventari.remove("Claus de la Mazmorra")
                    actualitzaHUD()
                    
                else:
                    mostrarMissatge(text="Necessites les claus!", color="red")
        
        case 4:
            if "Ves a la zona d'entrenament" in Missions:
                mostrarMissatge(text="Atac especial fisic aprés!!", color="green")
                Missions.pop()
                Missions.append("Ves al prado")
                actualitzaHUD()
            else:
                mostrarMissatge(text="No pot aprendre res encara")

        
        case 5:
            mostrarMissatge(text="No s'ha trobat res")

        case 8:
            if "Ves al gremi" in Missions:
                mostrarMissatge(text="Has rebut una nova missió", color="green")
                Missions.pop()
                Missions.append("Ves al pantà")
                actualitzaHUD()
            elif "Torna al gremi" in Missions and "Elimina l'enemic 01" in MissionsCompletades:
                mostrarMissatge(text="Has rebut una nova missió", color="green")
                Missions.pop()
                Missions.append("Ves a la zona d'entrenament")
                actualitzaHUD()
            elif "Demana informació sobre les claus al gremi" in Missions and "Elimina l'enemic 02" in MissionsCompletades:
                mostrarMissatge(text="Has rebut una nova missió", color="green")
                Missions.pop()
                Missions.append("Ves a la mazmorra")
                actualitzaHUD()
            else:
                mostrarMissatge(text="No tens missions disponibles", color="red")


def actualitzaHUD():
    label_missions_text.config(text="\n".join(Missions))
    label_objectes.config(text="\n".join(LlistaInventari))

            
def sortirJoc():
    finestra.destroy()

#Botons
botonInvestigarZona = tk.Button(finestra, text="Investigar zona", command=investigarZona)
botonInvestigarZona.place(x=x_center*3.15, y=y_center*2.75)

botonInvestigarZona = tk.Button(finestra, text="Sortir del joc", command=sortirJoc)
botonInvestigarZona.place(x=x_center*3.15, y=y_center*3)

#Descripcions
descripcio2 = "Pantà"
descripcio3 = "Mazmorra"
descripcio4 = "Zona d'entrenament"
descripcio5 = "Poble inicial"
descripcio6 = "Casa de la maga"
descripcio7 = "Segona zona de Mazmorra"
descripcio8 = "Gremi d'aventurers"
descripcio9 = "Prado"

# Creació labels
label_coordenadores = tk.Label(finestra, text="Coordenades: ", font=("Arial", 16))
label_coordenadores.place(x=x_center * 0.1, y=y_center * 0.1)

label_coordenadores_actuales = tk.Label(finestra, text=LlistaMapa[posMapY][posMapX], font=("Arial", 16))
label_coordenadores_actuales.place(x=x_center * 0.65, y=y_center * 0.1)

label_titol_escena = tk.Label(finestra, text=descripcio5, font=("Arial", 16))
label_titol_escena.place(x=x_center * 1.75, y=y_center * 0.75)

label_accio = tk.Label(finestra, text="Acció: ", font=("Arial", 16))
label_accio.place(x=x_center * 1.15, y=y_center * 3.2)

label_inventari = tk.Label(finestra, text="Inventari: ", font=("Arial", 16))
label_inventari.place(x=x_center * 0.15, y=y_center * 1)

label_missions = tk.Label(finestra, text="Missions: ", font=("Arial", 16))
label_missions.place(x=x_center * 3.05, y=y_center * 1)

objecte_text = "\n".join(LlistaInventari)
label_objectes = tk.Label(finestra, text=objecte_text, font=("Arial", 16), justify="left")
label_objectes.place(x=x_center * 0.15, y=y_center * 1.15)

missions_text = "\n".join(Missions)
label_missions_text = tk.Label(finestra, text=missions_text, font=("Arial", 16), justify="right")
label_missions_text.place(x=x_center * 3.05, y=y_center * 1.15)

text = ""
label_Missatge = tk.Label(finestra, text=text, font=("Arial", 16), fg="red", wraplength= 400, justify="center")
label_Missatge.place(x=x_center*1.65, y=y_center*0.25)

entrada = tk.Entry(finestra,font=("Arial", 14))
entrada.place(x=x_center * 1.4, y=y_center * 3.2)
entrada.focus_set()


def actualitzaEscena(escena):
    global posMapX, posMapY, image1, image2, novaEscena, novaDescripcio, portaOberta

    match escena:

        case 1:
            print ("estas a l'escena 1")
        
        case 2:
            print ("estas a l'escena 2")
            if "Elimina l'enemic 01" in MissionsCompletades:
                novaEscena = image8
                novaDescripcio = descripcio9
            else:
                novaEscena = image2
                novaDescripcio = descripcio2
        
        case 3:
            print ("estas a l'escena 3")
            if portaMazmorraOberta == False:
                novaEscena = image3
                novaDescripcio = descripcio3
            elif portaMazmorraOberta == True:
                novaEscena = image7
                novaDescripcio = descripcio7

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
    global posMapY, posMapX, enemic1_viu, enemic2_viu
    
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
            if posMapX > 2 or LlistaMapa[posMapY][posMapX] == 9:
                print("No pots anar cap allá")
                posMapX -= 1

        case "oest":
            posMapX -= 1
            if posMapX < 0 or LlistaMapa[posMapY][posMapX] == 1 or LlistaMapa[posMapY][posMapX] == 7:
                print("No pots anar cap allá")
                posMapX += 1

        case "atacar":
            if LlistaMapa[posMapY][posMapX] == 2 and enemic1_viu == True and "Elimina l'enemic" in Missions:
                mostrarMissatge(text="Enemic del pantà derrotat!!", color="green")
                Missions.pop()
                Missions.append("Torna al gremi")
                MissionsCompletades.append("Elimina l'enemic 01")
                actualitzaHUD()
                enemic1_viu = False
                
            elif LlistaMapa[posMapY][posMapX] == 2 and enemic2_viu == True and "Elimina l'enemic" in Missions:
                mostrarMissatge(text="Enemic del prado derrotat!!", color="green")
                LlistaInventari.append("Claus de la Mazmorra")
                Missions.pop()
                Missions.append("Demana informació sobre les claus al gremi")
                MissionsCompletades.append("Elimina l'enemic 02")
                actualitzaHUD()
            else:
                mostrarMissatge(text="No pots atacar aquí", color="red")
    
        case _:
            print("Moviment no vàlid")
        
    actualitzaEscena(LlistaMapa[posMapY][posMapX])
    entrada.delete(0, tk.END)

    label_coordenadores_actuales.config(text=LlistaMapa[posMapY][posMapX])

def main():
    actualitzaEscena(LlistaMapa[posMapY][posMapX])
    entrada.bind("<Return>", moviment)

main()



finestra.mainloop()