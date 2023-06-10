import csv
from .models import GameType, Category, Mechanic, Designer, Artist, User, Game, Rating


# example of a path:  path = r'C:\Dev\BG_Recommender\bgrecommender\recommender\gametype_unique.csv'

# check mechanic "Deck, Bag, and Pool Building"

def populate_gametype(file_path):
    with open(file_path, 'r', encoding='utf-8') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            title = row['title']
            gametype = GameType(title=title)
            gametype.save()

def populate_category(file_path):
    with open(file_path, 'r', encoding='utf-8') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            title = row['title']
            category = Category(title=title)
            category.save()

def populate_mechanic(file_path):
    with open(file_path, 'r', encoding='utf-8') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            title = row['title']
            mechanic = Mechanic(title=title)
            mechanic.save()

def populate_designer(file_path):
    with open(file_path, 'r', encoding='utf-8') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            title = row['title']
            designer = Designer(title=title)
            designer.save()

def populate_artist(file_path):
    with open(file_path, 'r', encoding='utf-8') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            title = row['title']
            artist = Artist(title=title)
            artist.save()


def check(file_path):
    with open(file_path, 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            print(row)  # Print the row dictionary to inspect its structure

            # Access the 'title' key and handle KeyError if needed
            title = row.get('title')

def populate_game(file_path):  # from 1000games_complete.csv
    with open(file_path, 'r', encoding='utf-8') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            gameid = row['gameid']
            title = row['title']
            playingtime = row['playingtime']
            minplayers = row['minplayers']
            maxplayers = row['maxplayers']
            minage = row['minage']
            weight = row['weight']
            year = row['year']
            num_voters = row['num_voters']
            rating_geek = row['geek_rating']
            rating_avg = row['avg_rating']
            urlpic = row['urlpic']

            if not Game.objects.filter(gameid=gameid).exists():

                game = Game(
                    gameid=gameid,
                    title=title,      
                    playingtime=playingtime,
                    minplayers=minplayers,
                    maxplayers=maxplayers,
                    minage=minage,
                    weight=weight,
                    year=year,
                    num_voters=num_voters,
                    rating_geek=rating_geek,
                    rating_avg=rating_avg,
                    image_url=urlpic,
                )
                
                game.save()

                # Check if GameType objects exist
                gametypes = row['gametype'].split(';; ')
                for gametype in gametypes:
                    if GameType.objects.filter(title=gametype).exists():
                        gt = GameType.objects.get(title=gametype) 
                        game.gametype.add(gt.id)
                    else:
                        print(f"GameType '{gametype}' for the game {title} id#{gameid} does not exist.")

                # Check if Category objects exist
                categories = row['category'].split(';; ')
                for category in categories:
                    if Category.objects.filter(title=category).exists():
                        cat = Category.objects.get(title=category) 
                        game.category.add(cat.id)
                    else:
                        print(f"Category '{category}' for the game {title} id#{gameid} does not exist.")
                
                # Check if Mechanic objects exist
                mechanics = row['mechanic'].split(';; ')
                for mechanic in mechanics:
                    if Mechanic.objects.filter(title=mechanic).exists():
                        mech = Mechanic.objects.get(title=mechanic) 
                        game.mechanic.add(mech.id)
                    else:
                        print(f"Mechanic '{mechanic}' for the game {title} id#{gameid} does not exist.")

                game.save()
            else:
                print(f"The game {title} with id #{gameid}  already exists")


def populate_user(file_path):
    with open(file_path, 'r', encoding='utf-8') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            name = row['name']
            if not User.objects.filter(name=name).exists():  # add only new users
                user = User(name=name)
                user.save()
            else:
                print(f"{name} is already exist")


def populate_user_recgames(file_path):  # populated users with recommened games
    with open(file_path, 'r', encoding='utf-8') as csv_file:
        reader = csv.DictReader(csv_file)
        counter = 1
        for row in reader:
            name = row['user']
            gameid = row['gameid']
            if not User.objects.filter(name=name).exists():  # add only new users
                user = User(name=name)
                user.save()
            game = Game.objects.get(gameid=gameid) 
            user.games_rec.add(game.id)
            user.save()
            if counter % 10000 == 0:
                print(f"Entry #{counter} added")
            counter += 1

def populate_rating(file_path):  # from csv file: gameid, user, rating
    with open(file_path, 'r', encoding='utf-8') as csv_file:
        reader = csv.DictReader(csv_file)
        counter = 1
        for row in reader:
            gameid = row['gameid']
            user=row['user']
            rating_value=float(row['rating'])

            if Game.objects.filter(gameid=gameid).exists():
                if User.objects.filter(name=user).exists():
                    bgame = Game.objects.get(gameid=gameid) 
                    buser = User.objects.get(name=user)
                    if Rating.objects.filter(user=buser, game=bgame).exists():
                        print(f'This {bgame}:{buser} is already exist')
                    else:
                    
                        rating = Rating(     
                            user = buser,
                            game = bgame, 
                            rating=rating_value,
                        )
                        rating.save()
                    

                    if counter % 10000 == 0:
                        print(f"Rating #{counter} added")
                    counter += 1
                else:
                    print(f"{user} does not exist")
            else:
                print(f"Game with id #{gameid} does not exist")

def get_game_ratings(game_id):
    # all ratings for a given game
    game = Game.objects.get(gameid=game_id)
    ratings = Rating.objects.filter(game=game)
    return ratings

def get_user_ratings(username):
    # all ratings for a given user
    user = User.objects.get(name=username)
    ratings = Rating.objects.filter(user=user)
    for rating in ratings:
        print(f"{rating.game} - {rating.rating}")
    return ratings