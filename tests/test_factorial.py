import unittest
from src.factorial import factorial_iterativo, factorial_iterativo_while, factorial_recursivo, factorial_recursivo_ternario


class TestFactorial(unittest.TestCase):
    def test_factorial_iterativo(self):
        self.assertEqual(factorial_iterativo(5), 120)
        self.assertEqual(factorial_iterativo(0), 1)
        with self.assertRaises(ValueError):
            factorial_iterativo(-1)  # Debe lanzar ValueError

    def test_factorial_recursivo(self):
        self.assertEqual(factorial_recursivo(8), 40320)  # Como en tu ejemplo
        self.assertEqual(factorial_recursivo(1), 1)
        with self.assertRaises(ValueError):
            factorial_recursivo(-5)

    # Repite para las otras funciones...

numero = int(input(f"ingresa un numero: "))
print(f"Factorial iterativo estándar de {numero}: {factorial_iterativo(numero)}")
print(f"Factorial iterativo while de {numero}: {factorial_iterativo_while(numero)}")
print(f"Factorial recursivo estándar de {numero}: {factorial_recursivo(numero)}")
print(f"Factorial recursivo ternario de {numero}: {factorial_recursivo_ternario(numero)}")

# Probamos con 0
print(f"Factorial de 0: {factorial_recursivo_ternario(0)}")

# Probamos con negativo (debe lanzar excepción)
try:
    print(factorial_recursivo_ternario(-3))
except ValueError as e:
    print(f"Error correctamente capturado: {e}")

if __name__ == "__main__":
    unittest.main()