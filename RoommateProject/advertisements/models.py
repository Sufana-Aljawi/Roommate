from django.db import models

class Advertisement(models.Model):
    types_of_gender=models.TextChoices('types_of_gender',['Female','Male'])
    types_of_residential=models.TextChoices('types_of_residential',['Apartment','Room','House'])
    types_of_duration =models.TextChoices('types_of_duration',['Days','Weeks','Months'])
    title=models.CharField(max_length=500)
    image=models.ImageField(upload_to="images/")
    type_of_duration =models.CharField(max_length=500,choices=types_of_duration.choices)
    duration_residence=models.IntegerField()
    advertisement_date=models.DateTimeField(auto_now_add=True)
    type_of_residential=models.CharField(max_length=500,choices=types_of_residential.choices)
    longitude = models.DecimalField(max_digits=12, decimal_places=9)
    latitiiude=models.DecimalField(max_digits=12, decimal_places=9)
    space=models.FloatField()
    price=models.FloatField()
    number_of_people=models.IntegerField()
    features=models.TextField()
    animal_allowed=models.BooleanField()
    min_age=models.IntegerField()
    max_age=models.IntegerField()
    gender=models.CharField(max_length=500,choices=types_of_gender.choices)
    smoke_allowed=models.BooleanField()
    advertisement_status=models.BooleanField()
    note=models.TextField()
    rooms_number=models.IntegerField()
    bathroom=models.IntegerField()
    has_kitchen=models.BooleanField()
    approved_status=models.CharField(max_length=500,default='pending')

class Advertisement_Image(models.Model):
    advertisement=models.ForeignKey(Advertisement,on_delete=models.CASCADE)
    image=models.ImageField(upload_to="images/")











# Create your models here.
