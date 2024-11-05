# database/db_connection.py
import sqlite3
from sqlite3 import Connection

def get_db_connection() -> Connection:
    """Establece y retorna la conexión a la base de datos."""
    connection = sqlite3.connect("dna_records.db")
    connection.row_factory = sqlite3.Row  # Permite acceder a las columnas por nombre
    return connection

def initialize_database():
    """Inicializa la base de datos creando las tablas necesarias."""
    connection = get_db_connection()
    with connection:
        connection.execute("""
            CREATE TABLE IF NOT EXISTS dna_records (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                dna_sequence TEXT UNIQUE,
                is_mutant BOOLEAN
            )
        """)
    connection.close()
