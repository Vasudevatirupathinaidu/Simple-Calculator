# Simple Calculator

from tkinter import *

root = Tk()

root.title("Calculator")
root.resizable(0,0)

# root.geometry("400x400")

root.configure(bg="#fff")


# Input
entry = Entry(root, width=35, borderwidth=2)

entry.grid(row=0, column=0, columnspan=3, padx=10, pady=15)


# functions
def button_click(number):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, str(current) + str(number))

def button_clear():
    entry.delete(0, END)

def button_add():
    first_number = entry.get()
    global f_num
    global math_operator
    math_operator = "add"

    try:
        f_num = int(first_number)
    except ValueError:
        pass

    entry.delete(0, END)

def button_subtraction():
    first_number = entry.get()
    global f_num
    global math_operator
    math_operator = "sub"

    try:
        f_num = int(first_number)
    except ValueError:
        pass

    entry.delete(0, END)

def button_multiplication():
    first_number = entry.get()
    global f_num
    global math_operator
    math_operator = "mul"

    try:
        f_num = int(first_number)
    except ValueError:
        pass

    entry.delete(0, END)

def button_division():
    first_number = entry.get()
    global f_num
    global math_operator
    math_operator = "div"

    try:
        f_num = int(first_number)
    except ValueError:
        pass

    entry.delete(0, END)

def button_equal():
    second_number = entry.get()
    entry.delete(0, END)

    try:
        if math_operator == "add":
            entry.insert(0, f_num + int(second_number))
    except ValueError:
        pass
    except NameError:
        pass

    try:       
        if math_operator == "sub":
            entry.insert(0, f_num - int(second_number))
    except ValueError:
        pass
    except NameError:
        pass

    try:        
        if math_operator == "mul":
            entry.insert(0, f_num * int(second_number))
    except ValueError:
        pass
    except NameError:
        pass

    try: 
        if math_operator == "div":
            entry.insert(0, f_num / int(second_number))
    except ValueError:
        pass
    except ZeroDivisionError:
        pass
    except NameError:
        pass


# Buttons for display numbers and math operators
btn1 = Button(root, padx=39, pady=20, text="1", bg="#1a3365", fg="#ffbb00", borderwidth=1, activebackground="#021F4B", activeforeground="white", relief=FLAT, cursor="hand2", command=lambda: button_click(1))
btn2 = Button(root, padx=40, pady=20, text="2", bg="#1a3365", fg="#ffbb00", borderwidth=1, activebackground="#021F4B", activeforeground="white", relief=FLAT, cursor="hand2", command=lambda: button_click(2))
btn3 = Button(root, padx=40, pady=20, text="3", bg="#1a3365", fg="#ffbb00", borderwidth=1, activebackground="#021F4B", activeforeground="white", relief=FLAT, cursor="hand2", command=lambda: button_click(3))
btn4 = Button(root, padx=39, pady=20, text="4", bg="#1a3365", fg="#ffbb00", borderwidth=1, activebackground="#021F4B", activeforeground="white", relief=FLAT, cursor="hand2", command=lambda: button_click(4))
btn5 = Button(root, padx=40, pady=20, text="5", bg="#1a3365", fg="#ffbb00", borderwidth=1, activebackground="#021F4B", activeforeground="white", relief=FLAT, cursor="hand2", command=lambda: button_click(5))
btn6 = Button(root, padx=40, pady=20, text="6", bg="#1a3365", fg="#ffbb00", borderwidth=1, activebackground="#021F4B", activeforeground="white", relief=FLAT, cursor="hand2", command=lambda: button_click(6))
btn7 = Button(root, padx=39, pady=20, text="7", bg="#1a3365", fg="#ffbb00", borderwidth=1, activebackground="#021F4B", activeforeground="white", relief=FLAT, cursor="hand2", command=lambda: button_click(7))
btn8 = Button(root, padx=40, pady=20, text="8", bg="#1a3365", fg="#ffbb00", borderwidth=1, activebackground="#021F4B", activeforeground="white", relief=FLAT, cursor="hand2", command=lambda: button_click(8))
btn9 = Button(root, padx=40, pady=20, text="9", bg="#1a3365", fg="#ffbb00", borderwidth=1, activebackground="#021F4B", activeforeground="white", relief=FLAT, cursor="hand2", command=lambda: button_click(9))
btn0 = Button(root, padx=39, pady=20, text="0", bg="#1a3365", fg="#ffbb00", borderwidth=1, activebackground="#021F4B", activeforeground="white", relief=FLAT, cursor="hand2", command=lambda: button_click(0))

btn_add = Button(root, padx=38, pady=20, text="+", bg="#ffffff", fg="#1a3365", borderwidth=1, activebackground="#021F4B", activeforeground="white", relief=FLAT, cursor="hand2", command=button_add)
btn_equal = Button(root, padx=88, pady=20, text="=", bg="#ff4343", fg="#ffffff", borderwidth=1, activebackground="#ffffff", activeforeground="#ff4343", relief=FLAT, cursor="hand2", command=button_equal)
btn_clear = Button(root, padx=78, pady=20, text="Clear", bg="#ffbb00", fg="#1a3365", borderwidth=1, activebackground="#ffffff", activeforeground="#ffbb00", relief=FLAT, cursor="hand2", command=button_clear)

btn_subtraction = Button(root, padx=40, pady=20, text="-", bg="#ffffff", fg="#1a3365", borderwidth=1, activebackground="#021F4B", activeforeground="#ffffff", relief=FLAT, cursor="hand2", command=button_subtraction)
btn_multiplication = Button(root, padx=40, pady=20, text="*", bg="#ffffff", fg="#1a3365", borderwidth=1, activebackground="#021F4B", activeforeground="#ffffff", relief=FLAT, cursor="hand2", command=button_multiplication)
btn_division = Button(root, padx=40, pady=20, text="/", bg="#ffffff", fg="#1a3365", borderwidth=1, activebackground="#021F4B", activeforeground="white", relief=FLAT, cursor="hand2", command=button_division)


btn1.grid(row=3, column=0, pady=1)
btn2.grid(row=3, column=1, pady=1)
btn3.grid(row=3, column=2, pady=1)

btn4.grid(row=2, column=0, pady=1)
btn5.grid(row=2, column=1, pady=1)
btn6.grid(row=2, column=2, pady=1)

btn7.grid(row=1, column=0, pady=1)
btn8.grid(row=1, column=1, pady=1)
btn9.grid(row=1, column=2, pady=1)

btn0.grid(row=4, column=0, pady=1)
btn_clear.grid(row=4, column=1, columnspan=2, pady=1)

btn_add.grid(row=5, column=0, pady=1)
btn_equal.grid(row=5, column=1, columnspan=2, pady=1)

btn_subtraction.grid(row=6, column=0, pady=1)
btn_multiplication.grid(row=6, column=1, pady=1)
btn_division.grid(row=6, column=2, pady=1)


root.mainloop()