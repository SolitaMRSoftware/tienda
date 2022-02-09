from tkinter import *
from tkinter import messagebox
import sqlite3

#defino conexion a la base de datos
conexion=sqlite3.connect('mi tienda.db')

ventana = Tk()
ventana.geometry("1000x600") 
ventana.title("Tienda")
ventana.config(bg="bisque2")
ventana.state('zoomed')   

global tipoIndum

#imagen de fondo
IMG1=PhotoImage(file="E:\SOL\proyectosTerminados\PROYECTO FINAL/img/fondo.png")
label1=Label(ventana,image=IMG1)
label1.place(x=0,y=0,relwidth=1,relheight=1)






                 ###VALIDACIÓN DE DATOS VACIOS O INCORRECTOS

def validacionTexto(palabra):
        val=True
        for elemento in palabra:
                if(ord (elemento) < 64 or ord(elemento) > 122):
                        if(ord (elemento) != 32):
                                if(ord( elemento)!= 44):
                                        if(ord(elemento)!=64):
                                                val=False
                                                break
        return val

def validacionNum(numero):
        val=True
        for elemento in numero:
                if(ord(elemento) < 48 or ord(elemento) > 57 ):
                         if(ord (elemento) != 32):
                                if( ord(elemento) !=44):
                                        if(ord(elemento)!=46):
                                                if(ord(elemento)!=37):
                                                         if(ord(elemento)!=99):
                                                                 if(ord(elemento)!=45):
                                                                         if(ord (elemento) !=47):
                                                                                val=False
                                                                                break
        return val
        

def home():
    frameRemeras.place_forget()
    framePantalones.pack_forget()
    frameBlusas.pack_forget()
    frameVestidos.pack_forget()
    frameIndumentaria.pack_forget()
    frameClientes.pack_forget()
    frameVentas.pack_forget()
    frameProveedores.pack_forget()

    
def clientes():
    frameRemeras.place_forget()
    framePantalones.pack_forget()
    frameBlusas.pack_forget()
    frameVestidos.pack_forget()
    frameIndumentaria.pack_forget()
    frameVentas.pack_forget()
    frameProveedores.pack_forget()
    frameClientes.pack(expand=1,fill="x",padx=251)
    
def indumentaria():
    frameRemeras.pack_forget()
    framePantalones.pack_forget()
    frameBlusas.pack_forget()
    frameVestidos.pack_forget()
    frameClientes.pack_forget()
    frameVentas.pack_forget()
    frameProveedores.pack_forget()
    frameIndumentaria.pack(expand=1,fill="x",padx=251)

def ventas():
    frameRemeras.place_forget()
    framePantalones.pack_forget()
    frameBlusas.pack_forget()
    frameVestidos.pack_forget()
    frameClientes.pack_forget()
    frameIndumentaria.pack_forget()
    frameProveedores.pack_forget()
    frameVentas.pack(expand=1,fill="x",padx=251)
    
def proveedores():
    frameRemeras.place_forget()
    framePantalones.pack_forget()
    frameBlusas.pack_forget()
    frameVestidos.pack_forget()
    frameClientes.pack_forget()
    frameIndumentaria.pack_forget()
    frameVentas.pack_forget()
    frameProveedores.pack(expand=1,fill="x",padx=251)

    
#botones del MENÚ

boton1= Button(ventana,width=13,text="Home",bd=3,font=("poor richard",18),bg="#E91E63",command=home)
boton1.place(x=25,y=150)

boton2= Button(ventana,width=13,text="Clientes",bd=3,font=("poor richard",18),bg="#E91E63",command=clientes)
boton2.place(x=25,y=310)

boton3= Button(ventana,text="Indumentaria",width=13,bd=3,font=("poor richard",18),bg="#E91E63",command=indumentaria)
boton3.place(x=25,y=230)

boton4= Button(ventana,text="Ventas",width=13,bd=3,font=("poor richard",18),bg= "#E91E63",command=ventas)
boton4.place(x=25,y=390)

boton5= Button(ventana,text="Proveedores",width=13,bd=3,font=("poor richard",18),bg="#E91E63",command=proveedores)
boton5.place(x=25,y=470)

#frame del menu

frameClientes = Frame(ventana,width=900,height=800, bg="#FEDC3D")
frameIndumentaria =Frame(ventana,width=900,height=800,bg="#FEDC3D")
frameVentas = Frame(ventana,width=900,height=800, bg="#FEDC3D")
frameProveedores = Frame(ventana,width=900,height=800, bg="#FEDC3D")

#FRAME DE ROPA

