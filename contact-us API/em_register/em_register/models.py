from django.db import models


class em_register(models.Model ):
    your_name = models.CharField(max_length=100,default='')
    your_email = models.CharField(max_length=100,default='')
    subject=models.TextField(max_length=100,default='')
    message=models.TextField(max_length=500,default='')
    
 




    def __str__(self):
        return self.subject
    