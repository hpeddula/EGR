from django.db import models

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=200)


    def __str__(self):
        return self.name


class User(models.Model):
    u_fname = models.CharField(max_length=30)
    u_lname = models.CharField(max_length=30)
    company = models.ForeignKey('Company',on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return '{} {} {}'.format(self.u_fname,self.u_lname,self.company)
