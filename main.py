import random
from tkinter import *
from tkinter import messagebox
from functools import partial
import matriz_forma1 as mf1
import nodo_doble as nd
import tripleta as tr
import sys
from PIL import Image, ImageTk

# Se aumenta el límite de profundida de recursión
sys.setrecursionlimit(1000000000)

# Declaración características de la ventana
window = Tk()
window.title("Menú Principal - Buscaminas")
window.geometry('500x300')
window.resizable(0, 0)

# Declaración de listas globables de interés
buttons = []
visited = []
marked = []
bombs = []

# Métodos del GUI


def abrir_config():  # Método asociado al botón J U G A R
    # Declaración características de la ventana
    window.geometry('250x250')
    center(window)
    mi_label1.place_forget()
    mi_label2.place_forget()
    boton_exit.place_forget()
    boton_ins.place_forget()
    boton_inicio.place_forget()
    # Botones del Menu de Configuración
    # Botón P R I N C I P I A N T E
    boton_pri.pack()
    boton_pri.place(relx=0.5, rely=0.2, anchor=CENTER)
    # Botón I N T E R M E D I O
    boton_int.pack()
    boton_int.place(relx=0.5, rely=0.4, anchor=CENTER)
    # Botón E X P E R T O
    boton_exp.pack()
    boton_exp.place(relx=0.5, rely=0.6, anchor=CENTER)
    # Botón P E R S O N A L I Z A D O
    boton_per.pack()
    boton_per.place(relx=0.5, rely=0.8, anchor=CENTER)


def abrir_rules():  # Método asociado al botón R E G L A S
    # Declaración características de la ventana
    window.title("Buscaminas: Reglas")
    window.geometry('530x300')
    center(window)
    mi_label1.place_forget()
    mi_label2.place_forget()
    boton_exit.place_forget()
    boton_ins.place_forget()
    boton_inicio.place_forget()
    text_rul.pack()
    insert_volver(0.1, 0.8)


def center(win):  # Método para centrar las ventanas
    win.update_idletasks()
    width = win.winfo_width()
    height = win.winfo_height()
    x = (win.winfo_screenwidth() // 2) - (width // 2)
    y = (win.winfo_screenheight() // 2) - (height // 2)
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))


def exit_game():  # Método asociado al botón S A L I R
    window.destroy()


def clear_window(a, b, c, d):  # Método para limpiar la ventana
    a.place_forget()
    b.place_forget()
    c.place_forget()
    d.place_forget()


def clear_grid():  # Método que remueve las casillas del tablero
    for i in range(0, len(buttons)):
        buttons[i].place_forget()


def insert_volver(a, b):  # Método que inserta el botón V O L V E R
    boton_volver.pack()
    boton_volver.place(relx=a, rely=b)


def insert_con(a, b):  # Método que inserta el botón C O N T I N U A R
    boton_con.pack()
    boton_con.place(relx=a, rely=b)


def insert_label():  # Método que inserta los labeles en la ventana
    label_row.pack()
    label_col.pack()
    label_bomb.pack()
    label_row.place(x=10, y=10)
    label_col.place(x=10, y=40)
    label_bomb.place(x=10, y=70)


def insert_text():   # Método que inserta los campos de texto - Juego Personalizado
    text_row.pack()
    text_col.pack()
    text_bomb.pack()
    text_row.place(x=120, y=10)
    text_col.place(x=120, y=40)
    text_bomb.place(x=120, y=70)


def read_per():  # Método que lee las entradas de texto
    a = int(row.get())
    b = int(col.get())
    c = int(bomb.get())
    text_row.delete(0, END)
    text_col.delete(0, END)
    text_bomb.delete(0, END)
    forget_per()
    init_per(a, b, c)


def forget_per():  # Método que reestablece las cajas de texto
    boton_con.place_forget()
    label_row.place_forget()
    label_col.place_forget()
    label_bomb.place_forget()
    text_row.place_forget()
    text_col.place_forget()
    text_bomb.place_forget()


