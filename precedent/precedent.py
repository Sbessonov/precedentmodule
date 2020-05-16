class Term:
    def __init__(self, value, membership_function):
        self._name = value
        self._membership_func = membership_function

    def get_value(self):
        pass

    def membership(self, number: float):
        return self._membership_func(number)


class LinguisticVariable:
    def __init__(self):
        self.name = ''
        self.terms = []

    def get_value(self, number: float):
        pass

    def get_terms(self):
        return self.terms


class SituationalVector:
    pass