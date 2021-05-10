from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    return "welcome chandan tomar"

@app.route("/hello")
def hello():
    return "welcome hello"
    
if __name__=="__main__":
    app.run(host="0.0.0.0", port=8080)
