import pytest
from services.servicio import MutantService

@pytest.fixture
def service():
    return MutantService()

def test_is_mutant_true(service):
    dna_mutante = ["ATGCGA", "CAGTGC", "TTATGT", "AGAAGG", "CCCCTA", "TCACTG"]
    assert service.check_dna(dna_mutante) is True

def test_is_mutant_false(service):
    dna_no_mutante = ["ATGCGA", "CAGTGC", "TTATGT", "AGABGG", "CCGCTA", "TCACTG"]
    assert service.check_dna(dna_no_mutante) is False
