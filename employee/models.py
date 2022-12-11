from django.db import models
from datetime import date


class AbstractPerson(models.Model):
    name = models.CharField(max_length=20)
    birth_date = models.DateField()

    class Meta:
        abstract = True
        ordering = ['name', ]

    def get_age(self):
        date.today - self.birth_date

    def __str__(self):
        return self.name



class Employee(AbstractPerson):
    position = models.CharField(max_length=50)
    salary = models.IntegerField(null=True)
    work_experience = models.DateField(null=True)


    def __str__(self):
        return self.position


class Passport(models.Model):
    inn = models.CharField(max_length=16)
    id_card = models.CharField(max_length=7)
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE, related_name='passports')

    def get_gender(self):
        if '1' in self.inn[0]:
            return 'Female'
        elif '2' in self.inn[0]:
            return 'Male'

    def save(self, *args, **kwargs):
        print(f'ИНН-{self.inn} был успешно сохранен, ID CARD-{self.id_card} была успешно сохранена')
        super().save(*args, **kwargs)

    def __str__(self):
        return self.inn


class WorkProject(models.Model):
    employees = models.ManyToManyField(Employee, related_name='work_projects', through='Membership')
    project_name = models.CharField(max_length=20)

    def save(self, *args, **kwargs):
        print(f'{self.employees}-{self.project_name}')

    def __str__(self):
        return self.project_name


class Membership(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    project = models.ForeignKey(WorkProject, on_delete=models.CASCADE)
    date_joined = models.DateField()

    def save(self, *args, **kwargs):
        print(f'{self.employee}-{self.prooject}')

    def __str__(self):
        return self.employee.name


class Client(AbstractPerson):
    address = models.CharField(max_length=20)
    phone_number = models.IntegerField()

    def __str__(self):
        return self.address


class VIPClient(Client):
    vip_status_start = models.DateField(null=True)
    donation_amount = models.IntegerField(null=True)

    def __str__(self):
        return self.vip_status_start