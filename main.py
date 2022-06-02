from flask import Flask, jsonify, request, render_template, make_response, session
from view import dverse_bp
import os

os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

app = Flask(__name__, static_url_path="/static")
app.secret_key = "dverse_server"

app.register_blueprint(dverse_bp.dverse_bp, url_prefix="/dverse")


if __name__ == "__main__":
    app.run(host="localhost", port="8080", debug=True)