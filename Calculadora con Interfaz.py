
import tkinter as tk

root = tk.Tk()

numero1 = tk.StringVar()
numero2 = tk.StringVar()
mensaje = tk.StringVar()


def sumar():
    num1 = numero1.get()
    num2 = numero2.get()
    n1 = int(num1)
    n2 = int(num2)
    sum = n1+n2
    mensaje.set(sum)
    numero1.set('')
    numero2.set('')


def restar():
    num1 = numero1.get()
    num2 = numero2.get()
    n1 = int(num1)
    n2 = int(num2)
    res = n1-n2
    mensaje.set(res)
    numero1.set('')
    numero2.set('')

def multiplicar():
    num1 = numero1.get()
    num2 = numero2.get()
    n1 = int(num1)
    n2 = int(num2)
    mul = n1*n2
    mensaje.set(mul)
    numero1.set('')
    numero2.set('')

def dividir():
    num1 = numero1.get()
    num2 = numero2.get()
    n1 = int(num1)
    n2 = int(num2)
    div = n1/n2
    mensaje.set(div)
    numero1.set('')
    numero2.set('')



root.geometry('500x400')
root.title('CALCULADORA')

root.configure(bg="#48466d")

tk.Label(root, text='CALCULADORA :)', bg="#48466d", fg='#46cdcf', font=('', 32)).place(x=60, y=30)

#Entrada de los dos numeros
tk.Label(root, text='Numero 1:', bg="#48466d", fg='#46cdcf', font=('', 20)).place(x=100, y=120)
tk.Entry(root, justify='center', textvariable=numero1, ).place(x=250, y=130)

tk.Label(root, text='Numero 2:', bg="#48466d", fg='#46cdcf', font=('', 20)).place(x=100, y=170)
tk.Entry(root, justify='center', textvariable=numero2).place(x=250, y=180)

#Sumar
tk.Button(root, text='SUMAR', bd=0, command=sumar).place(x=150, y=225)

#Restar
tk.Button(root, text='RESTAR', bd=0, command=restar).place(x=200, y=225)

#Multiplicar
tk.Button(root, text='MULTIPLICAR', bd=0, command=multiplicar).place(x=250, y=225)

#Division
tk.Button(root, text='DIVIDIR', bd=0, command=dividir).place(x=333, y=225)


tk.Label(root, text='Resultado:', bg="#48466d", fg='#46cdcf', font=('', 20)).place(x=100, y=280)
tk.Entry(root,justify = 'center', textvariable=mensaje, bg='white', fg='black').place(x=250, y=290)
tk.Button(root, text='Salir', bd=0, command=root.destroy).place(x=250, y=350)

root.mainloop()