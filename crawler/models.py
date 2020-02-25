from django.db import models

# Create your models here.
class notice(models.Model):
    writer = models.CharField(max_length = 10)
    date = models.DateField()
    title = models.CharField(max_length = 150, unique=True)
    detail = models.TextField()

    def __str__(self):
        return '%s - %s' % (self.title, self.date)
