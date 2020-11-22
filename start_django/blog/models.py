from django.db import models

# Create your models here.
class Furite(models.model):
    name = models.CharField(max_length=50)
    descript = models.FloatField()
    price = models.FloatField()
    quantity = models.IntegerField()
    cdate = models.DateTiemField(auto_now_add=True)

    def __str__(self):
        return[self.id,self.name,self.descript]