import unittest
from src.fibonacci import fibonacci_iterativo, fibonacci_recursivo
#resolver fibonacci
class test_fibonacci(unittest.TestCase):
    def fibonacci_recursivo(self):
        self.assertEqual(fibonacci_recursivo(2))
        self.assertEqual(fibonacci_recursivo(0))
        with self.assertRaises(ValueError):
            fibonacci_recursivo(-1)
    
    def fibonacci_iterativo(self):
        self.assertEqual(fibonacci_iterativo(5))
        self.assertEqual(fibonacci_iterativo(10))
        with self.assertRaises(ValueError):
            fibonacci_iterativo(-5)
#fin fibonacci

if __name__ == "__main__":
    unittest.main()