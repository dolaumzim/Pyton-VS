from tkinter import *
from tkinter import messagebox
def get_height():
    height = float(ENTRY2.get())
    return height
def get_weight():
    weight = float(ENTRY1.get())
    return weight
def calculate_bmi(): 
    try:
        height = get_height()
        weight = get_weight()
        height = height / 100.0
        bmi = weight / (height ** 2)
    except ZeroDivisionError:
        messagebox.showinfo("Result", "Please enter positive height!!")
    except ValueError:
        messagebox.showinfo("Result", "Please enter valid data!")
    else:
        messagebox.showinfo("Your BMI Calculated is : ", bmi)

if __name__ == '__main__':
    TOP = Tk()
    TOP.bind("<Return>", calculate_bmi)
    TOP.geometry("400x600")
    TOP.configure(background="#8c52ff")
    TOP.title("Sudokinho dos Broder")
    TOP.resizable(width=False, height=False)
    LABLE = Label(TOP, bg="#8c52ff",fg="#ffffff", text="Sudokinho", font=("Helvetica", 15, "bold"), pady=10)
    LABLE.place(x=150, y=0)

    # margin = 50
    # gap = 30
    # gap_group = 50

    # n_group_rows = 3
    # n_group_columns = 3

    # n_input_rows = 3
    # n_input_columns = 3



    # for group_row in range(n_group_rows):
    #     for_column in range(n_group_columns):


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

    
    ENTRYA1 = Entry(TOP, bd=2, width=2, font="Roboto 11")
    ENTRYA1.place(x=50, y=60)
    
    ENTRYA2 = Entry(TOP, bd=2, width=2, font="Roboto 11")
    ENTRYA2.place(x=80, y=60)

    ENTRYA3 = Entry(TOP, bd=2, width=2, font="Roboto 11")
    ENTRYA3.place(x=110, y=60)

    ENTRYA4 = Entry(TOP, bd=2, width=2, font="Roboto 11")
    ENTRYA4.place(x=50, y=90)
    
    ENTRYA5 = Entry(TOP, bd=2, width=2, font="Roboto 11")
    ENTRYA5.place(x=80, y=90)

    ENTRYA6 = Entry(TOP, bd=2, width=2, font="Roboto 11")
    ENTRYA6.place(x=110, y=90)

    ENTRYA7 = Entry(TOP, bd=2, width=2, font="Roboto 11")
    ENTRYA7.place(x=50, y=120)
    
    ENTRYA8 = Entry(TOP, bd=2, width=2, font="Roboto 11")
    ENTRYA8.place(x=80, y=120)

    ENTRYA9 = Entry(TOP, bd=2, width=2, font="Roboto 11")
    ENTRYA9.place(x=110, y=120)

    ENTRYB1 = Entry(TOP, bd=2, width=2, font="Roboto 11")
    ENTRYB1.place(x=160, y=60)
    
    ENTRYB2 = Entry(TOP, bd=2, width=2, font="Roboto 11")
    ENTRYB2.place(x=190, y=60)

    ENTRYB3 = Entry(TOP, bd=2, width=2, font="Roboto 11")
    ENTRYB3.place(x=220, y=60)

    ENTRYB4 = Entry(TOP, bd=2, width=2, font="Roboto 11")
    ENTRYB4.place(x=160, y=90)
    
    ENTRYB5 = Entry(TOP, bd=2, width=2, font="Roboto 11")
    ENTRYB5.place(x=190, y=90)

    ENTRYB6 = Entry(TOP, bd=2, width=2, font="Roboto 11")
    ENTRYB6.place(x=220, y=90)

    ENTRYB7 = Entry(TOP, bd=2, width=2, font="Roboto 11")
    ENTRYB7.place(x=160, y=120)
    
    ENTRYB8 = Entry(TOP, bd=2, width=2, font="Roboto 11")
    ENTRYB8.place(x=190, y=120)

    ENTRYB9 = Entry(TOP, bd=2, width=2, font="Roboto 11")
    ENTRYB9.place(x=220, y=120)

    ENTRYC1 = Entry(TOP, bd=2, width=2, font="Roboto 11")
    ENTRYC1.place(x=270, y=60)
    
    ENTRYC2 = Entry(TOP, bd=2, width=2, font="Roboto 11")
    ENTRYC2.place(x=300, y=60)

    ENTRYC3 = Entry(TOP, bd=2, width=2, font="Roboto 11")
    ENTRYC3.place(x=330, y=60)

    ENTRYC4 = Entry(TOP, bd=2, width=2, font="Roboto 11")
    ENTRYC4.place(x=270, y=90)
    
    ENTRYC5 = Entry(TOP, bd=2, width=2, font="Roboto 11")
    ENTRYC5.place(x=300, y=90)

    ENTRYC6 = Entry(TOP, bd=2, width=2, font="Roboto 11")
    ENTRYC6.place(x=330, y=90)

    ENTRYC7 = Entry(TOP, bd=2, width=2, font="Roboto 11")
    ENTRYC7.place(x=270, y=120)
    
    ENTRYC8 = Entry(TOP, bd=2, width=2, font="Roboto 11")
    ENTRYC8.place(x=300, y=120)

    ENTRYC9 = Entry(TOP, bd=2, width=2, font="Roboto 11")
    ENTRYC9.place(x=330, y=120)

    ENTRYD1 = Entry(TOP, bd=2, width=2, font="Roboto 11")
    ENTRYD1.place(x=50, y=170)
    
    ENTRYD2 = Entry(TOP, bd=2, width=2, font="Roboto 11")
    ENTRYD2.place(x=80, y=170)

    ENTRYD3 = Entry(TOP, bd=2, width=2, font="Roboto 11")
    ENTRYD3.place(x=110, y=170)

    ENTRYD4 = Entry(TOP, bd=2, width=2, font="Roboto 11")
    ENTRYD4.place(x=50, y=200)
    
    ENTRYD5 = Entry(TOP, bd=2, width=2, font="Roboto 11")
    ENTRYD5.place(x=80, y=200)

    ENTRYD6 = Entry(TOP, bd=2, width=2, font="Roboto 11")
    ENTRYD6.place(x=110, y=200)

    ENTRYD7 = Entry(TOP, bd=2, width=2, font="Roboto 11")
    ENTRYD7.place(x=50, y=230)
    
    ENTRYD8 = Entry(TOP, bd=2, width=2, font="Roboto 11")
    ENTRYD8.place(x=80, y=230)

    ENTRYD9 = Entry(TOP, bd=2, width=2, font="Roboto 11")
    ENTRYD9.place(x=110, y=230)

    ENTRYE1 = Entry(TOP, bd=2, width=2, font="Roboto 11")
    ENTRYE1.place(x=160, y=170)
    
    ENTRYE2 = Entry(TOP, bd=2, width=2, font="Roboto 11")
    ENTRYE2.place(x=190, y=170)

    ENTRYE3 = Entry(TOP, bd=2, width=2, font="Roboto 11")
    ENTRYE3.place(x=220, y=170)

    ENTRYE4 = Entry(TOP, bd=2, width=2, font="Roboto 11")
    ENTRYE4.place(x=160, y=200)
    
    ENTRYE5 = Entry(TOP, bd=2, width=2, font="Roboto 11")
    ENTRYE5.place(x=190, y=200)

    ENTRYE6 = Entry(TOP, bd=2, width=2, font="Roboto 11")
    ENTRYE6.place(x=220, y=200)

    ENTRYE7 = Entry(TOP, bd=2, width=2, font="Roboto 11")
    ENTRYE7.place(x=160, y=230)
    
    ENTRYE8 = Entry(TOP, bd=2, width=2, font="Roboto 11")
    ENTRYE8.place(x=190, y=230)

    ENTRYE9 = Entry(TOP, bd=2, width=2, font="Roboto 11")
    ENTRYE9.place(x=220, y=230)

    ENTRYF1 = Entry(TOP, bd=2, width=2, font="Roboto 11")
    ENTRYF1.place(x=270, y=170)
    
    ENTRYF2 = Entry(TOP, bd=2, width=2, font="Roboto 11")
    ENTRYF2.place(x=300, y=170)

    ENTRYF3 = Entry(TOP, bd=2, width=2, font="Roboto 11")
    ENTRYF3.place(x=330, y=170)

    ENTRYF4 = Entry(TOP, bd=2, width=2, font="Roboto 11")
    ENTRYF4.place(x=270, y=200)
    
    ENTRYF5 = Entry(TOP, bd=2, width=2, font="Roboto 11")
    ENTRYF5.place(x=300, y=200)

    ENTRYF6 = Entry(TOP, bd=2, width=2, font="Roboto 11")
    ENTRYF6.place(x=330, y=200)

    ENTRYF7 = Entry(TOP, bd=2, width=2, font="Roboto 11")
    ENTRYF7.place(x=270, y=230)
    
    ENTRYF8 = Entry(TOP, bd=2, width=2, font="Roboto 11")
    ENTRYF8.place(x=300, y=230)

    ENTRYF9 = Entry(TOP, bd=2, width=2, font="Roboto 11")
    ENTRYF9.place(x=330, y=230)

    ENTRYG1 = Entry(TOP, bd=2, width=2, font="Roboto 11")
    ENTRYG1.place(x=50, y=170)
    
    ENTRYG2 = Entry(TOP, bd=2, width=2, font="Roboto 11")
    ENTRYG2.place(x=80, y=170)

    ENTRYG3 = Entry(TOP, bd=2, width=2, font="Roboto 11")
    ENTRYG3.place(x=110, y=170)

    ENTRYG4 = Entry(TOP, bd=2, width=2, font="Roboto 11")
    ENTRYG4.place(x=50, y=200)
    
    ENTRYG5 = Entry(TOP, bd=2, width=2, font="Roboto 11")
    ENTRYG5.place(x=80, y=200)

    ENTRYG6 = Entry(TOP, bd=2, width=2, font="Roboto 11")
    ENTRYG6.place(x=110, y=200)

    ENTRYG7 = Entry(TOP, bd=2, width=2, font="Roboto 11")
    ENTRYG7.place(x=50, y=230)
    
    ENTRYG8 = Entry(TOP, bd=2, width=2, font="Roboto 11")
    ENTRYG8.place(x=80, y=230)

    ENTRYG9 = Entry(TOP, bd=2, width=2, font="Roboto 11")
    ENTRYG9.place(x=110, y=230)

    ENTRYH1 = Entry(TOP, bd=2, width=2, font="Roboto 11")
    ENTRYH1.place(x=160, y=170)
    
    ENTRYH2 = Entry(TOP, bd=2, width=2, font="Roboto 11")
    ENTRYH2.place(x=190, y=170)

    ENTRYH3 = Entry(TOP, bd=2, width=2, font="Roboto 11")
    ENTRYH3.place(x=220, y=170)

    ENTRYH4 = Entry(TOP, bd=2, width=2, font="Roboto 11")
    ENTRYH4.place(x=160, y=200)
    
    ENTRYH5 = Entry(TOP, bd=2, width=2, font="Roboto 11")
    ENTRYH5.place(x=190, y=200)

    ENTRYH6 = Entry(TOP, bd=2, width=2, font="Roboto 11")
    ENTRYH6.place(x=220, y=200)

    ENTRYH7 = Entry(TOP, bd=2, width=2, font="Roboto 11")
    ENTRYH7.place(x=160, y=230)
    
    ENTRYH8 = Entry(TOP, bd=2, width=2, font="Roboto 11")
    ENTRYH8.place(x=190, y=230)

    ENTRYH9 = Entry(TOP, bd=2, width=2, font="Roboto 11")
    ENTRYH9.place(x=220, y=230)

    ENTRYI1 = Entry(TOP, bd=2, width=2, font="Roboto 11")
    ENTRYI1.place(x=270, y=170)
    
    ENTRYI2 = Entry(TOP, bd=2, width=2, font="Roboto 11")
    ENTRYI2.place(x=300, y=170)

    ENTRYI3 = Entry(TOP, bd=2, width=2, font="Roboto 11")
    ENTRYI3.place(x=330, y=170)

    ENTRYI4 = Entry(TOP, bd=2, width=2, font="Roboto 11")
    ENTRYI4.place(x=270, y=200)
    
    ENTRYI5 = Entry(TOP, bd=2, width=2, font="Roboto 11")
    ENTRYI5.place(x=300, y=200)

    ENTRYI6 = Entry(TOP, bd=2, width=2, font="Roboto 11")
    ENTRYI6.place(x=330, y=200)

    ENTRYI7 = Entry(TOP, bd=2, width=2, font="Roboto 11")
    ENTRYI7.place(x=270, y=230)
    
    ENTRYI8 = Entry(TOP, bd=2, width=2, font="Roboto 11")
    ENTRYI8.place(x=300, y=230)

    ENTRYI9 = Entry(TOP, bd=2, width=2, font="Roboto 11")
    ENTRYI9.place(x=330, y=230)

    BUTTON = Button(bg="#000000",fg='#ffffff', bd=12, text="CHECK", padx=33, pady=10, command=calculate_bmi,
                    font=("Helvetica", 20, "bold"))
    BUTTON.grid(row=5, column=0, sticky=W)
    BUTTON.place(x=115, y=400)

    TOP.mainloop()