class ProgrammingLanguage:
    def __init__(self, name="", typing="", reflection=False, year=0):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        if self.reflection:
            return True
        else:
            return False

    def __str__(self):
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, " \
               f"First appeared in {self.year}"
