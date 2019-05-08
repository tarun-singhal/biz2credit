"""This is init module."""

from flask import Flask

# Place where app is defined
app = Flask(__name__)

from . import userResource, userListResource
from . import storyResource, storyListResource 