

from django.db import models
from datetime import datetime
from django.core.validators import RegexValidator





# Create your models here.


class medicine(models.Model):
    medicinename=models.CharField(max_length=70)
    brandname=models.CharField(max_length=70)
    medicinequantity=models.IntegerField()
    medicineprice=models.IntegerField()
    time = models.DateField(auto_now_add=True )

    def __str__(self):
        return self.medicinename



class patient(models.Model):
    patient_firstname=models.CharField(max_length=70)
    patient_middlename=models.CharField(max_length=70 ,default='')
    patient_lastname=models.CharField(max_length=70,default='')
    patient_address=models.CharField(max_length=70)
    patient_mobileno=models.IntegerField()
    time = models.DateField(auto_now_add=True )

    def __str__(self):
        return self.patient_firstname









class receipt(models.Model):
    username=models.CharField(max_length=70)
    medicinename=models.CharField(max_length=70)
    medicinetiming=models.CharField(max_length=100)
    medicineprice=models.IntegerField()

    def __str__(self):
        return self.username



class receiptHistory(models.Model):
    username=models.CharField(max_length=70)
    medicinename=models.CharField(max_length=70)
    medicinetiming=models.CharField(max_length=100)
    medicineprice=models.IntegerField()
    time = models.DateField(auto_now_add=True)


class medicineoutside(models.Model):
    username = models.CharField(max_length=30, default="no user")
    ousidemedicinename=models.CharField(max_length=20)
    ousidemedicinetime=models.CharField(max_length=20)

    
    def __str__(self):
        return self.ousidemedicinename  


class medicineoutsideHistory(models.Model):
    username = models.CharField(max_length=30, default="no user")
    ousidemedicinename=models.CharField(max_length=20)
    ousidemedicinetime=models.CharField(max_length=20)
    time = models.DateField(auto_now_add=True)



class notes(models.Model):
    title=models.CharField(max_length=50)
    desc=models.TextField()
    time = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.title

class blooddonation(models.Model):
    patient_firstname=models.CharField(max_length=70,default="")
    patient_middlename=models.CharField(max_length=70,default="")
    patient_lastname=models.CharField(max_length=70,default="")
    address=models.CharField(max_length=70)
    blood_group=(
        ('O+','O+'),
        ('O-','O-'),
        ('A+','A+'),
        ('A-','A-'),
        ('B+','B+'),
        ('B-','B-'),
        ('AB+','AB+'),
        ('AB-','AB-'),
    )
    bloodgroup=models.CharField(max_length=10,choices=blood_group,default="O+")
    mobileno=models.IntegerField()
    # healthissue=models.CharField(max_length=100,null=True)
    time = models.DateField(auto_now_add=True)

    
    

    def __str__(self):
        return self.patientname


class doctorsdetails(models.Model):
    doctorname = models.CharField(max_length=70)
    address=models.CharField(max_length=100)
    mobileno=models.CharField(max_length=100)
    hospitaname=models.CharField(max_length=100)
    pincode=models.CharField(max_length=6,default="")

    
    def __str__(self):
        return self.doctorname
    


class criticalpatient(models.Model):
    patient_firstname=models.CharField(max_length=70)
    patient_middlename=models.CharField(max_length=70 ,default='')
    patient_lastname=models.CharField(max_length=70,default='')
    patient_address=models.CharField(max_length=70)
    patient_mobileno=models.IntegerField()
    prescribedoctorname=models.CharField(max_length=70)
    healthproblem=models.CharField(max_length=70)
    time = models.DateField(auto_now_add=True )

    def __str__(self):
        return self.patient_firstname
