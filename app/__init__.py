from flask import Flask
from infra.repository.post_repository import PostRepository

app = Flask(__name__)
repo = PostRepository()

from app.controllers import default