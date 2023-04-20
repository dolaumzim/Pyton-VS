import math
import sys
import os
from tkinter import *
from tkinter import ttk
import tkinter as tk

gridnumber = 0
sudoku = []
color = '#FFFFFF'


def popupBonus():   #popup que mostra que checou certo
    popupBonusWindow = tk.Toplevel()
    popupBonusWindow.wm_title("Grid")
    popx = root.winfo_rootx() + int(root.winfo_width()/2) - 100
    popy = root.winfo_rooty() + int(root.winfo_height()/2) - 60
  
    popupBonusWindow.geometry(f'200x120+{popx}+{popy}')

    frameA = ttk.Frame(popupBonusWindow) #considerar fazer 2 frames para o titulo fica melhor
    frameA.pack(expand=True)

    labelBonus = tk.Label(frameA, text="Muito Bom, nota 2!").pack()
    labelBonus = tk.Label(frameA, text="").pack()
    #ENTRY1 = ttk.Entry(frameA, width=5, font="Roboto 11").pack() #input para o tamanho do grid
    B1 = ttk.Button(frameA, text="Okay", command=(popupBonusWindow.destroy)).pack()

def popupBonus2():   #popup que mostra que checou errado
    popupBonusWindow2 = tk.Toplevel()
    popupBonusWindow2.wm_title("Grid")
    popx = root.winfo_rootx() + int(root.winfo_width()/2) - 100
    popy = root.winfo_rooty() + int(root.winfo_height()/2) - 60
  
    popupBonusWindow2.geometry(f'200x120+{popx}+{popy}')

    frameB = ttk.Frame(popupBonusWindow2) #considerar fazer 2 frames para o titulo fica melhor
    frameB.pack(expand=True)

    labelBonus = tk.Label(frameB, text="Ô Burro!").pack()
    labelBonus = tk.Label(frameB, text="").pack()
    #ENTRY1 = ttk.Entry(frameA, width=5, font="Roboto 11").pack() #input para o tamanho do grid
    B1 = ttk.Button(frameB, text="Okay", command=(popupBonusWindow2.destroy)).pack()

def check_test():   #teste de checagem de resposta, por enquanto chega se dentro de um quadrado há repetição
    for y in range (n_groups):
        check = []
        for x in range (n_groups): 
            check.append(sudoku[y][x].get())
        dup = {x for x in check if check.count(x) > 1}
        if dup != set():
            print(f'sudoku {y}{dup}')
        else : 
            popupBonus()

def choose_grid():  #seleciona o tamanho da grade

    if sudoku != [] : erase_sudoku() #apaga a grade se já existir uma

    global n_groups #transforma a variável em global para ser usada em outras funções
    if ENTRYGRID.get() == '': 
        n_groups = 9
    else : 
        gridnumber = int(ENTRYGRID.get())
        if gridnumber == 2 :
            n_groups = 4
        elif gridnumber == 3 :
            n_groups = 9        
        elif gridnumber == 4 :
            n_groups = 16
        elif gridnumber == 5 :
             n_groups = 25

    print_sudoku(n_groups)
    #ENTRYGRID.destroy()         #retirei o botão grid quando é apertado
    #BUTTONGRID.destroy()           #Por enquanto para um novo jogo é preciso reabrir o programa

