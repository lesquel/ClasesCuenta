from enum import Enum

class TipoCuenta(Enum):
    Corriente = "Corriente"
    Ahorro = "Ahorro"
class Cuenta:
    def __init__(self, cedula: int, titular: str, saldo: float, tipoCuenta: TipoCuenta, numeroCuenta: int): 
        self.__cedula = self.__validarInt(cedula)
        self.__titular = self.__validarString(titular)
        self.__saldo = self.__validarFloat(saldo)
        self.__tipoCuenta = tipoCuenta
        self.__numeroCuenta = self.__validarInt(numeroCuenta)
    
    # Métodos Públicos
    def depositar(self, cantidad: float):
        self.__saldo += self.__validarFloat(cantidad)

    def retirar(self, cantidad: float):
        cantidad_valida = self.__validarFloat(cantidad)
        self.__saldo -= self.__validarSaldo(self.__saldo, cantidad_valida)

    def mostrarSaldo(self):
        print(f"Saldo: {self.__saldo}")

    def mostrarInfo(self):
        print(f"Cédula: {self.__cedula}, Titular: {self.__titular}, Saldo: {self.__saldo}, Tipo de Cuenta: {self.__tipoCuenta.value}, Número de Cuenta: {self.__numeroCuenta}")

    # Métodos Privados
    def __validarFloat(self, valor: float):
        if isinstance(valor, (float, int)):  
            return float(valor)
        else:
            raise ValueError("El valor debe ser un número flotante válido.")

    def __validarInt(self, valor: int):
        if isinstance(valor, int):
            return valor
        else:
            raise ValueError("El valor debe ser un número entero.")

    def __validarSaldo(self, saldo: float, retiro: float):
        if retiro > saldo:
            raise ValueError("El retiro no puede ser mayor que el saldo disponible.")
        return retiro

    def __validarString(self, string: str):
        if isinstance(string, str) and all(c.isalpha() or c.isspace() for c in string):
            return string
        else:
            raise ValueError("El valor debe ser una cadena de caracteres que solo contenga letras y espacios.")

try:
    cuenta = Cuenta(cedula=123456789, titular="Juan Perez", saldo=1000, tipoCuenta=TipoCuenta.Corriente, numeroCuenta=123456)
    cuenta.mostrarInfo()
    cuenta.depositar(cantidad=100)
    cuenta.depositar(cantidad=100)
    cuenta.mostrarSaldo()
    cuenta.retirar(cantidad=50)
    cuenta.mostrarSaldo()
    cuenta.mostrarInfo()
except ValueError as e:
    print(e)
