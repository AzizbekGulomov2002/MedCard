from django.db import models

# Create your models here.


class Logo(models.Model):
    logo = models.ImageField(upload_to='images')
    def __str__(self):
        return "Image"
    

class MedCard(models.Model):
    type = models.CharField(max_length=100)
    name = models.CharField(max_length=500)
    description = models.CharField(max_length=200)
    added_date = models.DateField()
    deadline = models.DateField()
    price = models.IntegerField()

    count = models.IntegerField(default=19)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.count > 0:
            instances = []
            for _ in range(self.count):
                instances.append(MedCard(
                    type = self.type,
                    name=self.name,
                    description=self.description,
                    added_date=self.added_date,
                    deadline=self.deadline,
                    price=self.price
                ))
            MedCard.objects.bulk_create(instances)
    