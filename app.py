from flask import Flask

app = Flask(__name__)

@app.route("/")
def ghw():
    return "<p>Hello, API week Ryan from ash ketchup!</p>" 
if __name__=="__main__":
    app.run(debug=True)