frameRemeras = Frame(ventana,width=500,height=1000, bg="#FEDC3D")
frameVestidos = Frame(ventana,width=500,height=1000, bg="#FEDC3D")
frameBlusas = Frame(ventana,width=500,height=1000, bg="#FEDC3D")
framePantalones = Frame(ventana,width=500,height=1000, bg="#FEDC3D")


##FUNCION LISTADO

ventana.geometry('300x300')


listaArticulo=Listbox(frameIndumentaria,width=30,font=("segoe script",12))
listaArticulo.place(x=470,y=150)
     
#botones del frame de ropa

def vestidos():
    
    frameClientes.pack_forget()
    frameRemeras.place(x=1065,y=0)
    labelIndumentaria.config(text= "Vestidos",bg="#FEDC3D",font=("segoe script",20))
    global tipoIndum
    tipoIndum = "vestidos"
    
btnVestidos=Button(frameIndumentaria,command=vestidos,height=6,width=10,text="VESTIDOS",font=("segoe script",12),bg="#01ABAA",fg="#FFFFFF",bd=2)
btnVestidos.place(x=130,y=165)

def remeras():
   
    frameClientes.pack_forget()    
    frameRemeras.place(x=1065,y=0)
    labelIndumentaria.config(text= "Remeras", bg="#FEDC3D",font=("segoe script",20))
    global tipoIndum
    tipoIndum = "remeras"
    
btnRemeras=Button(frameIndumentaria,command=remeras,height=6,width=10,text="REMERAS",font=("segoe script",12),bg="#01ABAA",fg="#FFFFFF",bd=2)
btnRemeras.place(x=300,y=165)

def blusas():
    frameClientes.pack_forget()
    frameRemeras.place(x=1065,y=0)
    labelIndumentaria.config(text="Blusas", bg="#FEDC3D",font=("segoe script",20))
    global tipoIndum
    tipoIndum = "blusas"
    
btnBlusas=Button(frameIndumentaria,command=blusas,height=6,width=10,text="BLUSAS",font=("segoe script",12),bg="RoyalBlue3",fg="#FFFFFF",bd=2)
btnBlusas.place(x=130,y=355)

def pantalones():

    frameClientes.pack_forget()
    frameRemeras.place(x=1065,y=0)
    labelIndumentaria.config(text="Pantalones", bg="#FEDC3D",font=("segoe script",20))
    global tipoIndum
    tipoIndum = "pantalones"
    
    
btnPantalones=Button(frameIndumentaria,command=pantalones,height=6,width=10,text="PANTALONES",font=("segoe script",12),bg="RoyalBlue3",fg="#FFFFFF",bd=2)
btnPantalones.place(x=300,y=355)


labelIndumentaria1= Label(frameIndumentaria,text="Indumentaria",font=("segoe script",40),bg= "#FEDC3D")
labelIndumentaria1.place(x=320,y=30)


##label de indumentaria

labelIndumentaria = Label(frameRemeras,text="Indumentaria",font=("segoe script",12),bg= "#FEDC3D")
labelIndumentaria.place(x=90,y=0)

labelCódigo = Label(frameRemeras,text="Código",font=("segoe script",12),bg= "#FEDC3D")
labelCódigo.place(x=70,y=80)

labelDescripción = Label(frameRemeras,text="Descripción",font=("segoe script",12),bg= "#FEDC3D")
labelDescripción.place(x=70,y=150)

labelPrecio = Label(frameRemeras,text="Precio",font=("segoe script",12),bg= "#FEDC3D")
labelPrecio.place(x=70,y=220)

##entry de indumentaria

código=Entry(frameRemeras,font=("calibri",13),bd=2)
código.place(x=30,y=110)

descripción=Entry(frameRemeras,font=("calibri",13),bd=2)
descripción.place(x=30,y=180)

precio=Entry(frameRemeras,font=("calibri",13),bd=2)
precio.place(x=30,y=250)


#creo botones