def print_sudoku(n_groups): #imprime grade

    x_margin = 60
    y_margin = 80
    gap = 30

    n_input_numbers = n_groups
    n_sqrt = math.sqrt(n_groups)
    gap_group = (n_sqrt)* gap + 10

    for group in range(n_groups):
        sudoku.append([])
        x_coord = x_margin + (group%n_sqrt)*gap_group
        y_coord = y_margin + (group//n_sqrt)*gap_group
        for input in range(n_input_numbers):
            if (input == 0):
                pass
            elif (input == n_sqrt):
                x_coord = x_margin + (group%n_sqrt)*gap_group
                y_coord = y_coord + gap
            elif (input == 2*n_sqrt):
                x_coord = x_margin + (group%n_sqrt)*gap_group
                y_coord = y_coord + gap
            elif (input == 3*n_sqrt):
                x_coord = x_margin + (group%n_sqrt)*gap_group
                y_coord = y_coord + gap
            elif (input == 4*n_sqrt):
                x_coord = x_margin + (group%n_sqrt)*gap_group
                y_coord = y_coord + gap
            else:
                x_coord = x_coord + gap
                    
            sudoku[group].append(Entry(root, bd=2, width=2, background= color, justify=CENTER, font="Roboto 11"))
            sudoku[group][input].place(x=x_coord, y=y_coord) 

def erase_sudoku(): #apaga a grade
    for group in range(n_groups):
        for input in range(n_groups):
            sudoku[group][input].place_forget()

def insert_sudoku(): #insere um jogo específico

    for group in range(n_groups):
        for input in range(n_groups):
           sudoku[group][input].delete(0,END) 

    sudoku[0][0].insert(0,'') #1
    sudoku[0][1].insert(0,'')
    sudoku[0][2].insert(0,'')
    sudoku[0][3].insert(0,'7')
    sudoku[0][4].insert(0,'3')
    sudoku[0][5].insert(0,'')
    sudoku[0][6].insert(0,'')
    sudoku[0][7].insert(0,'')
    sudoku[0][8].insert(0,'9')

    sudoku[1][0].insert(0,'1') #2
    sudoku[1][1].insert(0,'')
    sudoku[1][2].insert(0,'9')
    sudoku[1][3].insert(0,'')
    sudoku[1][4].insert(0,'4')
    sudoku[1][5].insert(0,'2')
    sudoku[1][6].insert(0,'')
    sudoku[1][7].insert(0,'')
    sudoku[1][8].insert(0,'')

    sudoku[2][0].insert(0,'') #3
    sudoku[2][1].insert(0,'7')
    sudoku[2][2].insert(0,'')
    sudoku[2][3].insert(0,'')
    sudoku[2][4].insert(0,'8')
    sudoku[2][5].insert(0,'')
    sudoku[2][6].insert(0,'6')
    sudoku[2][7].insert(0,'')
    sudoku[2][8].insert(0,'')

    sudoku[3][0].insert(0,'8') #4
    sudoku[3][1].insert(0,'2')
    sudoku[3][2].insert(0,'')
    sudoku[3][3].insert(0,'')
    sudoku[3][4].insert(0,'9')
    sudoku[3][5].insert(0,'')
    sudoku[3][6].insert(0,'1')
    sudoku[3][7].insert(0,'')
    sudoku[3][8].insert(0,'')

    sudoku[4][0].insert(0,'') #5
    sudoku[4][1].insert(0,'7')
    sudoku[4][2].insert(0,'')
    sudoku[4][3].insert(0,'')
    sudoku[4][4].insert(0,'')
    sudoku[4][5].insert(0,'')
    sudoku[4][6].insert(0,'')
    sudoku[4][7].insert(0,'6')
    sudoku[4][8].insert(0,'')

    sudoku[5][0].insert(0,'') #6
    sudoku[5][1].insert(0,'')
    sudoku[5][2].insert(0,'9')
    sudoku[5][3].insert(0,'')
    sudoku[5][4].insert(0,'3')
    sudoku[5][5].insert(0,'')
    sudoku[5][6].insert(0,'')
    sudoku[5][7].insert(0,'5')
    sudoku[5][8].insert(0,'2')

    sudoku[6][0].insert(0,'') #7
    sudoku[6][1].insert(0,'')
    sudoku[6][2].insert(0,'7')
    sudoku[6][3].insert(0,'')
    sudoku[6][4].insert(0,'6')
    sudoku[6][5].insert(0,'')
    sudoku[6][6].insert(0,'')
    sudoku[6][7].insert(0,'5')
    sudoku[6][8].insert(0,'')

    sudoku[7][0].insert(0,'') #8
    sudoku[7][1].insert(0,'')
    sudoku[7][2].insert(0,'')
    sudoku[7][3].insert(0,'2')
    sudoku[7][4].insert(0,'5')
    sudoku[7][5].insert(0,'')
    sudoku[7][6].insert(0,'4')
    sudoku[7][7].insert(0,'')
    sudoku[7][8].insert(0,'6')

    sudoku[8][0].insert(0,'1') #9
    sudoku[8][1].insert(0,'')
    sudoku[8][2].insert(0,'')
    sudoku[8][3].insert(0,'')
    sudoku[8][4].insert(0,'4')
    sudoku[8][5].insert(0,'8')
    sudoku[8][6].insert(0,'')
    sudoku[8][7].insert(0,'')
    sudoku[8][8].insert(0,'')

def check_sudoku(): #checa o jogo específico inserido
    solution = []
    for group in range(n_groups):
        solution.append([])
        for input in range(n_groups):
            solution[group].append('')

    solution[0][0]='6' #1
    solution[0][1]='8'
    solution[0][2]='2'
    solution[0][3]='7'
    solution[0][4]='3'
    solution[0][5]='5'
    solution[0][6]='4'
    solution[0][7]='1'
    solution[0][8]='9'

    solution[1][0]='1' #2
    solution[1][1]='3'
    solution[1][2]='9'
    solution[1][3]='6'
    solution[1][4]='4'
    solution[1][5]='2'
    solution[1][6]='7'
    solution[1][7]='8'
    solution[1][8]='5'

    solution[2][0]='5' #3
    solution[2][1]='7'
    solution[2][2]='4'
    solution[2][3]='9'
    solution[2][4]='8'
    solution[2][5]='1'
    solution[2][6]='6'
    solution[2][7]='2'
    solution[2][8]='3'

    solution[3][0]='8' #4
    solution[3][1]='2'
    solution[3][2]='6'
    solution[3][3]='5'
    solution[3][4]='9'
    solution[3][5]='4'
    solution[3][6]='1'
    solution[3][7]='7'
    solution[3][8]='3'

    solution[4][0]='5' #5
    solution[4][1]='7'
    solution[4][2]='3'
    solution[4][3]='8'
    solution[4][4]='2'
    solution[4][5]='1'
    solution[4][6]='9'
    solution[4][7]='6'
    solution[4][8]='4'

    solution[5][0]='4' #6
    solution[5][1]='1'
    solution[5][2]='9'
    solution[5][3]='7'
    solution[5][4]='3'
    solution[5][5]='6'
    solution[5][6]='8'
    solution[5][7]='5'
    solution[5][8]='2'

    solution[6][0]='2' #7
    solution[6][1]='4'
    solution[6][2]='7'
    solution[6][3]='9'
    solution[6][4]='6'
    solution[6][5]='1'
    solution[6][6]='3'
    solution[6][7]='5'
    solution[6][8]='8'

    solution[7][0]='3' #8
    solution[7][1]='9'
    solution[7][2]='8'
    solution[7][3]='2'
    solution[7][4]='5'
    solution[7][5]='7'
    solution[7][6]='4'
    solution[7][7]='1'
    solution[7][8]='6'

    solution[8][0]='1' #9
    solution[8][1]='6'
    solution[8][2]='5'
    solution[8][3]='3'
    solution[8][4]='4'
    solution[8][5]='8'
    solution[8][6]='2'
    solution[8][7]='9'
    solution[8][8]='7'
    
    for group in range(n_groups):
        for input in range(n_groups):
            if solution[group][input] != sudoku[group][input].get() :
                popupBonus2()
                return 0
    popupBonus()
    

if __name__ == '__main__':
    root = Tk()
    root.bind("<Return>", lambda e: check_test())
    root.bind("<Tab>", lambda e: root.focus_set())

    sizex = 400 #colocar como variavel dependendo do gridsize
    sizey = 500 #colocar como variavel dependendo do gridsize
    posx = int(root.winfo_vrootwidth()/2) - int(sizex/2)
    posy = int(root.winfo_vrootheight()/2) - int(sizey/2)

    root.geometry(f'{sizex}x{sizey}+{posx}+{posy}')
    root.configure(background="#000000")
    root.title("Sudokinho dos Broder")
    root.resizable(width=True, height=True)

    # framesudoku = ttk.Frame(root)
    # framesudoku.pack(side=BOTTOM, expand=True)
    # frametitle = ttk.Frame(root)
    # frametitle.pack(side=TOP, expand=True)
    LABLE = Label(root, bg="#ff7f00",fg="#ffffff", text="Sudokinho", font=("Helvetica", 15, "bold"), pady=10)
    LABLE.place(x=150, y=0)
    
    ENTRYGRID = ttk.Entry( width=5, font="Roboto 11")
    ENTRYGRID.place(x=27, y=420)

    for x in color:# coloquei somente para poder minimizar, depois retirar for
        soma= 1+1
        # if gridnumber == 0 :
        #     n_groups = 9
        #     print('default')
        # elif gridnumber == 2 :
        #     n_groups = 4
        #     print('aqui')
        # elif gridnumber == 3 :
        #     n_groups = 9        # trocar por get_grid de alguma
        # elif gridnumber == 4 :
        #     n_groups = 16
        # elif gridnumber == 5 :
        #     n_groups = 25

        # n_input_numbers = n_groups

        # n_sqrt = math.sqrt(n_groups)

        # gap = 30
        # gap_group = (n_sqrt)* gap + 10

        # x_margin = 50
        # y_margin = 80

        # sudoku = []
        # tretas = 0
        # for group in range(n_groups):
        #     sudoku.append([])
        #     x_coord = x_margin + (group%n_sqrt)*gap_group
        #     y_coord = y_margin + (group//n_sqrt)*gap_group
        #     for input in range(n_input_numbers):
        #         if (input == 0):
        #             pass
        #         elif (input == n_sqrt):
        #             x_coord = x_margin + (group%n_sqrt)*gap_group
        #             y_coord = y_coord + gap
        #         elif (input == 2*n_sqrt):
        #             x_coord = x_margin + (group%n_sqrt)*gap_group
        #             y_coord = y_coord + gap
        #         elif (input == 3*n_sqrt):
        #             x_coord = x_margin + (group%n_sqrt)*gap_group
        #             y_coord = y_coord + gap
        #         elif (input == 4*n_sqrt):
        #             x_coord = x_margin + (group%n_sqrt)*gap_group
        #             y_coord = y_coord + gap
        #         else:
        #             x_coord = x_coord + gap
                        
        #         sudoku[group].append(Entry(root, bd=2, width=2, font="Roboto 11"))
        #         sudoku[group][input].place(x=x_coord, y=y_coord)

    
    BUTTONGRID = Button(bg="#000000",fg='#ffffff', bd=5, text="GRID", padx=2, pady=2, command=choose_grid,
                    font=("Helvetica", 10, "bold"))
    BUTTONGRID.grid(row=5, column=1, sticky=W)
    BUTTONGRID.place(x=25, y=450)
    

    BUTTON = Button(bg="#000000",fg='#ffffff', bd=12, text="CHECK", padx=33, pady=10, command= check_sudoku,
                    font=("Helvetica", 20, "bold"))
    BUTTON.grid(row=5, column=0, sticky=W)
    BUTTON.place(x=100, y=400)

    BUTTONINSERT = Button(bg="#000000",fg='#ffffff', bd=5, text="NEW", padx=2, pady=2, command=insert_sudoku,
                    font=("Helvetica", 10, "bold"))
    BUTTONINSERT.grid(row=5, column=1, sticky=W)
    BUTTONINSERT.place(x=320, y=450)

    root.mainloop()
    


                    #  |  |  |
                # [2, 5, 0, 0, 3, 0, 9, 0, 1],
                # [0, 1, 0, 0, 0, 4, 0, 0, 0],
                # [4, 0, 7, 0, 0, 0, 2, 0, 8],
                #  |  |  |
                # [0, 0, 5, 2, 0, 0, 0, 0, 0],
                # [0, 0, 0, 0, 9, 8, 1, 0, 0],
                # [0, 4, 0, 0, 0, 3, 0, 0, 0],
                #  |  |  |
                # [0, 0, 0, 3, 6, 0, 0, 7, 2],
                # [0, 7, 0, 0, 0, 0, 0, 0, 3],
                # [9, 0, 3, 0, 0, 0, 6, 0, 4]