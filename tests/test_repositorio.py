import pytest
from repositories.repositorio import MutantRepository, ADNRecord


@pytest.fixture
def repository():
    repo = MutantRepository()
    repo.clear_database()  
    yield repo
    repo.clear_database()  
def test_save_dna_result(repository):
    dna = ["ATGCGA", "CAGTGC", "TTATGT", "AGAAGG", "CCCCTA", "TCACTG"]
    repository.save_dna_result(dna, True)
    assert len(repository.db.query(ADNRecord).all()) == 1  


def test_get_statistics(repository):
    dna_mutant = ["ATGCGA", "CAGTGC", "TTATGT", "AGAAGG", "CCCCTA", "TCACTG"]
    dna_human = ["ATGCGA", "CAGTGC", "TTATGT", "AGABGG", "CCGCTA", "TCACTG"]
    
    repository.save_dna_result(dna_mutant, True)
    repository.save_dna_result(dna_human, False)
    
    stats = repository.get_statistics()
    assert stats["count_mutant_dna"] == 1
    assert stats["count_human_dna"] == 1
    assert stats["ratio"] == 1.0
