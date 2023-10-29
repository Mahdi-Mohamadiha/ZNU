from django.db import models
from django.db.models.signals import post_migrate
from django.dispatch import receiver

# Create your models here.

@receiver(post_migrate)
def create_initial_data(sender, **kwargs):
    if sender.name == 'commentary':
        if Writer.objects.count() == 0:
            writer = Writer.objects.create(first_name="NA", last_name="NA", sex="NA")
            Comment.objects.create(writer=writer, title="NA", text="NA", reply=1)
            print("Message: Initial data created successfully for Writer and Comment models.")

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