def init_menu():  # Método que inicializa el menú principal

    # Declaración de características de la ventana
    bombs.clear()
    visited.clear()
    marked.clear()
    window.title("Menú Principal - Buscaminas")
    window.geometry('500x300')
    center(window)
    clear_grid()
    boton_volver.place_forget()
    text_rul.forget()

    # Posicionamiento de Imagenes
    mi_label1.place(x=10, y=26)
    mi_label2.place(x=90, y=40)

    # Botón J U G A R
    boton_inicio.pack()
    boton_inicio.place(relx=0.5, rely=0.6, anchor=CENTER)

    # Botón R E G L A S
    boton_ins.pack()
    boton_ins.place(relx=0.5, rely=0.7, anchor=CENTER)

    # Botón S A L I R
    boton_exit.pack()
    boton_exit.place(relx=0.5, rely=0.8, anchor=CENTER)


def init_pri():  # Método Juego P R I N C I P I A N T E

    # Declaración de características de la ventana
    clear_window(boton_pri, boton_int, boton_exp, boton_per)
    a = genera_matriz(8, 8, 10)
    window.geometry('160x220')
    window.title('Buscaminas: Principiante')
    center(window)
    insert_volver(0.1, 0.8)
    genera_botones(8, 8, a)


def init_int():  # Método Juego I N T E R M E D I O

    # Declaración de características de la ventana
    clear_window(boton_pri, boton_int, boton_exp, boton_per)
    a = genera_matriz(16, 16, 40)
    window.geometry('320x380')
    window.title('Buscaminas: Intermedio')
    center(window)
    insert_volver(0.05, 0.875)
    genera_botones(16, 16, a)


def init_exp():  # Método Juego E X P E R T O

    # Declaración de características de la ventana
    clear_window(boton_pri, boton_int, boton_exp, boton_per)
    a = genera_matriz(16, 30, 99)
    window.geometry('600x380')
    window.title('Buscaminas: Experto')
    center(window)
    insert_volver(0.025, 0.875)
    genera_botones(16, 30, a)


def init_per(r, c, b):  # Método Juego P E R S O N A L I Z A D O

    # Declaración de características de la ventana
    clear_window(boton_pri, boton_int, boton_exp, boton_per)
    a = genera_matriz(r, c, b)
    rows = str((r*20)+60)
    cols = str((c*20))
    window.geometry(str(cols)+'x'+str(rows))
    window.title('Buscaminas: Personalizado')
    center(window)
    insert_volver(0.025, 0.875)
    genera_botones(r, c, a)


def init_per_menu():  # Método para personalizar el juego

    # Declaración de características de la ventana
    clear_window(boton_pri, boton_int, boton_exp, boton_per)
    window.geometry('230x150')
    window.title('Personalización')
    center(window)
    insert_con(0.25, 0.75)
    insert_label()
    insert_text()


def genera_botones(m, n, a):  # Método que genera las botones del tablero
    block = []
    for i in range(n):
        block.append([])
        for j in range(m):
            temp_command = partial(check, j, i, a, block)
            right_click_event = partial(mark_bomb, block, i, j)
            block[i].append(Button(window, command=temp_command, font='Consolas 14 bold'))
            block[i][j].place(x=i * 20, y=j * 20, width=20, height=20)
            block[i][j].bind('<Button-3>', right_click_event)
            buttons.append(block[i][j])
    return block


def mark_bomb(block, i, j, e): # Método que marca una casilla
    ganada(block)
    if block[i][j]['state'] != DISABLED and block[i][j]['text'] != 'O':
        marked.append([i, j])
        block[i][j].config(text='O', image=flag_img)
    else:
        marked.remove([i, j])
        block[i][j].config(text='', image='')
    ganada(block)


def bomb_count(vecinos, a):  # Método que cuenta las bombas en los alrededores de una casilla
    bombs_n = 0
    for k in range(0, len(vecinos)):
        for t in range(0, len(vecinos[0])):
            if t == 0:
                x1 = vecinos[k][t]
            elif t == 1:
                y1 = vecinos[k][t]
        if a.busca_coord(x1, y1):
            bombs_n = bombs_n + 1
    return bombs_n


