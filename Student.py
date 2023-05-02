from University.Person import person


class student(person):
    def __init__(self, first_name, grade):
        self.first_name = first_name
        self.grade = grade

    def avg_calc(self, grade1, grade2):
        avg = (grade1 + grade2) /2
        print('Avg found value is =' + str(avg))
        return avg
