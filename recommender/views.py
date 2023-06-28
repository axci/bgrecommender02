from django.shortcuts import render, get_object_or_404
from django.core.mail import send_mail  # for sending email message
from .models import Game, GameType, User, Category, Mechanic
from .forms import UserForm, EmailForm


def game_list(request):
    games = Game.objects.all()  # all games
    gametypes = GameType.objects.all()
    
    # Sending a message to my email
    sent = False 
    if request.method == 'POST':
        # Form was submitted
        form_email = EmailForm(request.POST)
        if form_email.is_valid():
            # Form fields passed validation
            cd = form_email.cleaned_data
            subject = f"A message from {cd['name']} from mysite"
            message = f"{cd['name']} {cd['email']}\n\n{cd['message']}"
            send_mail(subject, message, 'm.kolbasov@gmail.com',
                      ['m.kolbasov@gmail.com'])
            sent = True
    else:
        form_email = EmailForm()

    context = {
        'games': games,
        'gametypes': gametypes,
        'sent': sent,
        'form_email': form_email,
        'form': UserForm(),
    }

    username = request.GET.get('username')  # from index.html form
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