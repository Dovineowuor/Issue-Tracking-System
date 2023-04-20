from django.db import models

# Create your Models here
class Board(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class List(models.Model):
    board = models.ForeignKey(Board, on_delete=models.CASCADE, related_name='lists')
    name = models.CharField(max_length=255)

class Card(models.Model):
    list = models.ForeignKey(List, on_delete=models.CASCADE, related_name='cards')
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    due_date = models.DateTimeField(blank=True, null=True)
    background = models.ImageField(upload_to='card_backgrounds/', blank=True, null=True)
    pellets = models.ImageField(upload_to='card_pellets/', blank=True, null=True)