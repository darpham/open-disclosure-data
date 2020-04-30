from flask import Flask

from health_check.main import ping
from apiv1.main import api
from datetime import datetime
import os

# Init App
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['JSON_SORT_KEYS'] = False
# Import Blueprints
app.register_blueprint(ping)
app.register_blueprint(api, url_prefix="/apiv1")

@app.route("/")
def test():
  return "Test"

# Run Server
if __name__ == "__main__":
  app.run(debug=True )