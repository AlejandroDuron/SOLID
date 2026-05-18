from abc import ABC, abstractmethod

# Boleto 

class Boleto(ABC):
    def __init__(self, pelicula):
        self.pelicula = pelicula

    @abstractmethod
    def calcular_precio(self):
        pass
    
    @abstractmethod
    def tipo(self):
        pass
    
class BoletoGeneral(Boleto):
    precioBase = 5.00

    def calcular_precio(self):
        return self.precioBase
    
    def tipo(self):
        return "General"
    

class BoletoVIP(Boleto):
    def calcular_precio(self):
        return BoletoGeneral.precioBase * 2  
    
    def tipo(self):
        return "VIP"
    

class BoletoEstudiante(Boleto):
    Descuento = 0.20

    def calcular_precio(self):
        return BoletoGeneral.precioBase * (1 - self.Descuento)  
    
    def tipo(self):
        return "Estudiante"
    
#--------------------------------------------------
# Clase para entidad

class Entidad:
    def __init__(self, nombre):
        self.nombre = nombre
        
#--------------------------------------------------
# Notidiaciones

# habia pensado que estas funciones podrian recibir el resumen, es decir la clase formate_datos para que de ahi saquen todos los datos que enecesitan

class Notificacion():
    pass # falta

# Clase Repositorio
class Repositorio():
    pass # falta

#--------------------------------------------------
# Pagos

class pagable(ABC):
    @abstractmethod
    def pagar(self, monto, comprador):
        pass

class pagoEfectivo(pagable):
    def pagar(self, monto, comprador):
        return f"[EFECTIVO] Recibiendo ${monto:.2f} a {comprador}"
    
class pagoTarjeta(pagable):
    def pagar(self, monto, comprador):
        return f"[TARJETA] Cobrando ${monto:.2f} a {comprador}"
    
#--------------------------------------------------
# Formateo de datos
    
class CalcularTotal():
    def calcular_total(self, boleto, cantidad):
        return boleto.calcular_precio() * cantidad
         
class Datos():
    def __init__(self, calculadora):
        self.calculadora = calculadora
        
    def formateo_datos(self, boleto, cantidad, comprador, metodo_pago):
        precio = self.calculadora.calcular_total(boleto, cantidad)
        pago_info = metodo_pago.pagar(precio, comprador.nombre)
        
        return {
            "pelicula": boleto.pelicula,
            "cantidad": cantidad,
            "nombre": comprador.nombre,
            "total": precio,
            "pago_info": pago_info
        }

#--------------------------------------------------
## Funcion impresora de resultado

class TicketCheckout():
    def imprimir_datos(self):
        pass # falta

#--------------------------------------------------
# pruebas

calculadora = CalcularTotal()
datos       = Datos(calculadora)
db          = registroDB()
email       = notificacionEmail()
ticket      = TicketCheckout(db, email)

# Ana Garcia
boleto1    = BoletoVIP("Inception")
comprador1 = Entidad("Ana Garcia")
metodo1    = pagoTarjeta()
resumen1   = datos.formateo_datos(boleto1, 2, comprador1, metodo1)
ticket.imprimir_datos(resumen1)

# Luis Perez
boleto2    = BoletoEstudiante("Inception")
comprador2 = Entidad("Luis Perez")
metodo2    = pagoEfectivo()
resumen2   = datos.formateo_datos(boleto2, 3, comprador2, metodo2)
ticket.imprimir_datos(resumen2)