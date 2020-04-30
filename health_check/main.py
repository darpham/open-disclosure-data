from flask import Blueprint

ping = Blueprint("health_check", __name__)

# @health_check.route("/health_check")
@ping.route("/health_check")
def health_check():
  return "healthy"

""" TODO - create health_check enpoint
- connection to DB
- local file CRUD
- able to upload/download to S3
"""