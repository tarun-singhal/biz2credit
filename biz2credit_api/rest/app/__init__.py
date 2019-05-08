
"""This is init module."""

from flask import Flask

# Place where app is defined
app = Flask(__name__)


from app import v1
# from app import blogData