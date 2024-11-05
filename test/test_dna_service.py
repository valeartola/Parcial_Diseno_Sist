# test/test_dna_service.py

import unittest
from services.dna_service import is_mutant

class TestDNAService(unittest.TestCase):
    def test_is_mutant_true(self):
        # Caso de prueba con ADN de un mutante
        dna = [
            "ATGCGA",
            "CAGTGC",
            "TTATGT",
            "AGAAGG",
            "CCCCTA",
            "TCACTG"
        ]
        self.assertTrue(is_mutant(dna), "El ADN debería ser mutante")

    def test_is_mutant_false(self):
        # Caso de prueba con ADN de un humano (no mutante)
        dna = [
            "ATGCGA",
            "CAGTAC",
            "TTAAGT",
            "AGGAGG",
            "CCGCTA",
            "TCACTG"
        ]
        self.assertFalse(is_mutant(dna), "El ADN no debería ser mutante")

    def test_is_mutant_edge_case(self):
        # Caso de prueba límite, donde el ADN es justo en el límite de no ser mutante
        dna = [
            "ATGCGA",
            "CAGTAC",
            "TTATGT",
            "AGAAGG",
            "CTGCTA",
            "TCACTG"
        ]
        self.assertFalse(is_mutant(dna), "Este ADN no debería ser mutante")

if __name__ == "__main__":
    unittest.main()
