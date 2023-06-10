from django.contrib import admin
from .models import GameType, Category, Mechanic, Designer, Artist, User, Game, Rating


@admin.register(GameType)
class GameTypeAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    ordering = ['title']
    list_display = ['title']
    search_fields = ['title']

@admin.register(Mechanic)
class MechanicAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title']

@admin.register(Designer)
class DesignerAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title']

@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title']

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

@admin.register(Game)  # ! changing this line
class GameAdmin(admin.ModelAdmin):
    list_display = ['title', 'year', 'num_voters', 'rating_geek', 'rating_avg',
                     'playingtime', 'minplayers',
                    'maxplayers', 'minage', 'weight']
    list_filter = ['year', 'gametype', 'category', 'mechanic', 'playingtime', 'minage',]
    search_fields = ['title']
    ordering = ['rating_geek', 'year']

@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ['user', 'game', 'rating']