from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = '7f6c53a8f5bfd7fb547adfdf'
from influencer import routes
