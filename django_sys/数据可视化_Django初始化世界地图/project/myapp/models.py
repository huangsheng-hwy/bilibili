from django.db import models


# Create your models here.

class Grades(models.Model):
    gname = models.CharField(max_length=20)
    gdate = models.DateTimeField()
    ggirlnum = models.IntegerField()
    gboynum = models.IntegerField()
    isDelete = models.BooleanField(default=False)

    def __str__(self):
        return self.gname


class Students(models.Model):
    sname = models.CharField(max_length=20, verbose_name='sname')
    sgender = models.BooleanField(default=True, verbose_name='sgender')
    sage = models.IntegerField()
    scontend = models.CharField(max_length=20)
    isDelete = models.BooleanField(default=False)
    sgrade = models.ForeignKey("Grades", on_delete=models.CASCADE)

    def __str__(self):
        return self.sname
