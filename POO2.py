from abc import ABC, abstractmethod

# Boleto 

class Boleto(ABC):
    precioBase = 5.00

    @abstractmethod
    def calcular_precio(self):
        pass
    
    @abstractmethod
    def tipo(self):
        pass
    
class BoletoGeneral(Boleto):
    def calcular_precio(self):
        return self.precioBase
    
    def tipo(self):
        return "General"
    

class BoletoVIP(Boleto):
    def calcular_precio(self):
        return self.precioBase * 2
    
    def tipo(self):
        return "VIP"
    

class BoletoEstudiante(Boleto):
    Descuento = 0.20

    def calcular_precio(self):
        return self.precioBase * (1 - self.Descuento)  
    
    def tipo(self):
        return "Estudiante"
    
#--------------------------------------------------
# Clase para entidad

class Entidad(ABC):
    def __init__(self, nombre):
        self.nombre = nombre

class PersonaNatural(Entidad):
    def __init__(self, nombre):
        super().__init__(nombre)


#--------------------------------------------------
# Notidiaciones

# habia pensado que estas funciones podrian recibir el resumen, es decir la clase formate_datos para que de ahi saquen todos los datos que enecesitan

class Notificacion(ABC):
    @abstractmethod
    def enviar(self, resumen):
        pass

class notificacionEmail(Notificacion):
    def enviar(self, resumen):
        return f"[EMAIL] Confirmacion enviada a {resumen['nombre']} por ${resumen['total']:.2f}"

# Clase Repositorio
class Repositorio(ABC):
    @abstractmethod
    def guardar(self, resumen):
        pass

class registroDB(Repositorio):
    def guardar(self, resumen):
        return f"[DB] {resumen['nombre']} | {resumen['tipo']} x{resumen['cantidad']} = ${resumen['total']:.2f}"

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
    
class Formateable(ABC):
    
    @abstractmethod
    def formateo_datos(self, boleto, cantidad, comprador, metodo_pago):
        pass
         
class Datos(Formateable):
    def __init__(self, calculadora):
        self.calculadora = calculadora
        
    def formateo_datos(self, boleto, cantidad, comprador, metodo_pago):
        precio = self.calculadora.calcular_total(boleto, cantidad)
        pago_info = metodo_pago.pagar(precio, comprador.nombre)
        
        return {
            "tipo": boleto.tipo(),
            "cantidad": cantidad,
            "nombre": comprador.nombre,
            "total": precio,
            "pago_info": pago_info
        }

#--------------------------------------------------
## Funcion impresora de resultado

class Imprimible(ABC):
    
    @abstractmethod
    def imprimir_datos(self, resumen):
        pass

class TicketCheckout(Imprimible):
    def __init__(self, repositorio, notificacion):
        self.repositorio = repositorio
        self.notificacion = notificacion

    def imprimir_datos(self, resumen):
        print(f"{resumen['tipo']} x{resumen['cantidad']} -- {resumen['nombre']}")
        print(resumen['pago_info'])
        print(self.repositorio.guardar(resumen))
        print(self.notificacion.enviar(resumen))
        print(f"Total: ${resumen['total']:.2f}")
        print()

#--------------------------------------------------
# pruebas

calculadora = CalcularTotal()
datos       = Datos(calculadora)
db          = registroDB()
email       = notificacionEmail()
ticket      = TicketCheckout(db, email)

# Ana Garcia
boleto1    = BoletoVIP()
comprador1 = PersonaNatural("Ana Garcia")
metodo1    = pagoTarjeta()
resumen1   = datos.formateo_datos(boleto1, 2, comprador1, metodo1)
ticket.imprimir_datos(resumen1)

# Luis Perez
boleto2    = BoletoEstudiante()
comprador2 = PersonaNatural("Luis Perez")
metodo2    = pagoEfectivo()
resumen2   = datos.formateo_datos(boleto2, 3, comprador2, metodo2)
ticket.imprimir_datos(resumen2)