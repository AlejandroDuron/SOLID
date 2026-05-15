from abc import ABC, abstractmethod

class Boleto(ABC):
    def __init__(self, pelicula, nombre):
        self.pelicula = pelicula
        self.nombre = nombre

    @abstractmethod
    def calcular_precio(self):
        pass
    
    
class BoletoGeneral(Boleto):
    precioBase = 5.00

    def calcular_precio(self):
        return self.precioBase
    

class BoletoVIP(Boleto):
    def calcular_precio(self):
        return BoletoGeneral.precioBase * 2  
    

class BoletoEstudiante(Boleto):
    Descuento = 0.20

    def calcular_precio(self):
        return BoletoGeneral.precioBase * (1 - self.Descuento)  
    
#--------------------------------------------------

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
    
class calcularTotal():
    def calcular_total(self, boleto, cantidad):
        return boleto.calcular_precio() * cantidad
         
class TicketCheckout(calcularTotal):
    def imprimirBoleto(self, boleto, cantidad, metodo_pago):
        precio = self.calcular_total(boleto, cantidad)
        nombre = boleto.nombre
        pago_info = metodo_pago.pagar(precio, nombre)
        
        return f""
        

        
    

# pruebas

boleto1 = BoletoGeneral("Dune")
boleto2 = BoletoVIP("La Cenicienta")
boleto3 = BoletoEstudiante("Zootopia 2")
boleto4 = BoletoGeneral("RIO 1")
reserva = ReservaCine()

reserva.agregar_boleto(boleto1)
reserva.agregar_boleto(boleto2)
reserva.agregar_boleto(boleto3)
reserva.agregar_boleto(boleto4)
reserva.agregar_boleto(boleto3)



metodo_pago = pagoTarjeta()
reserva.mostrar_resumen(metodo_pago)