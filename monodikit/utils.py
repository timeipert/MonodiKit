class Leveler:
    def __init__(self, documentType):
        docTypeToLevel = {"Level1": 1, "Level2": 2, "Level3": 3}
        self.levels = docTypeToLevel[documentType]
        self.current_level = 0

    def next_level(self):
        if self.levels < self.current_level:
            self.current_level += 1
            return True
        else:
            return False

    @property
    def interdivision(self):
        if self.levels > self.current_level:
            return True
        else:
            return False