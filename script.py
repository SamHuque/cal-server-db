from flask import Flask
import ics
from flask import send_file

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello, World!"


@app.route("/whatever")
def whatever():
    return "whatever"


# what is the host. I can put "0.0.0.0" as well and it works the same way
app.run(host="0.0.0", port=3500)
