from django.db import models

# когда создавать миграции и отправлять
# когда создается новая таблица или меняется архитектура старой

# в формате статьи
class Genres(models.Model): # Genres = таблица Genres в бд db.sqlite3
    # id == pk (primary key) джаго сам создаст
    title = models.CharField(max_length=50)
    content = models.TextField()
    image = models.ImageField(upload_to='images/', null=True, max_length=255)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)

    # id_film = models.IntegerField()
    # зависимости от фильмов
    def __str__(self):
        return self.title