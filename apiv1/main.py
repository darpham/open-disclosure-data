from flask import Blueprint, request, redirect, jsonify

api = Blueprint("api", __name__)

@api.route("/")
def health_check():
  info = {
    "Name": "Open Discolusre Data API",
    "Description": "API for scraping, cleaning, and providing data around COVID-19 in the San Francisco Bay Area",
    "GitHub": "https://github.com/darpham/open-disclosure-data",
    "Version": "apiv1"
  }
  return jsonify(info)

