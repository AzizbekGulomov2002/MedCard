from django.db import models

# Create your models here.


class Logo(models.Model):
    logo = models.ImageField(upload_to='images')
    def __str__(self):
        return "Image"
    

class MedCard(models.Model):
    ichish_turi = models.CharField(max_length=100)
    dori_nomi = models.CharField(max_length=500)
    maxal = models.CharField(max_length=200)
    tayyorlandi = models.DateField()
    yaroqlilik = models.DateField()
    narx = models.IntegerField()

    count = models.IntegerField(default=19)

    def __str__(self):
        return self.dori_nomi

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.count > 0:
            instances = []
            for _ in range(self.count):
                instances.append(MedCard(
                    ichish_turi = self.ichish_turi,
                    dori_nomi=self.dori_nomi,
                    maxal=self.maxal,
                    tayyorlandi=self.tayyorlandi,
                    yaroqlilik=self.yaroqlilik,
                    narx=self.narx
                ))
            MedCard.objects.bulk_create(instances)
    