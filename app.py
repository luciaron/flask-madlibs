from flask import Flask, request
from stories import Story, story, answers

app = Flask(__name__)

