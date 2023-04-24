from django.db import models
import redis
import json

# Create your models here.

class Board(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

    @classmethod
    def get_boards(cls):
        r = redis.Redis(host='localhost', port=6379, db=0)

        # Try to get data from Redis cache
        boards = r.get('boards')
        if boards:
            # If data is available in Redis cache, return it
            return json.loads(boards)

        # If data is not available in Redis cache, fetch it from database
        boards = cls.objects.all().values('id', 'name', 'description')

        # Store fetched data in Redis cache
        r.set('boards', json.dumps(list(boards)))
        return boards


class List(models.Model):
    board = models.ForeignKey(Board, on_delete=models.CASCADE, related_name='lists')
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Card(models.Model):
    list = models.ForeignKey(List, on_delete=models.CASCADE, related_name='cards')
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    due_date = models.DateTimeField(blank=True, null=True)
    background = models.ImageField(upload_to='card_backgrounds/', blank=True, null=True)
    pellets = models.ImageField(upload_to='card_pellets/', blank=True, null=True)

    def __str__(self):
        return self.name

    @classmethod
    def get_cards(cls, list_id):
        r = redis.Redis(host='localhost', port=6379, db=0)

        # Try to get data from Redis cache
        cards = r.get(f'cards_{list_id}')
        if cards:
            # If data is available in Redis cache, return it
            return json.loads(cards)

        # If data is not available in Redis cache, fetch it from
