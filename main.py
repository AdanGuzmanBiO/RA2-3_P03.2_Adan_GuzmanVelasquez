#Importacions
import tkinter as tk
import pygame
pygame.mixer.init()

# Creem la finestra del joc
finestraX = 1024
finestraY = 768
finestra = tk.Tk()
finestra.title("Aventura grafica RPG")
finestra.geometry(f"{finestraX}x{finestraY}")

#Audio
musica_fondo_activa = True
pygame.mixer.music.load("audio/Musica_Global_RPG.wav")
so_atac_fisic = pygame.mixer.Sound("audio/Atac_Fisic.wav")
so_atac_magic = pygame.mixer.Sound("audio/Atac_Magic.wav")
reproducir_musica = None

# Creem el canvas del joc
canvasX = finestraX // 2
canvasY = finestraY // 2
posMapX = 1
posMapY = 1
canvas = tk.Canvas(finestra, width=canvasX, height=canvasY, bg="lightblue")
canvas_enemic = tk.Canvas(finestra, width=canvasX//2, height=canvasY//2, bg="lightblue")

# Creem les llistes per al mapa, inventari, habilitats i missions
LlistaMapa = [[1,2,3],[4,5,6],[7,8,9]]
LlistaInventari = []
Habilitats = []
Missions = ["Ves al gremi"]
MissionsCompletades = []

# Imatges escenes
image1 = tk.PhotoImage(file="img/PobleInicial.png")
image2 = tk.PhotoImage(file="img/ZonaAventura001.png")
image3 = tk.PhotoImage(file="img/EntradaMazmorra02.png")
image4 = tk.PhotoImage(file="img/CasaMaga.png")
image5 = tk.PhotoImage(file="img/CampoEntrenamiento.png")
image6 = tk.PhotoImage(file="img/GremioAventureros.png")
image7 = tk.PhotoImage(file="img/ZonaMazmorra002.png")
image8 = tk.PhotoImage(file="img/ZonaAventura002.png")
image9 = tk.PhotoImage(file="img/BossFinal.png")
novaEscena = image1

# Imatges Enemics
enemic1_Mazmorra_img = tk.PhotoImage(file="img/Enemic_Mazmorra.png")
enemic_Panta_img = tk.PhotoImage(file="img/Enemic_Panta.png")
enemic_Prado_img = tk.PhotoImage(file="img/Enemic_Prado.png")
enemic_actual = None

# Imatges Zona mazmorra
ZonaActualMazmorra = image3
portaMazmorraOberta = False

# Posicionem les imatges i els canvas
img_escena_id = canvas.create_image(finestraX // 4, finestraY // 4, image = novaEscena)
img_enemic_id = canvas_enemic.create_image(finestraX // 8, finestraY // 8, image = enemic_actual)

x_center = (finestraX - canvasX) // 2
y_center = (finestraY - canvasY) // 2
canvas.place(x=x_center, y=y_center)

# Enemics
enemic1_viu = True
enemic2_viu = True
enemic1_mazmorra_viu = True
BossInvocat = False

# Funció que mostra missatges al jugador
def mostrarMissatge(text, duracio=5000, color = "red"):
    label_Missatge.config(text=text, fg=color)
    finestra.after(duracio, lambda:label_Missatge.config(text=""))

# Funció que mostra dialegs al jugador
def mostrarDialeg(text, duracio=5000, color = "green"):
    canvas.itemconfig(dialeg_canvas,text=text, fill=color)
    finestra.after(duracio, lambda:canvas.itemconfig(dialeg_canvas,text=""))

# Funció que actualitza les missions del jugador
def ActualitzarMissio(Missio_Nova, Missio_Completada):
    Missions.pop()
    Missions.append(Missio_Nova)
    MissionsCompletades.append(Missio_Completada)
    actualitzaHUD()

# Funció que mostra l'enemic a la pantalla
def MostrarEnemic(enemic):
    global enemic_actual
    enemic_actual = enemic
    canvas_enemic.itemconfig(img_enemic_id, image= enemic_actual)
    canvas_enemic.place(x=x_center*1.75, y=y_center*1.95)

# Funció que oculta l'enemic de la pantalla
def OcultarEnemic():
    global enemic_actual
    enemic_actual = None
    canvas_enemic.itemconfig(img_enemic_id, image= enemic_actual)
    canvas_enemic.place_forget()

# Funció que investiga la zona on es troba el jugador i mostra els enemics, missatges i missions corresponents
def investigarZona():
    global novaEscena, portaMazmorraOberta, BossInvocat

    zona = LlistaMapa[posMapY][posMapX]

    match zona:
        case 2:
            if "Ves al pantà" in Missions:
                MostrarEnemic(enemic_Panta_img)
                mostrarMissatge(text="Enemic trobat!!", color="red")
                ActualitzarMissio(Missio_Nova="Elimina l'enemic del Pantà", Missio_Completada=None)
            elif "Ves al Prado" in Missions:
                MostrarEnemic(enemic_Prado_img)
                mostrarMissatge(text="Enemic trobat!!", color="red")
                ActualitzarMissio(Missio_Nova="Elimina l'enemic del Prado", Missio_Completada=None)
            else:
                mostrarMissatge(text="No pots fer res encara aquí", color="red")
        
        case 3:
                if "Claus de la Mazmorra" in LlistaInventari:
                    mostrarMissatge(text="Porta oberta!!", color="green")
                    novaEscena = image7
                    canvas.itemconfig(img_escena_id, image= novaEscena)
                    portaMazmorraOberta = True
                    LlistaInventari.remove("Claus de la Mazmorra")
                    ActualitzarMissio(Missio_Nova="Informar al gremi sobre la mazmorra", Missio_Completada="Obre la porta de la mazmorra")

                elif novaEscena == image7 and "atac magic" in Habilitats and enemic1_mazmorra_viu == True:
                    MostrarEnemic(enemic1_Mazmorra_img)
                    mostrarMissatge(text="Enemic trobat!!", color="red")
                    ActualitzarMissio(Missio_Nova="Elimina l'enemic mazmorra 01", Missio_Completada=None)

                elif novaEscena == image7 and "atac magic" in Habilitats and "Invoca el boss final a la mazmorra" in Missions:
                    novaEscena = image9
                    canvas.itemconfig(img_escena_id, image= novaEscena)
                    novaDescripcio = descripcio1
                    label_titol_escena.config(text=novaDescripcio)
                    BossInvocat = True
                    mostrarMissatge(text="Boss final invocat!!", color="red")
                    ActualitzarMissio(Missio_Nova="Elimina el boss final", Missio_Completada=None)

                else:
                    if "Claus de la Mazmorra" not in LlistaInventari and "Obre la porta de la mazmorra" not in MissionsCompletades:
                        mostrarMissatge(text="Necessites les claus!", color="red")
                    elif novaEscena == image7 and "atac magic" not in Habilitats:
                        mostrarMissatge(text="No pots investigar aqui, els enemic son massa forts!", color="red")
                    
        case 4:
            if "atac fisic" in Habilitats:
                mostrarDialeg(text="Guerrer: Ja no et puc ensenyar res més, segueix fent les missions!", color="yellow")
            else:
                if "Ves a la zona d'entrenament" in Missions:
                    Habilitats.append("atac fisic")
                    ActualitzarMissio(Missio_Nova="Ves al pantà", Missio_Completada=None)
                    mostrarMissatge(text="Atac fisic aprés!!", color="green")
                    mostrarDialeg(text="Guerrer: Tens talent per l'esgrima, segueix entrenant novat!", color="yellow")

                else:
                    mostrarMissatge(text="No pot aprendre res encara")
                    mostrarDialeg(text="Guerrer: Encara no pots entrenar aquí, fora!", color="yellow")

        case 5:
            
            if "Demana informació sobre el grimori en el poble" in Missions and "Elimina l'enemic 02" in MissionsCompletades:
                mostrarMissatge(text="Localització de la maga aconseguida!", color="green")
                mostrarDialeg(text="Aldeana: La casa de la maga está cap a l'est desde aquest Poble, però es perillosa!", color="black")
                ActualitzarMissio(Missio_Nova="Ves a la casa de la maga", Missio_Completada=None)
            else:
                mostrarMissatge(text="No pots fer res aquí encara")

        case 6:
            if "atac magic" in Habilitats:
                mostrarDialeg(text="Maga: No puc ensenyar-te res mes. Ja tens els elements necessaris per continuar la teva aventura", color="green")
            else:
                if "Ves a la casa de la maga" in Missions and "Grimori" in LlistaInventari:
                    mostrarMissatge(text="Atac magic aprés!!", color="green")
                    mostrarDialeg(text="Maga: Amb aquest atac magic et pots obrir camí per noves zones perilloses.")
                    ActualitzarMissio(Missio_Nova="Ves a la mazmorra", Missio_Completada=None)
                    Habilitats.append("atac magic")
                    
                else:
                    mostrarMissatge(text="No pots aprendre res encara")
                    mostrarDialeg(text="Maga: No estás en condicions encara per aprendre magia")

        case 8:
            if "Ves al gremi" in Missions:
                mostrarMissatge(text="Has rebut una nova missió", color="green")
                mostrarDialeg(text="Lider del gremi: Amb el tue nivell no pots fer missions! Parla amb el guerrer i després ves al pantà", color="yellow")
                ActualitzarMissio(Missio_Nova="Ves a la zona d'entrenament", Missio_Completada=None)

            elif "Torna al gremi" in Missions and "Elimina l'enemic 01" in MissionsCompletades:
                mostrarMissatge(text="Has rebut una nova missió", color="green")
                mostrarDialeg(text="Lidel del gremi: Bona feina! Amb aquestes claus pots obrir la porta de la mazmorra.", color="yellow")
                ActualitzarMissio(Missio_Nova="Obre la porta de la mazmorra", Missio_Completada=None)

            elif "Informar al gremi sobre la mazmorra" in Missions:
                mostrarMissatge(text="Has rebut una nova missió", color="green")
                mostrarDialeg(text="Lidel del gremi: Encara no tens el nivell suficient per investigar aquesta mazmorra, aconsegueis nivell al Prado!", color="yellow")
                ActualitzarMissio(Missio_Nova="Ves al Prado", Missio_Completada=None)
            
            elif "Demana informació sobre la runa al gremi" in Missions:
                mostrarMissatge(text="Has rebut una nova missió", color="green")
                mostrarDialeg(text="Lidel del gremi: T'has convertir en un dels millors aventurers, aquesta runa serveix per invocar al Boss en la mazmorra, ja tens el nivell suficient per fer-ho.", color="yellow")
                ActualitzarMissio(Missio_Nova="Invoca el boss final a la mazmorra", Missio_Completada=None)

            else:
                mostrarMissatge(text="No tens missions disponibles", color="red")

# Funció que actualitza el HUD del jugador amb les missions i l'inventari actuals
def actualitzaHUD():
    label_missions_text.config(text="\n".join(Missions))
    label_objectes.config(text="\n".join(LlistaInventari))

# Funció que permet al jugador sortir del joc i aturar la música de fons
def sortirJoc():
    global musica_fondo_activa, reproducir_musica
    musica_fondo_activa = False
    if reproducir_musica is not None:
        reproducir_musica.stop()
    finestra.destroy()

# Botons
botonInvestigarZona = tk.Button(finestra, text="Investigar zona", command=investigarZona)
botonInvestigarZona.place(x=x_center*3.15, y=y_center*2.75)

botonSortirJoc = tk.Button(finestra, text="Sortir del joc", command=sortirJoc)
botonSortirJoc.place(x=x_center*3.15, y=y_center*3)

# Descripcions
descripcio1 = "Boss Final!!"
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
label_titol_escena.place(x=x_center * 1.65, y=y_center * 0.75)

label_accio_moviment = tk.Label(finestra, text="Moviment: ", font=("Arial", 16))
label_accio_moviment.place(x=x_center * 1.15, y=y_center * 3.2)

label_accio_moviment_possible = tk.Label(finestra, text="Nord, Sud, Est i Oest", font=("Arial", 16))
label_accio_moviment_possible.place(x=x_center * 1.55, y=y_center * 3.2)

label_accio_combat = tk.Label(finestra, text="Combat: ", font=("Arial", 16))
label_accio_combat.place(x=x_center * 1.15, y=y_center * 3.4)

label_accio_combat_02 = tk.Label(finestra, text="Atac fisic i Atac magic", font=("Arial", 16))
label_accio_combat_02.place(x=x_center * 1.50, y=y_center * 3.4)

label_accio = tk.Label(finestra, text="Acció: ", font=("Arial", 16))
label_accio.place(x=x_center * 1.15, y=y_center * 3.6)

label_inventari = tk.Label(finestra, text="Inventari: ", font=("Arial", 16))
label_inventari.place(x=x_center * 0.15, y=y_center * 1)

label_missions = tk.Label(finestra, text="Missions: ", font=("Arial", 16))
label_missions.place(x=x_center * 3.05, y=y_center * 1)

objecte_text = "\n".join(LlistaInventari)
label_objectes = tk.Label(finestra, text=objecte_text, font=("Arial", 16), justify="left", wraplength=200)
label_objectes.place(x=x_center * 0.15, y=y_center * 1.15)

missions_text = "\n".join(Missions)
label_missions_text = tk.Label(finestra, text=missions_text, font=("Arial", 16), justify="left", wraplength=200)
label_missions_text.place(x=x_center * 3.05, y=y_center * 1.15)

text = ""
label_Missatge = tk.Label(finestra, text=text, font=("Arial", 16), fg="red", wraplength= 400, justify="center")
label_Missatge.place(x=x_center*1.5, y=y_center*0.25)

dialeg_canvas = canvas.create_text(canvasX//2, canvasY - 40, text=text,fill="white", font=("Arial", 12), width=380, justify="center")

entrada = tk.Entry(finestra,font=("Arial", 14))
entrada.place(x=x_center * 1.4, y=y_center * 3.6)
entrada.focus_set()

# Funció que actualitza l'escena del joc segons la posició del jugador al mapa, les missions completades
# o els items que té a l'inventari
def actualitzaEscena(escena):
    global posMapX, posMapY, image1, image2, novaEscena, novaDescripcio

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
            elif portaMazmorraOberta == True and BossInvocat == False:
                novaEscena = image7
                novaDescripcio = descripcio7
            elif portaMazmorraOberta == True and BossInvocat == True:
                novaEscena = image9
                novaDescripcio = descripcio1

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

# Funció que permet al jugador moure's per les diferents escenes del joc, atacar als enemics i completar les missions
# Solament es pot atacar als enemics si es cumpleixen les condicions de les missions i si el jugador té les habilitats necessàries per fer-ho
def moviment(event=None):
    global posMapY, posMapX, enemic1_viu, enemic2_viu, enemic1_mazmorra_viu, BossInvocat
    
    text = entrada.get().strip().lower()
    match text:
        case "nord":
            posMapY -= 1
            if posMapY < 0 or LlistaMapa[posMapY][posMapX] == 1:
                mostrarMissatge(text= "No pots anar cap allá")
                posMapY += 1

        case "sud":
            posMapY += 1
            if posMapY > 2 or LlistaMapa[posMapY][posMapX] == 7 or LlistaMapa[posMapY][posMapX] == 9:
                mostrarMissatge(text= "No pots anar cap allá")
                posMapY -= 1

        case "est":
            posMapX += 1
            if posMapX > 2 or LlistaMapa[posMapY][posMapX] == 9:
                mostrarMissatge(text= "No pots anar cap allá")
                posMapX -= 1

        case "oest":
            posMapX -= 1
            if posMapX < 0 or LlistaMapa[posMapY][posMapX] == 1 or LlistaMapa[posMapY][posMapX] == 7:
                mostrarMissatge(text= "No pots anar cap allá")
                posMapX += 1

        case "atac fisic":
            if "atac fisic" in Habilitats:
                if LlistaMapa[posMapY][posMapX] == 2 and enemic1_viu == True and "Elimina l'enemic del Pantà" in Missions:
                    so_atac_fisic.play()
                    OcultarEnemic()
                    mostrarMissatge(text="Enemic del Pantà derrotat!!", color="green")
                    LlistaInventari.append("Claus de la Mazmorra")
                    ActualitzarMissio(Missio_Nova="Torna al gremi", Missio_Completada="Elimina l'enemic 01")
                    enemic1_viu = False

                elif LlistaMapa[posMapY][posMapX] == 2 and enemic2_viu == True and "Elimina l'enemic del Prado" in Missions:
                    so_atac_fisic.play()
                    OcultarEnemic()
                    mostrarMissatge(text="Enemic del Prado derrotat!!", color="green")
                    LlistaInventari.append("Grimori")
                    ActualitzarMissio(Missio_Nova="Demana informació sobre el grimori en el poble", Missio_Completada="Elimina l'enemic 02")
                    enemic2_viu = False
                
                elif LlistaMapa[posMapY][posMapX] == 3 and enemic1_mazmorra_viu == True and "Elimina l'enemic mazmorra 01" in Missions:
                    so_atac_fisic.play()
                    OcultarEnemic()
                    mostrarMissatge(text="Enemic de la mazmorra derrotat!!", color="green")
                    LlistaInventari.append("Runa d'invocació del boss")
                    ActualitzarMissio(Missio_Nova="Demana informació sobre la runa al gremi", Missio_Completada="Elimina l'enemic mazmorra 01")
                    enemic1_mazmorra_viu = False
                
                elif LlistaMapa[posMapY][posMapX] == 3 and BossInvocat == True and "Elimina el boss final" in Missions:
                    so_atac_fisic.play()
                    mostrarMissatge(text="Boss final derrotat!!", color="green")
                    ActualitzarMissio(Missio_Nova="Sense missions, joc completat!", Missio_Completada="Elimina el boss final")
                    BossInvocat = False
                else:
                    mostrarMissatge(text="No pots atacar aquí", color="red")
            else:
                mostrarMissatge(text="No has aprés aquesta habilitat encara")

        case "atac magic":
            if "atac magic" in Habilitats:
                if LlistaMapa[posMapY][posMapX] == 2:
                    mostrarMissatge(text="No pots utilitzar aquesta habilitat aquí.")

                elif LlistaMapa[posMapY][posMapX] == 3 and enemic1_mazmorra_viu == True and "Elimina l'enemic mazmorra 01" in Missions:
                    so_atac_magic.play()
                    OcultarEnemic()
                    mostrarMissatge(text="Enemic de la mazmorra derrotat!!", color="green")
                    LlistaInventari.append("Runa d'invocació del boss")
                    ActualitzarMissio(Missio_Nova="Demana informació sobre la runa al gremi", Missio_Completada="Elimina l'enemic mazmorra 01")
                    enemic1_mazmorra_viu = False

                elif LlistaMapa[posMapY][posMapX] == 3 and BossInvocat == True and "Elimina el boss final" in Missions:
                    so_atac_magic.play()
                    OcultarEnemic()
                    mostrarMissatge(text="Boss final derrotat!!", color="green")
                    ActualitzarMissio(Missio_Nova="Sense missions, joc completat!", Missio_Completada="Elimina el boss final")
                    BossInvocat = False

            else:
                mostrarMissatge(text="No has aprés aquesta habilitat encara")
    
        case _:
            print("Moviment no vàlid")
        
    actualitzaEscena(LlistaMapa[posMapY][posMapX])
    entrada.delete(0, tk.END)

    label_coordenadores_actuales.config(text=LlistaMapa[posMapY][posMapX])

# Funció principal que inicia el joc, actualitza l'escena inicial i comença la música de fons
def main():
    actualitzaEscena(LlistaMapa[posMapY][posMapX])
    entrada.bind("<Return>", moviment)
    pygame.mixer.music.play(-1)

# Iniciem el joc
main()

# Mantenim la finestra oberta
finestra.mainloop() 