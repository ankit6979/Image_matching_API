# Image_matching_API
from flask import Flask, request, jsonify
from flask import render_template
#from firebase import firebase
import feature_matching as f
#firebase = firebase.FirebaseApplication('https://illegal-hoarding.firebaseio.com', None)
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.args.get:
        url1 = request.args.get("url1")
        url2 = request.args.get("url2")
        #parsing array here
        #url2 = request.args.get("url2")
        if(f.feature_matching(url1, url2, 0)):
            return "True"
    return "False"

#@app.route("/mahendra", methods=["GET", "POST"])
#def home_firebase():
    #result = firebase.get('/Boards', None, {'location': '18.5971665&73.7071467'})
    #return jsonify(result)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
