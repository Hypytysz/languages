from django.db import models

# Create your models here.

class Box(models.Model):
    box_name = models.CharField(max_length=100)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.box_name}"

class Card(models.Model):
    question = models.CharField(max_length=100)
    answer = models.CharField(max_length=100)
    box = models.ForeignKey('cards.Box', on_delete=models.CASCADE, related_name='boxs')
    date_created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.question