def busquedaInd():
    
    global tipoIndum
    if(tipoIndum=="vestidos"):
        buscarCódigo=(código.get(),)
        tabla=conexion.cursor()
        tabla.execute("SELECT * FROM vestidos WHERE código = ?", buscarCódigo)
        conexion.commit()
        datos=tabla.fetchall()
        tabla.close
        if (len (datos)>0):
            messagebox.showinfo("Vestidos", "Vestido encontrado")
            for dato in datos:
                    código.delete(0,END)
                    código.insert(END,dato[0])
                    descripción.delete(0,END)
                    descripción.insert(END,dato[1])
                    precio.delete(0,END)
                    precio.insert(END,dato[2])
        else:
                    messagebox.showwarning("Vestidos", "Vestido no encontrado")
    
    if(tipoIndum=="remeras"):
        buscarCódigo=(código.get(),)
        tabla=conexion.cursor()
        tabla.execute("SELECT * FROM remeras WHERE código = ?", buscarCódigo)
        conexion.commit()
        datos=tabla.fetchall()
        tabla.close
        if (len (datos)>0):
            messagebox.showinfo("Remeras", "Remera encontrada")
            for dato in datos:
                    código.delete(0,END)
                    código.insert(END,dato[0])
                    descripción.delete(0,END)
                    descripción.insert(END,dato[1])
                    precio.delete(0,END)
                    precio.insert(END,dato[2])
        else:
                    messagebox.showwarning("Remeras", "Remera no encontrada")
    
            
    if(tipoIndum=="blusas"):
        buscarCódigo=(código.get(),)
        tabla=conexion.cursor()
        tabla.execute("SELECT * FROM blusas WHERE código = ?", buscarCódigo)
        conexion.commit()
        datos=tabla.fetchall()
        tabla.close
        if (len (datos)>0):
            messagebox.showinfo("Blusas", "Blusa encontrada")
            for dato in datos:
                    código.delete(0,END)
                    código.insert(END,dato[0])
                    descripción.delete(0,END)
                    descripción.insert(END,dato[1])
                    precio.delete(0,END)
                    precio.insert(END,dato[2])
        else:
                messagebox.showwarning("Blusas", "Blusa no encontrada")
            
            
    if(tipoIndum=="pantalones"):
        buscarCódigo=(código.get(),)
        tabla=conexion.cursor()
        tabla.execute("SELECT * FROM pantalones WHERE código = ?", buscarCódigo)
        conexion.commit()
        datos=tabla.fetchall()
        tabla.close
        if (len (datos)>0):
            messagebox.showinfo("Pantalones", "Pantalón encontrado")
            for dato in datos:
                    código.delete(0,END)
                    código.insert(END,dato[0])
                    descripción.delete(0,END)
                    descripción.insert(END,dato[1])
                    precio.delete(0,END)
                    precio.insert(END,dato[2])
        else:
                messagebox.showwarning("Pantalones", "Pantalón no encontrado")
         
botonBuscar=Button(frameRemeras,width=15,text="Buscar",font=("segoe script",12),bg="#FEA680",bd=2,command=busquedaInd)
botonBuscar.place(x=50,y=360)

     
def guardarInd():
    global tipoIndum
    if(tipoIndum=="vestidos"):    
        datos=(código.get(),descripción.get(),precio.get())
        tabla=conexion.cursor()
        tabla.execute("INSERT INTO vestidos(código,descripción,precio)VALUES(?,?,?)",datos)
        conexion.commit()
        tabla.close
        messagebox.showinfo("vestidos","Guardado exitoso")

    if(tipoIndum=="remeras"):
    
        datos=(código.get(),descripción.get(),precio.get())
        tabla=conexion.cursor()
        tabla.execute("INSERT INTO remeras(código,descripción,precio)VALUES(?,?,?)",datos)
        conexion.commit()
        tabla.close
        messagebox.showinfo("remeras","Guardado exitoso")
    
    if(tipoIndum=="blusas"):
    
        datos=(código.get(),descripción.get(),precio.get())
        tabla=conexion.cursor()
        tabla.execute("INSERT INTO blusas(código,descripción,precio)VALUES(?,?,?)",datos)
        conexion.commit()
        tabla.close
        messagebox.showinfo("blusas","Guardado exitoso")
    
    if(tipoIndum=="pantalones"):
    
        datos=(código.get(),descripción.get(),precio.get())
        tabla=conexion.cursor()
        tabla.execute("INSERT INTO pantalones(código,descripción,precio)VALUES(?,?,?)",datos)
        conexion.commit()
        tabla.close
        messagebox.showinfo("pantalones","Guardado exitoso")
    
    
botonGuardar=Button(frameRemeras,width=15,text="Guardar",font=("segoe script",12),bg="#FEA680",bd=2,command=guardarInd)
botonGuardar.place(x=50,y= 430)

