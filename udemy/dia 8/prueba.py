import unittest
import cambia_texto

class TestCambiaTexto(unittest.TestCase):
    def test_todo_mayusculas(self):
        self.assertEqual(cambia_texto.todo_mayusculas("hola mundo"), "HOLA MUNDO")
        self.assertEqual(cambia_texto.todo_mayusculas("Python"), "PYTHON")
        self.assertEqual(cambia_texto.todo_mayusculas(""), "")
        self.assertEqual(cambia_texto.todo_mayusculas("123"), "123")
        self.assertEqual(cambia_texto.todo_mayusculas("¡Hola!"), "¡HOLA!")


if __name__ == '__main__':
    unittest.main()
