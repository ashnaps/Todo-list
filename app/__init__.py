"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-chi7l2rhp8u7g2edn270-a.oregon-postgres.render.com",
        database="todo_al7o",
        user="todo_al7o_user",
        password="RSJ7frHVnqoH9FzNHj8QLFvU5FlZTjkV")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
