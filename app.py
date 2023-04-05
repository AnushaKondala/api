from flask import Flask

app = Flask(__name__)

@app.route("/")
def ghw():
    return "<p>Hello, API from ANUSHA!</p>" 
if __name__=="__main__":
    app.run(debug=True)