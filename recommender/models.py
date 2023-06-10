from django.db import models
from django.utils import timezone
from django.utils.text import slugify


class GameType(models.Model):
    title = models.CharField(max_length=30)
    slug = models.SlugField(max_length=30, default='')

    class Meta:  
        ordering = ['-title']  # Creating a sort order from newest to oldest
        indexes = [models.Index(fields=['-title']),]  # This will improve performance for queries filtering or ordering results by this field
    def __str__(self):  # for human-readable representation of the object
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=50)
    class Meta:  
        ordering = ['-title']  # Creating a sort order from newest to oldest
        indexes = [models.Index(fields=['-title']),]  # This will improve performance for queries filtering or ordering results by this field
    def __str__(self):  # for human-readable representation of the object
        return self.title

class Mechanic(models.Model):
    title = models.CharField(max_length=50)
    class Meta:  
        ordering = ['title']  # Creating a sort order from newest to oldest
        indexes = [models.Index(fields=['-title']),]  # This will improve performance for queries filtering or ordering results by this field
    def __str__(self):  # for human-readable representation of the object
        return self.title

class Designer(models.Model):
    title = models.CharField(max_length=50)
    class Meta:  
        ordering = ['-title']  # Creating a sort order from newest to oldest
        indexes = [models.Index(fields=['-title']),]  # This will improve performance for queries filtering or ordering results by this field
    def __str__(self):  # for human-readable representation of the object
        return self.title

class Artist(models.Model):
    title = models.CharField(max_length=50)
    class Meta:  
        ordering = ['-title']  # Creating a sort order from newest to oldest
        indexes = [models.Index(fields=['-title']),]  # This will improve performance for queries filtering or ordering results by this field
    def __str__(self):  # for human-readable representation of the object
        return self.title


class Game(models.Model):
    gameid = models.IntegerField()
    title = models.CharField(max_length=150)
    year = models.IntegerField(blank=True, null=True)
    num_voters = models.IntegerField(blank=True, null=True) # number of voters
    rating_geek = models.FloatField(blank=True, null=True)
    rating_avg = models.FloatField(blank=True, null=True)
    gametype = models.ManyToManyField(GameType, blank=True)
    category = models.ManyToManyField(Category, blank=True)
    mechanic = models.ManyToManyField(Mechanic,blank=True)
    designer = models.ManyToManyField(Designer, blank=True)
    artist = models.ManyToManyField(Artist, blank=True)
    playingtime = models.IntegerField(blank=True, null=True)
    minplayers = models.IntegerField(blank=True, null=True)
    maxplayers = models.IntegerField(blank=True, null=True)
    minage = models.IntegerField(blank=True, null=True)
    weight = models.FloatField(blank=True, null=True)
    image_url = models.URLField(blank=True)

    class Meta:  
        ordering = ['-title']  # Creating a sort order from newest to oldest
        indexes = [models.Index(fields=['-title']),]  # This will improve performance for queries filtering or ordering results by this field
    def __str__(self):  # for human-readable representation of the object
        return self.title

class User(models.Model):
    name = models.CharField(max_length=50)
    games_rec = models.ManyToManyField(Game, blank=True)
    class Meta:  
        ordering = ['-name']  # Creating a sort order from newest to oldest
        indexes = [models.Index(fields=['-name']),]  # This will improve performance for queries filtering or ordering results by this field
    def __str__(self):  # for human-readable representation of the object
        return self.name


class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    game = models.ForeignKey(Game, on_delete=models.CASCADE, blank=True)
    rating = models.IntegerField()

    def __str__(self):
        return f"{self.user}: {self.rating}"

