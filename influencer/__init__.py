from flask import Flask

app = Flask(__name__)
from influencer import routes
