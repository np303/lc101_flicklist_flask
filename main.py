from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True      # displays runtime errors in the browser, too

# a list of movies that nobody should have to watch
terrible_movies = [
    "Gigli",
    "Star Wars Episode 1: Attack of the Clones",
    "Paul Blart: Mall Cop 2",
    "Nine Lives",
    "Starship Troopers"
]

def get_current_watchlist():
    # returns user's current watchlist--hard coded for now
    return [ "Star Wars", "Minions", "Freaky Friday", "My Favorite Martian" ]



def get_watched_movies():
    return [ "The Matrix", "The Princess Bride", "Buffy the Vampire Slayer" ]


@app.route("/rating-confirmation", methods=['POST'])
def rate_movie():
    movie = request.form['movie']
    rating = request.form['rating']

    if movie not in get_watched_movies():
        # the user tried to rate a movie that isn't in their list,
        # so we redirect back to the front page and tell them what went wrong
        error = "'{0}' is not in your Watched Movies list, so you can't rate it, foo!".format(movie)

        # redirect to homepage, and include error as a query parameter in the URL
        return redirect("/?error=" + error)
     
    # if we didn't redirect by now, then all is well
    return render_template('rating-confirmation.html', movie=movie, rating=rating)

# Creates a new route called movie_ratings which handles a GET on /ratings
@app.route("/ratings", methods=['GET'])
def movie_ratings():
    return render_template('ratings.html', movies = get_watched_movies())

@app.route("/crossoff", methods=['POST'])
def crossed_off_movie():
    crossed_off_movie = request.form['crossed-off-movie']

    if crossed_off_movie not in get_current_watchlist():
    # the user tried to cross off a movie that isn't in their list,
    # so we redirect back to the front page and tell them what went wrong 
        error ="'{0}', is not in your Watchlist, so you can't cross it off, foo!".format(crossed_off_movie)

    # redirect to homepage, and include error as a query parameter in the URL
    return redirect ("/?error=" + error)

    #if we didn't redirect you by now, then all is good. 
    return render_template('crossoff.html', crossed_off_movie=crossed_off_movie)

@app.route("/add", methods=['POST'])
def add_movie():
    # look inside the request to figure out what the user typed
    new_movie = request.form['new-movie']

    # if the user typed nothing at all, redirect and tell them the error
    if (not new_movie) or (new_movie.strip() == ""):
        error = "Please specify the movie you want to add."
        return redirect("/?error=" + error)

    # if the user wants to add a terrible movie, redirect and tell them the error
    if new_movie in terrible_movies:
        error = "Trust me, you don't want to add '{0}' to your Watchlist".format(new_movie)
        return redirect("/?error=" + error)

    # 'escape' the user's input so that if they typed HTML, it doesn't mess up our site
    new_movie_escaped = cgi.escape(new_movie, quote=True)

    return render_template('add-confirmation.html', movie=new_movie)


@app.route("/")
def index():
    encoded_error = request.args.get("error")
    return render_template('edit.html', watchlist=get_current_watchlist(), error=encoded_error and cgi.escape(encoded_error, quote=True))

app.run()

