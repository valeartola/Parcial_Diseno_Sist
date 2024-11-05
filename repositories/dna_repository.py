# repositories/dna_repository.py
from database.db_connection import get_db_connection
from models.dna_model import DNARecord

def save_dna_record(dna_sequence: str, is_mutant: bool) -> bool:
    """Guarda un registro de ADN en la base de datos si no existe."""
    try:
        connection = get_db_connection()
        with connection:
            # Verificar si el ADN ya existe
            existing_record = connection.execute(
                "SELECT * FROM dna_records WHERE dna_sequence = ?",
                (dna_sequence,)
            ).fetchone()
            if existing_record:
                # El ADN ya existe, no se inserta de nuevo
                return False
            
            # Insertar el nuevo registro si no existe
            connection.execute(
                "INSERT INTO dna_records (dna_sequence, is_mutant) VALUES (?, ?)",
                (dna_sequence, is_mutant)
            )
        return True
    except Exception as e:
        print(f"Error al guardar el registro: {e}")
        return False

def get_dna_record(dna_sequence: str) -> DNARecord:
    """Obtiene un registro de ADN por su secuencia."""
    connection = get_db_connection()
    with connection:
        row = connection.execute(
            "SELECT * FROM dna_records WHERE dna_sequence = ?",
            (dna_sequence,)
        ).fetchone()
        if row:
            return DNARecord(dna_sequence=row["dna_sequence"], is_mutant=bool(row["is_mutant"]))
    return None

def count_dna_records() -> tuple:
    #Cuenta los registros de ADN mutante y humano.
    connection = get_db_connection()
    with connection:
        mutant_count = connection.execute(
            "SELECT COUNT(*) FROM dna_records WHERE is_mutant = 1"
        ).fetchone()[0]
        human_count = connection.execute(
            "SELECT COUNT(*) FROM dna_records WHERE is_mutant = 0"
        ).fetchone()[0]
    return mutant_count, human_count