def modificarInd():
    global tipoIndum
    if(tipoIndum=="vestidos"):
        datos=(descripción.get(), precio.get(),código.get())
        tabla=conexion.cursor()
        tabla.execute("UPDATE vestidos SET descripción=?,precio=? WHERE código=?",datos)
        conexion.commit()
        tabla.close
        messagebox.showinfo("Vestidos","Modificado exitoso")

    if(tipoIndum=="remeras"):
        datos=(descripción.get(), precio.get(), código.get())
        tabla=conexion.cursor()
        tabla.execute("UPDATE remeras SET descripción=?,precio=? WHERE código=?",datos)
        conexion.commit()
        tabla.close
        messagebox.showinfo("Remeras","Modificado exitoso")
    
    if(tipoIndum=="blusas"):
        datos=(descripción.get(), precio.get(), código.get())
        tabla=conexion.cursor()
        tabla.execute("UPDATE blusas SET descripción=?,precio=? WHERE código=?",datos)
        conexion.commit()
        tabla.close
        messagebox.showinfo("Blusas", "Modificado exitoso")
    
    if(tipoIndum=="pantalones"):
        datos=(descripción.get(), precio.get(), código.get())
        tabla=conexion.cursor()
        tabla.execute("UPDATE pantalones SET descripción=?,precio=? WHERE código=?",datos)
        conexion.commit()
        tabla.close
        messagebox.showinfo("Pantalones", "Modificado exitoso")


botonModificar=Button(frameRemeras,width=15,text="Modificar",font=("segoe script",12),bg="#FEA680",bd=2,command=modificarInd)
botonModificar.place(x=50, y=500)

def limpiarInd():
    descripción.delete(0,END)
    precio.delete(0,END)
    código.delete(0,END)
    

botonLimpiar=Button(frameRemeras,width=15,text="Clear",font=("segoe script",12),bg="#FEA680",bd=2,command=limpiarInd)
botonLimpiar.place(x=50,y=570)

def limpiarList():
    listaArticulo.delete(0,END)
    
botonLimpiar=Button(frameIndumentaria, width=16,text="Clear",font=("segoe script",12),bg="#FEA680",bd=2,command=limpiarList)
botonLimpiar.place(x=547,y=430)


def listarInd():

    if (código.get() == ""):
                messagebox.showwarning( "Indumentaria", "Primero busque una prenda")
    else:
                global tipoIndum
                if(tipoIndum=="vestidos"):
                    listarCódigo=(código.get(),)
                    tabla=conexion.cursor()
                    tabla.execute("SELECT * FROM vestidos ORDER BY  código= ?", listarCódigo)
                    conexion.commit()
                    datos=tabla.fetchall()
                    tabla.close
                    listaArticulo.delete(0,END)
                    for dato in datos:
                        articulo=str(dato[0])+ " "+ str(dato[1]) + " "+ str(dato[2])
                        listaArticulo.insert(0,articulo)
                        
                        
                if(tipoIndum=="remeras"):
                    listarCódigo=(código.get(),)
                    tabla=conexion.cursor()
                    tabla.execute("SELECT * FROM remeras ORDER BY  código= ?", listarCódigo)
                    conexion.commit()
                    datos=tabla.fetchall()
                    tabla.close
                    listaArticulo.delete(0,END)
                    for dato in datos:
                        articulo=str(dato[0])+ " "+ str(dato[1]) + " "+ str(dato[2])
                        listaArticulo.insert(0,articulo)

                if(tipoIndum=="blusas"):
                    listarCódigo=(código.get(),)
                    tabla=conexion.cursor()
                    tabla.execute("SELECT * FROM blusas ORDER BY  código= ?", listarCódigo)
                    conexion.commit()
                    datos=tabla.fetchall()
                    tabla.close
                    listaArticulo.delete(0,END)
                    for dato in datos:
                        articulo=str(dato[0])+ " "+ str(dato[1]) + " "+ str(dato[2])
                        listaArticulo.insert(0,articulo)

                if(tipoIndum=="pantalones"):
                    listarCódigo=(código.get(),)
                    tabla=conexion.cursor()
                    tabla.execute("SELECT * FROM pantalones ORDER BY  código= ?", listarCódigo)
                    conexion.commit()
                    datos=tabla.fetchall()
                    tabla.close
                    listaArticulo.delete(0,END) 
                    for dato in datos:
                        articulo=str(dato[0])+ " "+ str(dato[1]) + " "+ str(dato[2])
                        listaArticulo.insert(0,articulo)

                
            
botonListar=Button(frameIndumentaria, width=16,text=" Listar Indumentaria",font=("segoe script",12),bg="#FEA680",bd=2,command=listarInd)
botonListar.place(x=547,y=380)
    

###SECTOR CLIENTES

#creo entrada para campos

id=Entry(frameClientes,width=10,font=("calibri",14),bd=2)
id.place(x=280,y=150)
nombre=Entry(frameClientes,font=("calibri",14),bd=2)
nombre.place(x=280, y=200)
telefono=Entry(frameClientes,font=("calibri",14),bd=2)
telefono.place(x=280, y=250)
mail=Entry(frameClientes,font=("calibri",14),bd=2)
mail.place(x=280, y=300)

