import unittest
import datetime
from apps.TemperaturasDB import BaseTemperaturas

# test que verifica el correcto funcionamiento de la clase BaseTemperaturas
# verifica que se guerden, devuelvan, eliminen y se obtengan las temperaturas correctamente
# ademas verifica que se obtengan las temperaturas maximas y minimas de un rango de fechas tanto correctas como incorrectas

class TestBaseTemperaturas(unittest.TestCase):
    def setUp(self):
        """Orden de complejidad: O(1)"""
        self.db = BaseTemperaturas()
        self.db.guardar_temperatura(20, datetime.date(2024, 6, 1))
        self.db.guardar_temperatura(25, datetime.date(2024, 6, 2))
        self.db.guardar_temperatura(15, datetime.date(2024, 6, 3))

    def test_devolver_temperatura(self):
        """Orden de complejidad: O(log n)"""
        self.assertEqual(self.db.devolver_temperatura(datetime.date(2024, 6, 1)), 20)
        self.assertEqual(self.db.devolver_temperatura(datetime.date(2024, 6, 2)), 25)
        self.assertEqual(self.db.devolver_temperatura(datetime.date(2024, 6, 3)), 15)
        with self.assertRaises(Exception):
            self.db.devolver_temperatura(datetime.date(2024, 6, 4))

    def test_max_temp_rango(self):
        """Orden de complejidad: O(log n) en el caso promedio y O(n) en el peor caso"""
        # Prueba el máximo en todo el rango
        self.assertEqual(self.db.max_temp_rango(datetime.date(2024, 6, 1), datetime.date(2024, 6, 3)), 25)
        # Prueba el máximo en un solo día
        self.assertEqual(self.db.max_temp_rango(datetime.date(2024, 6, 2), datetime.date(2024, 6, 2)), 25)
        # Prueba el máximo en el último día
        self.assertEqual(self.db.max_temp_rango(datetime.date(2024, 6, 3), datetime.date(2024, 6, 3)), 15)

    def test_max_temp_rango_fechas_invalidas(self):
        """Orden de complejidad: O(log n) en el caso promedio y O(n) en el peor caso"""
        with self.assertRaises(ValueError):
            self.db.max_temp_rango("2024-06-01", datetime.date(2024, 6, 3))
        with self.assertRaises(ValueError):
            self.db.max_temp_rango(datetime.date(2024, 6, 3), datetime.date(2024, 6, 1))

    def test_min_temp_rango(self):
        """Orden de complejidad: O(log n) en el caso promedio y O(n) en el peor caso"""
        self.assertEqual(self.db.min_temp_rango(datetime.date(2024, 6, 1), datetime.date(2024, 6, 3)), 15)
        self.assertEqual(self.db.min_temp_rango(datetime.date(2024, 6, 2), datetime.date(2024, 6, 3)), 15)
        self.assertEqual(self.db.min_temp_rango(datetime.date(2024, 6, 1), datetime.date(2024, 6, 2)), 20)

    def test_min_temp_rango_fechas_invalidas(self):
        """Orden de complejidad: O(log n) en el caso promedio y O(n) en el peor caso"""
        with self.assertRaises(ValueError):
            self.db.min_temp_rango("2024-06-01", datetime.date(2024, 6, 3))
        with self.assertRaises(ValueError):
            self.db.min_temp_rango(datetime.date(2024, 6, 3), datetime.date(2024, 6, 1))
    
    def test_temp_extremos_rango(self):
        """Orden de complejidad: O(log n) en el caso promedio y O(n) en el peor caso"""
        self.assertEqual(self.db.temp_extremos_rango(datetime.date(2024, 6, 1), datetime.date(2024, 6, 3)), (15, 25))
        self.assertEqual(self.db.temp_extremos_rango(datetime.date(2024, 6, 2), datetime.date(2024, 6, 2)), (25, 25))

    def test_devolver_temperaturas(self):
        """Orden de complejidad: O(n)"""
        esperado = [
            "01/06/2024: 20°C",
            "02/06/2024: 25°C",
            "03/06/2024: 15°C"
        ]
        self.assertEqual(self.db.devolver_temperaturas(datetime.date(2024, 6, 1), datetime.date(2024, 6, 3)), esperado)

    def test_borrar_temperatura(self):
        """Orden de complejidad: O(log n)"""
        self.db.borrar_temperatura(datetime.date(2024, 6, 2))
        with self.assertRaises(Exception):
            self.db.devolver_temperatura(datetime.date(2024, 6, 2))
        self.assertEqual(self.db.cantidad_muestras(), 2)

    def test_cantidad_muestras(self):
        """Orden de complejidad: O(1)"""
        self.assertEqual(self.db.cantidad_muestras(), 3)
        self.db.borrar_temperatura(datetime.date(2024, 6, 1))
        self.assertEqual(self.db.cantidad_muestras(), 2)

    def test_str(self):
        """Orden de complejidad: O(n)"""
        s = str(self.db)
        self.assertIn("01/06/2024", s)
        self.assertIn("20°C", s)

 
if __name__ == "__main__":
    unittest.main()