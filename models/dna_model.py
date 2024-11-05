# models/dna_model.py
class DNARecord:
    """Clase que representa un registro de ADN."""
    def __init__(self, dna_sequence: str, is_mutant: bool):
        self.dna_sequence = dna_sequence
        self.is_mutant = is_mutant