#creo label para campos

labelClientes=Label(frameClientes,text="Clientes",font=("segoe script",40),bg= "#FEDC3D")
labelClientes.place(x=320, y=30)

labelId=Label(frameClientes,text="Id",font=("segoe script",12),bg= "#FEDC3D")
labelId.place(x=200, y=150)
labelNombre=Label(frameClientes,text="Nombre",font=("segoe script",12),bg= "#FEDC3D")
labelNombre.place(x=200, y=200)
labelTelefono=Label(frameClientes,text="Teléfono",font=("segoe script",12),bg= "#FEDC3D")
labelTelefono.place(x=200, y=250)
labelMail=Label(frameClientes,text="Mail",font=("segoe script",12),bg= "#FEDC3D")
labelMail.place(x=200, y=300)


#creo botones del frame

#botones

def busqueda():
    buscarId=(id.get(),)
    tabla=conexion.cursor()
    tabla.execute("SELECT * FROM clientes WHERE id = ?", buscarId)
    conexion.commit()
    datos=tabla.fetchall()
    tabla.close
    if (len (datos)>0):
            messagebox.showinfo("Clientes", "Cliente encontrado")
            for dato in datos:
                id.delete(0,END)
                id.insert(END,dato[0])
                nombre.delete(0,END)
                nombre.insert(END,dato[1])
                telefono.delete(0,END)
                telefono.insert(END,dato[2])
                mail.delete(0,END)
                mail.insert(END,dato[3])
    else:
            messagebox.showwarning("Clientes", "Cliente no encontrado")
        

botonBuscar=Button(frameClientes,width=12,text="Buscar",font=("segoe script",12),bg="#FEA680",bd=2,command=busqueda)
botonBuscar.place(x=50,y=450)


def guardar():
    if (nombre.get() != "" and  telefono.get() !="" and mail.get() != "" ):
                if(validacionTexto(nombre.get())==False):
                        messagebox.showwarning ("Nombre ", "No es una letra")
                elif (validacionNum(telefono.get())==False):
                           messagebox.showwarning ("Teléfono", "No es un número")
                else:
                        messagebox.showinfo("Datos Correctos ", "Guardado Exitoso")
                        datos=(nombre.get(),telefono.get(),mail.get())
                        tabla=conexion.cursor()
                        tabla.execute("INSERT INTO clientes(nombre,telefono,mail)VALUES(?,?,?)",datos)
                        conexion.commit()
                        tabla.close
    else:
            messagebox.showwarning ("Clientes ","Datos Incompletos" )

                
botonGuardar=Button(frameClientes,width=12,text="Guardar",font=("segoe script",12),bg="#FEA680",bd=2,command=guardar)
botonGuardar.place(x=200,y=450)

def modificar():
      if (nombre.get() != "" and  telefono.get() !="" and mail.get() != "" ):
                if(validacionTexto(nombre.get())==False):
                        messagebox.showwarning ("Nombre ", "No es una letra")
                elif (validacionNum(telefono.get())==False):
                           messagebox.showwarning ("Teléfono", "No es un número")
                else:
                        messagebox.showinfo("Datos Correctos ", "Guardado Exitoso")
                        datos=(nombre.get(),telefono.get(), mail.get() ,id.get())
                        tabla=conexion.cursor()
                        tabla.execute("UPDATE clientes SET nombre=?,telefono=?,mail=? WHERE id=?",datos)
                        conexion.commit()
                        tabla.close
      else:
                messagebox.showwarning ("Clientes ","Datos Incompletos")
 

botonModificar=Button(frameClientes,width=12,text="Modificar",font=("segoe script",12),bg="#FEA680",bd=2,command=modificar)
botonModificar.place(x=350,y=450)

def eliminar():
     if (id.get()!="" ):
                messagebox.askquestion(  "Eliminar", "SEGURO DESEA ELIMINAR?")
     else:
            eliminarId=id.get()
            tabla=conexion.cursor()
            tabla.execute("DELETE FROM clientes WHERE id=?",eliminarId)
            conexion.commit()
            tabla.close
            messagebox.showinfo("Eliminación exitosa")
            
botonEliminar=Button(frameClientes,width=12,text="Eliminar",font=("segoe script",12),bg="#E91E63",bd=2,command=eliminar)
botonEliminar.place(x=650,y=450)

