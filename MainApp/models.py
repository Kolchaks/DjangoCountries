from django.db import models


class Languages(models.Model):
    name = models.CharField(max_length=30)

    def __repr__(self):
        return f"Countries {self.name}"


class Countries(models.Model):
    name = models.CharField(max_length=50)
    languages = models.ManyToManyField(to=Languages)

    def __repr__(self):
        return f"Countries {self.name}"
