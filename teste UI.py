import math
from tkinter import *
from tkinter import messagebox
def get_height():
    height = float(ENTRY2.get())
    return height
def get_grid():
    grid = float(ENTRY1.get())
    return grid
def calculate_bmi(): 
    try:
        height = get_height()
        weight = get_grid()
        height = height / 100.0
        bmi = weight / (height ** 2)
    except ZeroDivisionError:
        messagebox.showinfo("Result", "Please enter positive height!!")
    except ValueError:
        messagebox.showinfo("Result", "Please enter valid data!")
    else:
        messagebox.showinfo("Your BMI Calculated is : ", bmi)

def open_popup():
    top= Toplevel(TOP)
    top.geometry("250x250")
    top.title("Child Window")
    Label(top, text= "Hello World!", font=('Mistral 18 bold')).place(x=150,y=80)
    

if __name__ == '__main__':
    TOP = Tk()
    TOP.bind("<Return>", calculate_bmi)
    TOP.geometry("600x600")
    TOP.configure(background="#000000")
    TOP.title("Sudokinho dos Broder")
    TOP.resizable(width=True, height=True)
    LABLE = Label(TOP, bg="#ff7f00",fg="#ffffff", text="Sudokinho", font=("Helvetica", 15, "bold"), pady=10)
    LABLE.place(x=150, y=0)
    


    #n_groups = int(input())
    n_groups = 9        # trocar por get_grid de alguma forma
    n_input_numbers = n_groups

    n_sqrt = math.sqrt(n_groups)

    gap = 30
    gap_group = (n_sqrt)* gap + 10

    x_margin = 50
    y_margin = 60

    sudoku = []

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
                    
            sudoku[group].append(Entry(TOP, bd=2, width=2, font="Roboto 11"))
            sudoku[group][input].place(x=x_coord, y=y_coord)

                #Fazer por listas de listas:

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


    ENTRY1 = Entry(TOP, bd=2, width=5, font="Roboto 11")
    ENTRY1.place(x=100, y=500) #input para o tamanho do grid

    BUTTON = Button(bg="#000000",fg='#ffffff', bd=2, text="GRID", padx=2, pady=2, command=get_grid,
                    font=("Helvetica", 8, "bold"))
    BUTTON.grid(row=5, column=0, sticky=W)
    BUTTON.place(x=150, y=500)

    BUTTON = Button(bg="#000000",fg='#ffffff', bd=12, text="CHECK", padx=33, pady=10, command=open_popup,
                    font=("Helvetica", 20, "bold"))
    BUTTON.grid(row=5, column=0, sticky=W)
    BUTTON.place(x=100, y=400)

    TOP.mainloop()
    