def perdida(a, block):  # Método que avisa si se detona las minas
    messagebox.showerror('Fin del Juego', '¡Detonaste las minas!')
    for j in range(len(block)):
        for i in range(len(block[0])):
            block[j][i].config(state=DISABLED)
            if a.busca_coord(i, j):
                block[j][i].config(text='•', state=DISABLED, bg='red', fg='white', image='')
    bombs.clear()
    marked.clear()
    visited.clear()


def ganada(block):  # Método que avisa si se marcaron todas las minas correctamente
    if sorted(marked) == sorted(bombs):
        messagebox.showinfo('Fin del Juego', '¡Felicidades, has ganado!')
        for j in range(len(block)):
            for i in range(len(block[0])):
                block[j][i].config(state=DISABLED)
        bombs.clear()
        marked.clear()
        visited.clear()


def check(i, j, a, block):  # Método que chequea si la casilla presionada tiene una mina
    if a.busca_coord(i, j):
        perdida(a, block)
    else:
        vecinos = check_vecinos(i, j, block)
        clear_not_minas(block, i, j, vecinos, a)
        ganada(block)


def clear_not_minas(block, i, j, vecinos, a):  # Método que descubre las casillas sin minas
    if bomb_count(vecinos, a) == 0 and [i, j] not in visited:
        block[j][i].config(state=DISABLED, relief=FLAT, image='')
        for vecino in vecinos:
            x1 = vecino[0]
            y1 = vecino[1]
            vecinos_this = check_vecinos(x1, y1, block)
            clear_not_minas(block, x1, y1, vecinos_this, a)
            visited.append([i, j])
    else:
        if bomb_count(vecinos, a) == 0:
            block[j][i].config(state=DISABLED, text='', image='')
        else:
            block[j][i].config(state=DISABLED, text=bomb_count(vecinos, a), image='')


def check_vecinos(i, j, block):  # Método que recolecta los vecinos de una casilla en una lista
    vecinos = []
    for k in range(0, 8):
        if k == 0:
            x = i - 1
            y = j - 1
            if 0 <= y < len(block) and 0 <= x < len(block[0]):
                vecinos.append([x, y])
        elif k == 1:
            x = i - 1
            y = j
            if 0 <= y < len(block) and 0 <= x < len(block[0]):
                vecinos.append([x, y])
        elif k == 2:
            x = i - 1
            y = j + 1
            if 0 <= y < len(block) and 0 <= x < len(block[0]):
                vecinos.append([x, y])
        elif k == 3:
            x = i
            y = j + 1
            if 0 <= y < len(block) and 0 <= x < len(block[0]):
                vecinos.append([x, y])
        elif k == 4:
            x = i + 1
            y = j + 1
            if 0 <= y < len(block) and 0 <= x < len(block[0]):
                vecinos.append([x, y])
        elif k == 5:
            x = i + 1
            y = j
            if 0 <= y < len(block) and 0 <= x < len(block[0]):
                vecinos.append([x, y])
        elif k == 6:
            x = i + 1
            y = j - 1
            if 0 <= y < len(block) and 0 <= x < len(block[0]):
                vecinos.append([x, y])
        elif k == 7:
            x = i
            y = j - 1
            if 0 <= y < len(block) and 0 <= x < len(block[0]):
                vecinos.append([x, y])
    return vecinos


def genera_matriz(m, n, minas):  # Método que genera una matriz con minas en posiciones aleatorias
    v = 0
    u = 0
    a = mf1.MatrizForma1(m, n)
    a.construye_nodos_cabeza()
    x = random.randint(0, m)
    lx = [x]
    for i in range(0, minas):
        x = random.randint(1, m * n)
        while lx.count(x) > 0:
            x = random.randint(1, m * n)
        lx.append(x)
    lx = sorted(lx)
    for j in range(0, m):
        for k in range(0, n):
            if (lx[u]) == v and (u < minas):
                bombs.append([k, j])
                t = tr.Tripleta(j, k, 1)
                c = nd.NodoDoble(t)
                a.conecta_filas(c)
                a.conecta_columnas(c)
                u = u + 1
            v = v + 1
    return a