def limpiar():
    id.delete(0,END)
    nombre.delete(0,END)
    telefono.delete(0,END)
    mail.delete(0,END)
        
botonLimpiar=Button(frameClientes,width=12,text="Clear",font=("segoe script",12),bg="#FEA680",bd=2,command=limpiar)
botonLimpiar.place(x=500,y=450)

#####VENTAS


###LABEL DE VENTAS

labelVentas=Label(frameVentas,text="Ventas",font=("segoe script",40),bg= "#FEDC3D")
labelVentas.place(x=320, y=30)

labelNum=Label(frameVentas,text="Número de venta",font=("segoe script",14),bg= "#FEDC3D")
labelNum.place(x=10, y=130)

labelFecha=Label(frameVentas,text="Fecha",font=("segoe script",14),bg= "#FEDC3D")
labelFecha.place(x=10, y=180)

labelDesc=Label(frameVentas,text="Descripción",font=("segoe script",14),bg= "#FEDC3D")
labelDesc.place(x=10, y=230)

labelMonto=Label(frameVentas,text="Precio",font=("segoe script",14),bg= "#FEDC3D")
labelMonto.place(x=10, y=280)

labelPago=Label(frameVentas,text="Forma de Pago",font=("segoe script",14),bg= "#FEDC3D")
labelPago.place(x=10, y=330)


####ENTRY DE VENTAS

num=Entry(frameVentas,font=("calibri",13),bd=2)
num.place(x=190,y=130)

fecha=Entry(frameVentas,font=("calibri",13),bd=2)
fecha.place(x=190,y=180)

desc=Entry(frameVentas,font=("calibri",13),bd=2)
desc.place(x=190,y=230)

monto=Entry(frameVentas,font=("calibri",13),bd=2)
monto.place(x=190,y=280)

pago=Entry(frameVentas,font=("calibri",13),bd=2)
pago.place(x=190,y=330)


#### LISTA VENTAS

ventana.geometry('300x300')
ventana.config(bg="bisque2")


listaVentas=Listbox(frameVentas,width=30,font=("segoe script",12))
listaVentas.place(x=450,y=160)    
 


##BOTONES DE VENTAS

def busquedaVent():
    buscarId=(num.get(),)
    tabla=conexion.cursor()
    tabla.execute("SELECT * FROM ventas WHERE num = ?", buscarId)
    conexion.commit()
    datos=tabla.fetchall()
    tabla.close
    if (len (datos)>0):
            messagebox.showinfo("Ventas", "Venta encontrado")
            for dato in datos:
                num.delete(0,END)
                num.insert(END,dato[0])
                fecha.delete(0,END)
                fecha.insert(END,dato[1])
                desc.delete(0,END)
                desc.insert(END,dato[2])
                monto.delete(0,END)
                monto.insert(END,dato[3])
                pago.delete(0,END)
                pago.insert(END,dato[4])
    else:
            messagebox.showwarning("Ventas", "Venta no encontrada")

botonBuscarV=Button(frameVentas,width=12,text="Buscar",font=("segoe script",12),bg="#FEA680",bd=2,command=busquedaVent)
botonBuscarV.place(x=50,y=400)

def guardarVent():
    if (fecha.get() != "" and  desc.get() !="" and monto.get() != "" and pago.get() != "" ):
                if(validacionNum(fecha.get())==False):
                        messagebox.showwarning ("Fecha ", "No es un número")
                elif (validacionTexto(desc.get())==False):
                           messagebox.showwarning ("Descripción", "No es una letra")
                elif (validacionNum(monto.get())==False):
                           messagebox.showwarning ("Monto", "No es un número")
                elif (validacionTexto(desc.get())==False):
                           messagebox.showwarning ("Pago", "No es una letra")
                
                else:
                        messagebox.showinfo("Datos Correctos ", "Guardado Exitoso")
                        datos=(fecha.get(),desc.get(),monto.get(), pago.get())
                        tabla=conexion.cursor()
                        tabla.execute("INSERT INTO ventas(fecha, desc, monto, pago)VALUES(?,?,?,?)",datos)
                        conexion.commit()
                        tabla.close
    else:
                messagebox.showinfo("Ventas","Datos Incompletos ")
                
                        
botonGuardar=Button(frameVentas,width=12,text="Guardar",font=("segoe script",12),bg="#FEA680",bd=2,command=guardarVent)
botonGuardar.place(x=200, y=400)

def limpiarVent():
    num.delete(0, END)
    fecha.delete(0,END)
    desc.delete(0,END)
    monto.delete(0,END)
    pago.delete(0,END)
       
