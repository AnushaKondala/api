from flask import Flask, request

app = Flask(__name__)

hackathons={
    "GHW:API WEEK":{
    "start_date":"2023-04-03",
    "end_date":"2023-04-10",
    "type":"Digital Only"
    },
    "Bitcamp":{
    "start_date":"2023-04-07",
    "end_date":"2023-04-09",
    "type":"In person only"
    }
}
@app.route("/")
def ghw():
    return "<p>Hello, API from ANUSHA!</p>" 

@app.route("/getHackathons",methods=['GET'])
def getHackathons():
   return hackathons

if __name__=="__main__":
    app.run(debug=True)
