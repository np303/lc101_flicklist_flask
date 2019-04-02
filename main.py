from flask import Flask
import random

app = Flask(__name__)

app.config['DEBUG'] = True      # displays runtime errors in the browser, too

@app.route("/")
def index():
    # choose a movie by invoking our new function
    movie = get_random_movie()

    # build the response string
    day1 = "<h1>Movie of the Day</h1>"
    day1 += "<ul>"
    day1 += "<li>" + movie[0] + "</li>"
    day1 += "</ul>"

    # TODO: pick another random movie, and display it under
    # the heading "<h1>Tommorrow's Movie</h1>"
    day2 = "<h1>Tomorrow's Movie</h1>"
    day2 += "<ul>"
    day2 += "<li>" + movie[1] + "</li>"
    day2 += "</ul>"
    
    return day1 + day2

def get_random_movie():
    # TODO: make a list with at least 5 movie titles
    movies = ["The Crow", "Star Wars", "Fast N Furious", "Heavy Metal"]
    random.shuffle(movies)
    # TODO: randomly choose one of the movies, and return it
    return (movies[1], movies[2])


app.run()
