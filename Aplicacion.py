from tkinter import ttk,Tk,StringVar,messagebox
from tkinter.constants import *
import requests

class Aplicacion():
    __ventana=None
    __dolares=None
    __pesos=None

    def __init__(self):
        complete_url = 'https://www.dolarsi.com/api/api.php?type=dolar'
        r = requests.get(complete_url)
        x = r.json()
        i = 0
        while (i < len(x)) and (x[i]['casa']['nombre']!='Oficial'):
            i+=1
        if i < len(x):
            self.__venta=float(x[i]['casa']['venta'].replace(',','.'))
        self.__ventana = Tk()
        self.__ventana.geometry('290x115')
        self.__ventana.title('Conversor de moneda')

        mainframe = ttk.Frame(self.__ventana, padding="5 5 12 5")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        mainframe.columnconfigure(0, weight=1)
        mainframe.rowconfigure(0, weight=1)
        mainframe['borderwidth'] = 2
        mainframe['relief'] = 'sunken'
        self.__dolares = StringVar()
        self.__pesos = StringVar()
        self.__dolares.trace('w',self.conversor)
        self.dolaresEntry=ttk.Entry(mainframe,width=10,textvariable=self.__dolares).\
            grid(column=2,row=1,sticky=(W,E))
        ttk.Label(mainframe,text='dolares').\
            grid(column=3,row=1,sticky=W)
        ttk.Label(mainframe,text='es equivalente a ').\
            grid(column=1,row=2,sticky=E)
        ttk.Label(mainframe,textvariable=self.__pesos).\
            grid(column=2,row=2,sticky=(W,E))
        ttk.Label(mainframe,text='pesos').\
            grid(column=3,row=2,sticky=W)
        ttk.Button(mainframe,text='Salir',command=self.__ventana.destroy).\
            grid(column=3,row=3,sticky=W)

        for child in mainframe.winfo_children():
            child.grid_configure(padx=5, pady=5)
        self.__ventana.mainloop()


    def conversor(self,*args):
        if self.__dolares.get()!='':
            try:
                dolares=float(self.__dolares.get())
                valor=self.__venta
                pesos='{:.2f}'.format(valor*dolares)
                self.__pesos.set(pesos)
            except ValueError:
                messagebox.showerror(title='Error',
                                     message='Debe ingresar valor numerico')
                self.__dolares.set('')

        else:
            self.__pesos.set('')