from django.db import models

#models bibliotekani ichidan Model class-ga murojat qivotti

class Person(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    cat = models.ForeignKey("Category", models.PROTECT)

    def __str__(self):
        return self.name


class Category(models.Model):
    cat_name = models.CharField(max_length=60)

    def __str__(self):
        return self.cat_name

# Person, Category - bu bizda database-da table name bo'ladi
#Buni hozir Migration qilsak bu database-ga borib ikta table yaratib beradi: Person, Category
