import tkinter as tk
from tkinter import messagebox
def calcular_temps():
    if celcius_entry.get() or fahrenheit_entry.get() or kelvin_entry.get():
        try:
            if celcius_entry.get():
                c = float(celcius_entry.get())
                f = (c * 9/5) + 32
                k = c + 273.15
                fahrenheit_entry.delete(0, tk.END)
                kelvin_entry.delete(0, tk.END)
                fahrenheit_entry.insert(0, f)
                kelvin_entry.insert(0, k)
            elif fahrenheit_entry.get():
                f = float(fahrenheit_entry.get())
                c = (f - 32) * 5/9
                k = c + 273.15
                celcius_entry.delete(0, tk.END)
                kelvin_entry.delete(0, tk.END)
                celcius_entry.insert(0, c)
                kelvin_entry.insert(0, k)
            elif kelvin_entry.get():
                k = float(kelvin_entry.get())
                c = k - 273.15
                f = (c * 9/5) + 32
                celcius_entry.delete(0, tk.END)
                fahrenheit_entry.delete(0, tk.END)
                celcius_entry.insert(0, c)
                fahrenheit_entry.insert(0, f)
        except ValueError:
            messagebox.showerror("Error", "Por favor ingrese un numero valido")


def limpiar_temps():
    celcius_entry.delete(0, tk.END)
    fahrenheit_entry.delete(0, tk.END)
    kelvin_entry.delete(0, tk.END)
    messagebox.showinfo("Limpiar", "Campos limpiados correctamente")

    print("limpiand")
ventana= tk.Tk()
ventana.title("Conversor de Temperaturas")


#Etiquetas para las temperaturas
tk.Label(ventana, text="Celcius").grid(row=0,column=0,padx=10,pady=10)
tk.Label(ventana, text="Fahrenheit").grid(row=1,column=0,padx=10,pady=10)
tk.Label(ventana, text="Kelvin").grid(row=2,column=0,padx=10,pady=10)

#Entradas para las temperaturas
celcius_entry = tk.Entry(ventana)
fahrenheit_entry= tk.Entry(ventana)
kelvin_entry = tk.Entry(ventana)

celcius_entry.grid(row=0,column=1,padx=10,pady=10)
fahrenheit_entry.grid(row=1,column=1,padx=10,pady=10)
kelvin_entry.grid(row=2,column=1,padx=10,pady=10)

#Boton para convertir
btn_calcular= tk.Button(ventana, text="Calcular", command=calcular_temps)
btn_limpiar= tk.Button(ventana, text="Limpiar", command=limpiar_temps)

btn_calcular.grid(row=3,column=0,columnspan=2,pady=10)
btn_limpiar.grid(row=4,column=0,columnspan=2,pady=10)

#Ejecucuin de ventana
ventana.mainloop()
