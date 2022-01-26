from email import message
import smtplib
import tkinter

#Ventana
ventana = tkinter.Tk()
ventana.geometry("500x500")
ventana.title("Enviar Mensajes")
ventana.resizable(False, False)

#Etiquetas
etiqueta1 = tkinter.Label(ventana, text = "GitHub - ForeverAnimado", bg= "blue")
etiqueta1.pack(side= tkinter.BOTTOM, fill = tkinter.X)
etiqueta2 = tkinter.Label(ventana, text = "Hola bienvenido a mi programa para enviar correos electronicos", bg= "blue")
etiqueta2.pack(fill = tkinter.X)

#Entry's
mensaje = tkinter.Label(text="¿Cual es el mensaje que queres mandar?")
mensaje.pack()
cajademensaje = tkinter.Entry(ventana, font = "Helvetica 20")
cajademensaje.pack()

correo = tkinter.Label(text="¿Cual es la persona que se lo queres mandar?")
correo.pack()
cajadecorreo = tkinter.Entry(ventana, font = "Helvetica 20")
cajadecorreo.pack(padx=20, pady=20)

tucorreo = tkinter.Label(text="¿Cual es tu correo?")
tucorreo.pack()
cajadetucorreo = tkinter.Entry(ventana, font = "Helvetica 20")
cajadetucorreo.pack(padx=20, pady=20)

contraseña = tkinter.Label(text="¿Cual la contraseña de tu correo?")
contraseña.pack()
cajadetucontraseña = tkinter.Entry(ventana, font = "Helvetica 20")
cajadetucontraseña.pack(padx=20, pady=20)
cajadetucontraseña.config(show="*")
    
#Comando
def enviarcorreo():
        textomensaje = cajademensaje.get()
        textodecorreo = cajadecorreo.get()
        textodetucorreo = cajadetucorreo.get()
        textodetucontraseña = cajadetucontraseña.get()

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(textodetucorreo, textodetucontraseña)

        server.sendmail(textodetucorreo, textodecorreo, textomensaje)

        server.quit()

#Boton
Boton1 = tkinter.Button(ventana,padx="40", pady="10", text = "Enviar", command = enviarcorreo)
Boton1.pack()

print("Correo enviado")

ventana.mainloop()
