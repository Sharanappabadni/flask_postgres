from app import app
from flask import jsonify, request
from .views import User

user_view = User.as_view('user_view')
app.add_url_rule('/user', methods=['GET', 'POST'], view_func=user_view)