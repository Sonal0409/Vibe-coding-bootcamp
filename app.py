# Generate a python code that 
# creates a simple web server using Flask that returns "AI DevOps Bootcamp is awsome!" when the root URL is accessed.
# app should run on port 5000 
# host on 0.0.0.0
from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "AI DevOps Advanced Pipeline Running!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)