# Creación de Imagen Bandera
flag = Image.open('flag.png')
flag = flag.resize((15, 15), Image.ANTIALIAS)
flag_img = ImageTk.PhotoImage(flag)

# Creación de Imagen 1 del Menu
image1 = Image.open('LogoBuscaminas.png')
image1 = image1.resize((130, 130), Image.ANTIALIAS)
mi_img1 = ImageTk.PhotoImage(image1)
mi_label1 = Label(image=mi_img1)
mi_label1.pack()
mi_label1.place(x=10, y=26)

# Creación de Imagen 2 del Menu
image2 = Image.open('titulo_juego.png')
image2 = image2.resize((400, 70), Image.ANTIALIAS)
mi_img2 = ImageTk.PhotoImage(image2)
mi_label2 = Label(image=mi_img2)
mi_label2.pack()
mi_label2.place(x=90, y=40)

# Creación de R E G L A S

rul = "Algunas casillas tienen un número, el cual indica la cantidad de minas que hay en las casillas alrededor de " \
      "esta. Así, si una casilla tiene el número 1, significa que de las ocho casillas que hay alrededor exceptuando " \
      "los bordes o las esquinas hay 1 con minas y 6 sin minas. Si se descubre una casilla sin número indica que " \
      "ninguna de las casillas vecinas tiene mina y éstas se descubren automáticamente. \n\n > Click Izquierdo: " \
      "descubrir una casilla \n > Click Derecho: marcar una casilla\n\n Si se descubre una mina se pierde la " \
      "partida.\n Si se marcan todas las minas se gana la partida. "
text_rul = Text(window)
text_rul.insert(0.0, rul)
text_rul.config(width=50, height=8, font=("Tahoma", 14), padx=15, pady=15, selectbackground="red", state=DISABLED)

# Creación de Labeles y Textos

# Label F I L A S
row = StringVar()
label_row = Label(window, text="F I L A S : ", width=15)
text_row = Entry(textvariable=row, width=15)

# Label C O L U M N A S
col = StringVar()
label_col = Label(window, text="C O L U M N A S : ", width=15)
text_col = Entry(textvariable=col, width=15)

# Label B O M B A S
bomb = StringVar()
label_bomb = Label(window, text="B O M B A S : ", width=15)
text_bomb = Entry(textvariable=bomb, width=15)

# Creación de Botones

# Botón J U G A R
boton_inicio = Button(window, text="J U G A R", width=30, command=abrir_config)
boton_inicio.pack()
boton_inicio.place(relx=0.5, rely=0.6, anchor=CENTER)

# Botón R E G L A S
boton_ins = Button(window, text="R E G L A S", width=30, command=abrir_rules)
boton_ins.pack()
boton_ins.place(relx=0.5, rely=0.7, anchor=CENTER)

# Botón S A L I R
boton_exit = Button(window, text="S A L I R", width=30, command=exit_game)
boton_exit.pack()
boton_exit.place(relx=0.5, rely=0.8, anchor=CENTER)

# Botón V O L V E R
boton_volver = Button(window, text="V O L V E R", width=15, command=init_menu)

# Botón P R I N C I P I A N T E
boton_pri = Button(window, text="P R I N C I P I A N T E", width=30, command=init_pri)

# Botón I N T E R M E D I O
boton_int = Button(window, text="I N T E R M E D I O", width=30, command=init_int)

# Botón E X P E R T O
boton_exp = Button(window, text="E X P E R T O", width=30, command=init_exp)

# Botón P E R S O N A L I Z A D O
boton_per = Button(window, text="P E R S O N A L I Z A D O", width=30, command=init_per_menu)

# Botón C O N T I N U A R
boton_con = Button(window, text="C O N T I N U A R", width=15, command=read_per)

center(window)
window.mainloop()