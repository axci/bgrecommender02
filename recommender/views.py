from django.shortcuts import render, get_object_or_404
from .models import Game, GameType, User, Category, Mechanic
from .forms import UserForm


def game_list(request):
    games = Game.objects.all()  # all games
    gametypes = GameType.objects.all()
    
    username = request.GET.get('username')  # from index.html form
    context = {
        'games': games,
        'gametypes': gametypes,
        'form': UserForm(),
    }

    if username:
        try:
            user = User.objects.get(name=username)  # get above user from User model
            recommended_games = user.games_rec.all()
            context['user'] = user
            context['recommended_games'] = recommended_games
        except User.DoesNotExist:
            context['error_message'] = f"User '{username}' not found."
    
    return render(request, 'recommender/index.html', context)


def gametype_view(request, id):
    gametype = get_object_or_404(GameType, id=id)
    games = Game.objects.filter(gametype__id=id).order_by('-rating_geek')
    context = {
        'games': games,
        'gametype': gametype,
    }
    return render(request, 'recommender/gametype.html', context)

def category_view(request, id):
    category = get_object_or_404(Category, id=id)
    games = Game.objects.filter(category__id=id).order_by('-rating_geek')
    context = {
        'games': games,
        'category': category,
    }
    return render(request, 'recommender/category.html', context)

def mechanic_view(request, id):
    mechanic = get_object_or_404(Mechanic, id=id)
    games = Game.objects.filter(mechanic__id=id).order_by('-rating_geek')
    context = {
        'games': games,
        'mechanic': mechanic,
    }
    return render(request, 'recommender/mechanic.html', context)

def game_view(request, id):
    game = get_object_or_404(Game, id=id)
    gametypes = GameType.objects.all()
    context = {
        'game': game,
        'gametypes': gametypes,
    }
    return render(request, 'recommender/gamedetail.html', context)