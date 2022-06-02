from flask import Flask, Blueprint, request, render_template, make_response, jsonify, redirect, url_for, session

dverse_bp = Blueprint("dverse", __name__)


@dverse_bp.route("/")
@dverse_bp.route("/login")
def login():
    return render_template("login.html")

@dverse_bp.route("/welcome", methods=["POST", "GET"])
def welcome(username=None):
    if request.method == "POST":
        temp = request.form["username"]
        temp2 = request.form["hp"]
        return render_template("welcome.html", name = temp, hp = temp2)
    else:
        temp = request.args.get("username")
        return render_template("welcome.html", name=temp)

@dverse_bp.route("/list")
def dverse_list():
    return render_template("list.html")

@dverse_bp.route("/losttime")
def losttime():
    return render_template("detailed_losttime.html")

@dverse_bp.route("/eco")
def eco():
    return render_template("detailed_eco.html")

@dverse_bp.route("/eco_intro")
def eco_intro():
    return render_template("eco_intro.html")

