from django.db import models

# Create your models here.
class Web(models.Model):
    title=models.CharField(max_length=200)
    description=models.CharField(max_length=500)
    completed=models.BooleanField(default=False)

    # string representation of the class
    def __str__(self):
        #it will return the title
        return self.title 