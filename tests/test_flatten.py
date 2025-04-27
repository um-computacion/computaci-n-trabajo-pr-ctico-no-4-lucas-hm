import unittest
from src.flatten import list_flattener, SoloListasError
#resolver ejercicio listas
class TestAplanadorListas(unittest.TestCase):
    def test_lista_simple(self):
        self.assertEqual(list_flattener([1, 3.14, True, "hello"]), [1, 3.14, True, "hello"])
        self.assertEqual(list_flattener([]), [])
        self.assertEqual(list_flattener([False, "test", 42, 0.5]), [False, "test", 42, 0.5])
        self.assertEqual(list_flattener([-3, 0, 99.9, "", "Python"]), [-3, 0, 99.9, "", "Python"])
    def test_lista_anidada(self):
        self.assertEqual(list_flattener([1, [True, "nested"]]), [1, True, "nested"])
        self.assertEqual(list_flattener([["a", "b"], 3.14, [False, True]]), ["a", "b", 3.14, False, True])
        self.assertEqual(list_flattener([[]]), [])
        self.assertEqual(list_flattener([[1.1, 2.2], "middle", [True, [False, "deep", [0.1]]]]),[1.1, 2.2, "middle", True, False, "deep", 0.1])
    def test_elementos_invalidos(self):
        with self.assertRaises(SoloListasError):
            list_flattener([1, 2, (3, 4)])
        with self.assertRaises(SoloListasError):
            list_flattener([1, {'a': 2}, 3])
        with self.assertRaises(SoloListasError):
            list_flattener([1, [2, (3, 4)], 5])
        with self.assertRaises(SoloListasError):
            list_flattener([[1, 2],[{'a':3},4]])
#fin listas

if __name__ == "__main__":
    unittest.main()