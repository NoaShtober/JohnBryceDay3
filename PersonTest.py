from University.Person import person
from University.Student import student
from University.Driver import driver
from University.Lecturer import lecturer

student1 = student('John', 8)
student2 = student('Michael', 10)

driver1 = driver('Alex', 'Dor')
driver2 = driver('Moshe', 'Levi')

lecturer1 = lecturer('Lio', 'Messi')

student1.avg_calc(80, 90)
student2.avg_calc(90,70)