botonLimpiar=Button(frameVentas,width=12,text="Clear",font=("segoe script",12),bg="#FEA680",bd=2,command=limpiarVent)
botonLimpiar.place(x=50,y=470)


def modificarVent():
        if (fecha.get() != "" and  desc.get() !="" and monto.get() != "" and pago.get() != "" ):
                if(validacionNum(nombre.get())==False):
                        messagebox.showwarning ("Fecha ", "No es un número")
                elif (validacionTexto(desc.get())==False):
                           messagebox.showwarning ("Descripción", "No es una letra")
                elif (validacionNum(telefono.get())==False):
                           messagebox.showwarning ("Monto", "No es un número")
                elif (validacionNum(telefono.get())==False):
                           messagebox.showwarning ("Pago", "No es un número")
                else:
                        messagebox.showinfo("Datos Correctos ", "Guardado Exitoso")
                        datos=(fecha.get(),desc.get(), monto.get() ,pago.get(), num.get())
                        tabla=conexion.cursor()
                        tabla.execute("UPDATE ventas SET fecha=?,desc=?,monto=?, pago=? WHERE num=?",datos)
                        conexion.commit()
                        tabla.close
        else:
                messagebox.showwarning ("Ventas","Datos Incompletos")
 

botonModificar=Button(frameVentas,width=12,text="Modificar",font=("segoe script",12),bg="#FEA680",bd=2,command=modificarVent)
botonModificar.place(x=200,y=470)


def listarVent():
   
    listarFecha=(fecha.get(),)
    tabla=conexion.cursor()
    tabla.execute("SELECT * FROM ventas ORDER BY fecha = ?", listarFecha)
    conexion.commit()
    datos=tabla.fetchall()
    tabla.close
    listaVentas.delete(0,END)
    for dato in datos:
        ventas=str(dato[0])+ " "+str(dato[1])+ " "+ str(dato[2])+ " "+ str(dato[3])+" "+ str(dato[4])
        listaVentas.insert(0,ventas)
    
botonListar=Button(frameVentas,width=13,text="Listar Ventas",font=("segoe script",12),bg="#FEA680",bd=2,command=listarVent)
botonListar.place(x=550, y=410)

 
def limpiarLista():
    listaVentas.delete(0,END)
    
botonLimpiar=Button(frameVentas,width=13,text="Clear",font=("segoe script",12),bg="#FEA680",bd=2,command=limpiarLista)
botonLimpiar.place(x=550,y=470)


      
    
###PROVEEDORES


###LABEL DE PROVEEDORES

labelProveedores=Label(frameProveedores,text=" Proveedores",font=("segoe script",40),bg= "#FEDC3D")
labelProveedores.place(x=300, y=30)

labelClient=Label(frameProveedores,text="N° de Cliente",font=("segoe script",12),bg= "#FEDC3D")
labelClient.place(x=10, y=180)

labelRazon=Label(frameProveedores,text="Razón Social",font=("segoe script",12),bg= "#FEDC3D")
labelRazon.place(x=10, y=230)

labelCuit=Label(frameProveedores,text="CUIT",font=("segoe script",12),bg= "#FEDC3D")
labelCuit.place(x=10, y=280)

labelDomicilio=Label(frameProveedores,text="Domicilio",font=("segoe script",12),bg= "#FEDC3D")
labelDomicilio.place(x=10, y=330)

labelContacto=Label(frameProveedores,text="Contacto",font=("segoe script",12),bg= "#FEDC3D")
labelContacto.place(x=10, y=380)

###ENTRY DE PROVEEDORES

client=Entry(frameProveedores,font=("calibri",13),bd=2)
client.place(x=170,y=180)

razon=Entry(frameProveedores,font=("calibri",13),bd=2)
razon.place(x=170,y=230)

cuit=Entry(frameProveedores,font=("calibri",13),bd=2)
cuit.place(x=170,y=280)

domicilio=Entry(frameProveedores,font=("calibri",13),bd=2)
domicilio.place(x=170,y=330)

contacto=Entry(frameProveedores,font=("calibri",13),bd=2)
contacto.place(x=170,y=380)


###lista proveedores
ventana.geometry('300x300')
ventana.config(bg="fuchsia")


listaProv=Listbox(frameProveedores,width=30,font=("segoe script",12))
listaProv.place(x=435,y=160)    


####BOTONES DE PROVEEDORES

