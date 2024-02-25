class Employee:
    def __init__(self, name: str, unit: list, priority: bool = False):
        self.name = name
        self.unit = unit
        self.priority = priority

    def get_name(self):
        print(self.name)

    def get_unit(self):
        print(self.unit)
