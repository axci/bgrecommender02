from django.urls import path
from . import views
app_name = 'recommender'

urlpatterns = [
    # post views
    path('', views.game_list, name='game_list'),
    path('type/<int:id>/', views.gametype_view, name='gametype_view'),
    path('category/<int:id>/', views.category_view, name='category_view'),
    path('mechanic/<int:id>/', views.mechanic_view, name='mechanic_view'),
    path('game/<int:id>/', views.game_view, name='game_detail'),
]
