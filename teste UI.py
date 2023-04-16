import math
import sys
import os
from tkinter import *
from tkinter import ttk
import tkinter as tk

gridnumber = 0
sudoku = []





def popupBonus():   #novopopup para tentar pegar o valor de getgrid
    popupBonusWindow = tk.Toplevel()
    popupBonusWindow.wm_title("Grid")
    popx = root.winfo_rootx() + int(root.winfo_width()/2) - 100
    popy = root.winfo_rooty() + int(root.winfo_height()/2) - 60
  
    popupBonusWindow.geometry(f'200x120+{popx}+{popy}')

    frameA = ttk.Frame(popupBonusWindow) #considerar fazer 2 frames para o titulo fica melhor
    frameA.pack(expand=True)

    labelBonus = tk.Label(frameA, text="Type your desired Grid").pack()
    ENTRY1 = ttk.Entry(frameA, width=5, font="Roboto 11").pack() #input para o tamanho do grid
    B1 = ttk.Button(frameA, text="Okay", command=(popupBonusWindow.destroy)).pack()

def check_test():
    print(sudoku[2][0].get())   #teste para checar se os entrys funcionam

def choose_grid():
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
    ENTRYGRID.destroy()         #retirei o botão grid quando é apertado
    BUTTONGRID.destroy()           #Por enquanto para um novo jogo é preciso reabrir o programa


def print_sudoku(n_groups):
    # if len(sudoku) == 0: pass
    # else :
    #     for group in range(len(sudoku)):
    #         for input in range(len(sudoku)):
    #             sudoku[group][input].place_forget()       Tentativa de fazer o grid remontar quando
    #     #sudoku[2][0].place()                             clicado pela segunda vez

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
                    
            sudoku[group].append(Entry(root, bd=2, width=2, justify=CENTER, font="Roboto 11"))
            sudoku[group][input].place(x=x_coord, y=y_coord) 

if __name__ == '__main__':
    root = Tk()
    # root.bind("<Return>", calculate_bmi)

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
    

    BUTTON = Button(bg="#000000",fg='#ffffff', bd=12, text="CHECK", padx=33, pady=10, command=popupBonus ,
                    font=("Helvetica", 20, "bold"))
    BUTTON.grid(row=5, column=0, sticky=W)
    BUTTON.place(x=100, y=400)

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