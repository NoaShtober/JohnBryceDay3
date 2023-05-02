from University.Person import person


class lecturer(person):

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_mame = last_name

    def get_salary(selfself, salary, tax):
        final_salary = salary * (100-tax) / 100
        return final_salary