def busquedaP():
            buscarId=(client.get(),)
            tabla=conexion.cursor()
            tabla.execute("SELECT * FROM proveedores  WHERE client = ?", buscarId)
            conexion.commit()
            datos=tabla.fetchall()
            tabla.close
            if (len (datos)>0):
                    messagebox.showinfo("Proveedores", "Proveedor encontrado")
                    for dato in datos:
                        client.delete(0,END)
                        client.insert(END,dato[0])
                        razon.delete(0,END)
                        razon.insert(END,dato[1])
                        cuit.delete(0,END)
                        cuit.insert(END,dato[2])
                        domicilio.delete(0,END)
                        domicilio.insert(END,dato[3])
                        contacto.delete(0,END)
                        contacto.insert(END,dato[4])
            else:
                        messagebox.showwarning("Proveedores", "Proveedor no encontrado")


botonBuscarP=Button(frameProveedores,width=12,text="Buscar",font=("segoe script",12),bg="#FEA680",bd=2,command=busquedaP)
botonBuscarP.place(x=30,y=450)


def guardarProv():
         if (razon.get() != "" and  cuit.get() !="" and domicilio.get() != "" and contacto.get() != "" ):
                if(validacionTexto(nombre.get())==False):
                        messagebox.showwarning ("Razón ", "No es una letra")
                elif (validacionTexto(desc.get())==False):
                           messagebox.showwarning ("Cuit", "No es un número")
                else:
                        messagebox.showinfo("Datos Correctos ", "Modificado Exitoso")
                        datos=(razon.get(),cuit.get(),domicilio.get(), contacto.get())
                        tabla=conexion.cursor()
                        tabla.execute("INSERT INTO proveedores(razon, cuit, domicilio, contacto)VALUES(?,?,?,?)",datos)
                        conexion.commit()
                        tabla.close
         else:
                messagebox.showinfo("Datos Incompletos ")
                
                    
                    
botonGuardar=Button(frameProveedores,width=12,text="Guardar",font=("segoe script",12),bg="#FEA680",bd=2,command=guardarProv)
botonGuardar.place(x=180, y=450)

def modificarProv():
   if (razon.get() != "" and  cuit.get() !="" and domicilio.get() != "" and client.get() != "" ):
                if(validacionTexto(nombre.get())==False):
                        messagebox.showwarning ("Razón ", "No es una letra")
                elif (validacionNum(desc.get())==False):
                           messagebox.showwarning ("Cuit", "No es un número")
                else:
                        messagebox.showinfo("Datos Correctos ", "Modificado Exitoso")
                        datos=(razon.get(), cuit.get(), domicilio.get() , contacto.get (), client.get())
                        tabla=conexion.cursor()
                        tabla.execute("UPDATE proveedores SET razon=?, cuit=?, domicilio=? ,contacto=? WHERE client=?",datos)
                        conexion.commit()
                        tabla.close
   else:
        messagebox.showwarning ("Datos Incompletos")

botonModificar=Button(frameProveedores,width=12,text="Modificar",font=("segoe script",12),bg="#FEA680",bd=2,command=modificarProv)
botonModificar.place(x=30, y=500)

def limpiarProv():
    client.delete(0, END)
    razon.delete(0,END)
    cuit.delete(0,END)
    domicilio.delete(0,END)
    contacto.delete(0,END)
       
botonLimpiar=Button(frameProveedores,width=12,text="Clear",font=("segoe script",12),bg="#FEA680",bd=2,command=limpiarProv)
botonLimpiar.place(x=180,y=500)

def listarProv():
    listarClient=(client.get(),)
    tabla=conexion.cursor()
    tabla.execute("SELECT * FROM proveedores ORDER BY client = ?", listarClient)
    conexion.commit()
    datos=tabla.fetchall()
    tabla.close
    listaProv.delete(0,END)
    for dato in datos:
        proveedores=str(dato[0])+ " "+ str(dato[1]) + " "+ str(dato[2])+" "+str(dato[3])+" "+str(dato[4])
        listaProv.insert(0,proveedores)
        
botonListar=Button(frameProveedores,width=15,text="Listar Proveedores",font=("segoe script",12),bg="#FEA680",bd=2,command=listarProv)
botonListar.place(x=545, y=380)

def limpiarLista():
    listaProv.delete(0,END)
    
botonLimpiar=Button(frameProveedores,width=15,text="Clear",font=("segoe script",12),bg="#FEA680",bd=2,command=limpiarLista)
botonLimpiar.place(x=545,y=440)


def cerrarventana():
        ventana.destroy()

imgBotonSalir=PhotoImage(file="E:\SOL\proyectosTerminados\PROYECTO FINAL/img/salir.png")
btnSalir=Button(ventana,image=imgBotonSalir,command=cerrarventana,height=33,width=40).place(x=1232,y=630)
       

ventana.mainloop()


