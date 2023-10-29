from django.db import models

# Create your models here.

class Writer(models.Model):
    first_name = models.CharField(max_length=127)
    last_name = models.CharField(max_length=127)
    sex = models.CharField(max_length=2, blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Comment(models.Model):
    writer = models.ForeignKey(Writer, on_delete=models.SET(1))
    title = models.CharField(max_length=255)
    text = models.TextField()
    reply = models.IntegerField()

    def __str__(self):
        return self.title
