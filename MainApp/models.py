from django.db import models

class Languages(models.Model):
    name = models.CharField(max_length=30)


class Countries(models.Model):
    name = models.CharField(max_length=50)

    def __repr__(self):
        return f"Country {self.name}"
