from flask import Flask, request, render_template, jsonify, session
from boggle import Boggle

app = Flask(__name__)
app.config["SECRET_KEY"] = "phillyflyersarechampions"

boggle_game = Boggle()


@app.route('/')
def startpage():
    """Show the game board."""

    board = boggle_game.make_board()
    session['board'] = board

    return render_template("index.html", board=board)
