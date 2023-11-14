#Importación de bibliotecas
import tkinter as tk
from tkinter import messagebox

#Definición de la clase loginApp
class LoginApp(tk.Tk):
    def __init__(self, root): #Constructor
        super().__init__() #Esta clase va a heredar atributos a la clase set_up
        self.root = root  #Parte de la interfaz de tkinter
        self.root.title("Inicio de Sesión") #Parte de la interfaz como titulo de pestaña
        self.check = tk.BooleanVar() #Parte de la interfaz de tkinter

        self.username_var = tk.StringVar() #Almacena el nombre de usuario
        self.password_var = tk.StringVar() #Almacena la cotraseña
        
        self.label = tk.Label(root, text="Inicio de Sesión") #Parte de la interfaz como titulo de la pagina
        self.label.place(relx=0.5, rely=0.1, anchor="center") #Parte de la interfaz de tkinter
        
        tk.Label(root, text="Nombre de Usuario:").place(relx=0.5, rely=0.2, anchor="center") #Parte de la interfaz para ingresar usuario
        self.username_entry = tk.Entry(root, textvariable=self.username_var) #Parte de la interfaz para la variable usuario
        self.username_entry.place(relx=0.5, rely=0.3, anchor="center") #Parte de la interfza para la variable usuario

        tk.Label(root, text="Contraseña:").place(relx=0.5, rely=0.4, anchor="center") #Parte de la interfaz para ingresar contraseña
        self.password_entry = tk.Entry(root, textvariable=self.password_var, show="*") #Parte de la interfaz para la variable contraseña
        self.password_entry.place(relx=0.5, rely=0.5, anchor="center") #Parte de la interfaz para la ariable contraseña

        self.IS = tk.Button(root, text="Iniciar Sesión", command=self.login) #Button para iniciar sesión
        self.IS.place(relx=0.5, rely=0.7, anchor="center") #Parte de la interfaz para iniciar sesión
        self.CC = tk.Button(root, text="Crear cuenta", command=self.set_up) #Button para crear cuenta
        self.CC.place(relx=0.5, rely=0.88, anchor="center") #Parte de la interfaz para crear cuenta

    def login(self): #Función para ingresar
        username = self.username_var.get() #Guardar variable username
        password = self.password_var.get() #Guardar variable contraseña
        if self.check.get() == False: #Verificar si la opción es crear cuenta o iniciar sesión
            self.call = user.sin_registro(self, username, password) #Dirige a la función "sin_registro" si se presiona el boton crear cuenta
        else:
            self.call = user.con_registro(self) #Dirige a la función "con_registro" si se presiona el bton inicar sesión
              
    def set_up(self): #Función para crear cuenta
        crear_cuenta = tk.Toplevel(self.root) #Metodo de tkinter para llamar clases
        set_up(crear_cuenta, self) #Dirije a la clase crear cuenta
    
class set_up(LoginApp): #Clase crear cuenta
    
    def __init__(self, root, crear_cuenta): #Constructor
        super().__init__(root) #Hereda los atributos de LoginApp
        self.root = root #Parte de la interfaz tkinter
        self.crear_cuenta = crear_cuenta #Parte de la interfaz de tkinter 
        self.root.title("Crear cuenta") #Parte de la interfaz como titulo de la pagina
        self.label.destroy() #Elimina partes del heredero
        tk.Label(root, text="Crear cuenta").place(relx=0.5, rely=0.1, anchor="center") #Parte de la interfaz como titulo de la pagina
        self.check.set(True) #Variable para denotar registro de una cuenta
        self.CC.destroy() #Elimina partes del heredero
        
class user: #Clase de verificación de usuario
    
    def sin_registro(self, username, password): #Función si no hay registro
        
        if username == "usuario" and password == "contraseña": #Validar usuario y contraseña
            messagebox.showinfo("Inicio de Sesión", "Inicio de sesión exitoso") #Mensaje de succesful
        else:
            messagebox.showerror("Error", "Credenciales incorrectas") #Mensaje de error
   
    def con_registro(self): #Función si hay registro
            messagebox.showinfo("Inicio de Sesión", "Inicio de sesión exitoso") #Mensaje de succesful
        
if __name__ == "__main__": #Parte para iniciar la interfaz
    root = tk.Tk() #Parte para iniciar la interfaz con tkinter
    app = LoginApp(root) #Parte para iniciar la inter con la pagina inicial
    root.mainloop() #Parte para permanecer la interfaz abierta
