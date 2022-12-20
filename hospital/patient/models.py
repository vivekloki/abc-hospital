from django.db import models

# Create your models here.
class Department(models.Model):
    dpt_name=models.CharField(max_length=20)
    dpt_description=models.TextField(max_length=355)

    def __str__(self):
        return self.dpt_name
class Doctor(models.Model):
    doc_name=models.CharField(max_length=27)
    doc_spec=models.CharField(max_length=20)
    dpt_name=models.ForeignKey(Department,on_delete=models.CASCADE)
    doc_img=models.ImageField(upload_to='doctor')

    def __str__(self):
        return self.doc_name

class Booking(models.Model):
    p_name=models.CharField(max_length=255)
    p_phone=models.CharField(max_length=10)
    p_email=models.EmailField()
    doc_name=models.ForeignKey(Doctor,on_delete=models.CASCADE)
    dpt_name=models.ForeignKey(Department,on_delete=models.CASCADE)
    booking_date=models.DateField()
    booked_on=models.DateField(auto_now=True)

