from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def start():
    title = "The Bright Light"
    
    text = """On a quiet Sunday morning you wake up and start walking down the stairs, suddenly you see a shiny portal on the kitchen wall, what will you do?"""

    choices = [
        ('go_into_the_portal',"Go_inside"),
        ('walk_away',"leave_the_house!!!")
    ]

    return render_template('adventure.html', title=title, text=text, choices=choices)



@app.route("/inside")
def enter_house():
    title = "You go inside..."
    
    text = """... You enter the portal and you go in a beautiful forest where there is a sign saying Go left if you wan to follow your dreams."""

    choices = [
        ('Follow_the_sign',"Go_into_the_forest"),
        ('go_back_to_the_kitchen',"back_though_the_portal")
    ]

    return render_template('adventure.html', title=title, text=text, choices=choices)

@app.route("/escape")
def run_away():
    title = "You go back through the portal!"
    
    text = """You run as fast as you can outside of the house trying to find help from someone to close the portal."""

    choices = []

    return render_template('adventure.html', title=title, text=text, choices=choices)



@app.route("/stairs")
def up_stairs():
    title = "Look out!"
    
    text = """As you run out a big monster jumps in front of you."""

    choices = []

    return render_template('adventure.html', title=title, text=text, choices=choices)
