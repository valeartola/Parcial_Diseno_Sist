# services/dna_service.py

from repositories.dna_repository import save_dna_record

def is_mutant(dna: list) -> bool:
    """
    Determina si una secuencia de ADN corresponde a un mutante.
    Un humano es considerado mutante si se encuentran más de una secuencia
    de cuatro letras idénticas consecutivas en cualquier dirección (horizontal, vertical, diagonal).
    """
    size = len(dna)
    sequences_to_find = 2  # Se necesitan al menos dos secuencias para determinar mutante
    found_sequences = 0
    
    # Función para verificar una secuencia en una dirección específica
    def check_sequence(i, j, direction):
        """Verifica si hay cuatro letras idénticas en la dirección dada."""
        letter = dna[i][j]
        for step in range(1, 4):
            new_i = i + step * direction[0]
            new_j = j + step * direction[1]
            # Verificar si estamos dentro de los límites y si la letra coincide
            if new_i >= size or new_j >= size or new_j < 0 or dna[new_i][new_j] != letter:
                return False
        return True

    # Direcciones: derecha, abajo, diagonal derecha, diagonal izquierda
    directions = [(0, 1), (1, 0), (1, 1), (1, -1)]

    # Iterar sobre cada posición de la matriz
    for i in range(size):
        for j in range(size):
            for direction in directions:
                if check_sequence(i, j, direction):
                    found_sequences += 1
                    # Si encontramos las secuencias necesarias, es mutante
                    if found_sequences >= sequences_to_find:
                        # Guardar el ADN en la base de datos como mutante y retornar True
                        dna_sequence = "".join(dna)
                        save_dna_record(dna_sequence, is_mutant=True)
                        return True
                    # Si encontramos una secuencia, no buscamos más en la misma posición
                    break  # Evita contar secuencias superpuestas en otras direcciones

    # Guardar el ADN en la base de datos como no mutante y retornar False
    dna_sequence = "".join(dna)
    save_dna_record(dna_sequence, is_mutant=False)
    return False
