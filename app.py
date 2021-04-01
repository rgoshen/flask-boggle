from flask import Flask, request, render_template, jsonify, session
from boggle import Boggle

app = Flask(__name__)
<<<<<<< HEAD
app.config["SECRET_KEY"] = "fdfgkjtjkkg45yfdb"
=======
app.config["SECRET_KEY"] = "phillyflyersarechampions"
>>>>>>> 3feba4ea20661e9a8951d9e33795830e8777b6b5

boggle_game = Boggle()


<<<<<<< HEAD
@app.route("/")
def homepage():
    """Show board."""

    board = boggle_game.make_board()
    session['board'] = board
    highscore = session.get("highscore", 0)
    nplays = session.get("nplays", 0)

    return render_template("index.html", board=board,
                           highscore=highscore,
                           nplays=nplays)


@app.route("/check-word")
def check_word():
    """Check if word is in dictionary."""

    word = request.args["word"]
    board = session["board"]
    response = boggle_game.check_valid_word(board, word)

    return jsonify({'result': response})


@app.route("/post-score", methods=["POST"])
def post_score():
    """Receive score, update nplays, update high score if appropriate."""

    score = request.json["score"]
    highscore = session.get("highscore", 0)
    nplays = session.get("nplays", 0)

    session['nplays'] = nplays + 1
    session['highscore'] = max(score, highscore)

    return jsonify(brokeRecord=score > highscore)
=======
@app.route('/')
def startpage():
    """Show the game board."""

    board = boggle_game.make_board()
    session['board'] = board

    return render_template("index.html", board=board)
>>>>>>> 3feba4ea20661e9a8951d9e33795830e8777b6b5
