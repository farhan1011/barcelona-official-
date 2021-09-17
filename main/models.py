from django.db import models

# Create your models here.
class Players(models.Model):
    def __str__(self):
        return self.pl_name

    pl_name=models.CharField(max_length=50)
    pl_age=models.IntegerField()
    pl_number=models.IntegerField()
    pl_image=models.CharField(max_length=2000,default="https://www.slntechnologies.com/wp-content/uploads/2017/08/ef3-placeholder-image.jpg")
    pl_position=models.CharField(max_length=25,default='cam')

class Legends(models.Model):


    leg_name=models.CharField(max_length=100)
    leg_age=models.IntegerField()
    leg_image=models.CharField(max_length=1000,default=".....")
    leg_play=models.CharField(max_length=100)

class Womens(models.Model):


    name=models.CharField(max_length=200)
    age=models.IntegerField()
    image=models.CharField(max_length=2000)
    position=models.CharField(max_length=20)

