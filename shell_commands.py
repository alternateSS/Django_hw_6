from employee.models import *
from django.db.models import Q, Subquery
#
# e1 = Employee.objects.create(name='Rustam', birth_date='2002-05-25', position='Director', salary=25000, work_experience='2018-05-05', inn='123456789123456', id_card='1234567')
e1 = Passport(employee=Employee.objects.create(name='Rustam', birth_date='2002-05-25', position='Python Backend Developer', salary=1000, work_experience='2022-12-09'), inn='2234567891234567', id_card='1234567')
e2 = Passport(employee=Employee.objects.create(name='Rashid', birth_date='2002-10-27', position='Java Backend Developer', salary=500, work_experience='2022-12-09'), inn='1234567891234598', id_card='1234567')
e3 = Passport(employee=Employee.objects.create(name='Nurlan', birth_date='1992-02-01', position='Javascript Frontend Developer', salary=1500, work_experience='2022-12-09'), inn='1234567891234599', id_card='1234567')
e4 = Passport(employee=Employee.objects.create(name='Ormon', birth_date='2002-01-03', position='PHP Backend Developer', salary=2000, work_experience='2022-12-09'), inn='1234567891234510', id_card='1234567')
# e1.save()
# e2.save()
# e3.save()
# e4.save()
# e1.get_gender()

t_persons = Employee.objects.filter(name__startswith='O')
not_employee = t_persons.exclude(name__in=['Ormon'])
print(t_persons)
print(not_employee)



