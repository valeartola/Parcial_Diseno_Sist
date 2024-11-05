from sqlalchemy import Column, Integer, String, Boolean
from database.db_connection import Base

class ADNRecord(Base):
    __tablename__ = 'adn_records'

    id = Column(Integer, primary_key=True, autoincrement=True)
    dna_sequence = Column(String, unique=True, nullable=False)
    is_mutant = Column(Boolean, nullable=False)

    def __init__(self, dna_sequence, is_mutant):
        self.dna_sequence = dna_sequence
        self.is_mutant = is_mutant
