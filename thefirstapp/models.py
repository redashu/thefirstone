from django.db import models

# Create your models here.

class Appnames(models.Model):
    is_played=models.DateTimeField(auto_now_add=True)
    app_name=models.CharField(max_length=255)
    app_type=models.TextField()

    def __str__(self):
        return(self.app_name)

class Howtouse(models.Model):
    step_title=models.CharField(max_length=255)
    step1=models.TextField()
    step2=models.TextField()
    step3=models.TextField()
    order=models.IntegerField(default=0)
    app_name=models.ForeignKey(Appnames)

    def __str__(self):
        return (self.step_title)