from models.dna_model import ADNRecord
from database.db_connection import SessionLocal
from sqlalchemy.exc import IntegrityError

class MutantRepository:
    def __init__(self):
        self.db = SessionLocal()

    def save_dna_result(self, dna, is_mutant):
        dna_string = ",".join(dna)
        record = ADNRecord(dna_sequence=dna_string, is_mutant=is_mutant)
        try:
            self.db.add(record)
            self.db.commit()
            print("ADN guardado exitosamente.")
        except IntegrityError:
            self.db.rollback()
            print("Error: La secuencia de ADN ya existe en la base de datos.")

    def get_statistics(self):
        mutant_count = self.db.query(ADNRecord).filter_by(is_mutant=True).count()
        human_count = self.db.query(ADNRecord).filter_by(is_mutant=False).count()
        ratio = mutant_count / human_count if human_count > 0 else 0
        return {"count_mutant_dna": mutant_count, "count_human_dna": human_count, "ratio": ratio}

    def clear_database(self):
        """Elimina todos los registros de la tabla adn_records."""
        self.db.query(ADNRecord).delete()
        self.db.commit()
