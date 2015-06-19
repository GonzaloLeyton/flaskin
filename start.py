#!flask/bin/python
# -*- coding: utf-8 -*-

from flask import Flask, jsonify, request, make_response, abort
import pymongo, os, json, uuid, hashlib, datetime

app = Flask(__name__)

@app.route('/')
def hello():
    return "Welcome to Flask on Heroku!"

if __name__ == '__main__':
    app.run(debug=True)