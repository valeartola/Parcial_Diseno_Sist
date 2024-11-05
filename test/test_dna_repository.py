# test/test_dna_repository.py

import unittest
import os
from repositories.dna_repository import save_dna_record, get_dna_record, count_dna_records
from database.db_connection import get_db_connection

class TestDNARepository(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Configura una base de datos temporal para pruebas
        cls.connection = get_db_connection()
        # Crear la tabla de pruebas si no existe
        with cls.connection:
            cls.connection.execute("""
                CREATE TABLE IF NOT EXISTS dna_records (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    dna_sequence TEXT UNIQUE,
                    is_mutant BOOLEAN
                )
            """)

    def setUp(self):
        # Limpiar la tabla antes de cada prueba para evitar registros duplicados
        with self.connection:
            self.connection.execute("DELETE FROM dna_records")

    def test_save_dna_record_new(self):
        # Prueba guardar un nuevo registro de ADN
        dna_sequence = "ATGCGA"
        is_mutant = True
        result = save_dna_record(dna_sequence, is_mutant)
        self.assertTrue(result, "El registro debería guardarse exitosamente")

    def test_save_dna_record_duplicate(self):
        # Prueba que un registro duplicado no se guarde
        dna_sequence = "ATGCGA"
        is_mutant = True
        # Guardar el registro por primera vez
        save_dna_record(dna_sequence, is_mutant)
        # Intentar guardarlo nuevamente
        result = save_dna_record(dna_sequence, is_mutant)
        self.assertFalse(result, "El registro duplicado no debería guardarse")

    def test_get_dna_record_existing(self):
        # Prueba obtener un registro existente
        dna_sequence = "ATGCGA"
        is_mutant = True
        save_dna_record(dna_sequence, is_mutant)
        record = get_dna_record(dna_sequence)
        self.assertIsNotNone(record, "El registro debería existir")
        self.assertEqual(record.dna_sequence, dna_sequence)
        self.assertEqual(record.is_mutant, is_mutant)

    def test_get_dna_record_nonexistent(self):
        # Prueba obtener un registro inexistente
        dna_sequence = "ATGCGA"
        record = get_dna_record(dna_sequence)
        self.assertIsNone(record, "El registro no debería existir")

    def test_count_dna_records(self):
        # Prueba contar los registros de ADN mutante y humano
        save_dna_record("ATGCGA", True)   # Mutante
        save_dna_record("CAGTGC", False)  # Humano
        save_dna_record("TTATGT", True)   # Mutante
        save_dna_record("AGAAGG", False)  # Humano
        mutant_count, human_count = count_dna_records()
        self.assertEqual(mutant_count, 2, "Debería haber 2 registros mutantes")
        self.assertEqual(human_count, 2, "Debería haber 2 registros humanos")

    @classmethod
    def tearDownClass(cls):
        # Cierra la conexión de la base de datos y elimina la base temporal
        cls.connection.close()
        if os.path.exists("dna_records.db"):
            os.remove("dna_records.db")  # Eliminar la base de datos temporal al finalizar los tests

if __name__ == "__main__":
    unittest.main()
