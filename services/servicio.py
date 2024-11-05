from repositories.repositorio import MutantRepository

class MutantService:
    def __init__(self):
        self.repository = MutantRepository()

    def check_dna(self, dna):
        is_mutant = self.is_mutant(dna)
        self.repository.save_dna_result(dna, is_mutant)
        return is_mutant

    def is_mutant(self, dna):
        sequence_count = 0
        n = len(dna)

        def has_sequence(x, y, dx, dy):
            letter = dna[x][y]
            for i in range(1, 4):
                nx, ny = x + dx * i, y + dy * i
                if nx >= n or ny >= n or nx < 0 or ny < 0 or dna[nx][ny] != letter:
                    return False
            return True

        for x in range(n):
            for y in range(n):
                if (y + 3 < n and has_sequence(x, y, 0, 1)) or \
                   (x + 3 < n and has_sequence(x, y, 1, 0)) or \
                   (x + 3 < n and y + 3 < n and has_sequence(x, y, 1, 1)) or \
                   (x + 3 < n and y - 3 >= 0 and has_sequence(x, y, 1, -1)):
                    sequence_count += 1
                    if sequence_count > 1:
                        return True
        return False

    def get_statistics(self):
        return self.repository.get_statistics()
    