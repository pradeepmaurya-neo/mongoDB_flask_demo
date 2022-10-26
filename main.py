from flask import Flask,  Response, render_template
import json
import pymongo
from pymongo import MongoClient
from bson.json_util import dumps

app = Flask(__name__)
app.secret_key = "secret key"
# pkaOGvdL5KcHqvth
MONGODB_URI= 'paset your Url here'
client = pymongo.MongoClient(MONGODB_URI)

# db = client.test_database
# db = client.collections
#
# first add for future commit


@app.route("/", methods=['POST', 'GET'])
def home_page():
    # online_users = client.db.user.insert_one({'hello':'Pradeep'})
    # online_users = client.new.user.insert_one({'hello':'Pradeep', 'id':1245, 'place':'pune'})
    online_users = client.new.user1.insert_one({'hello':'Pradeep', 'id':1245, 'place':'pune'})
    return render_template("index.html", online_users=online_users)

@app.route('/read', methods=['GET'])
def read_data():
    hello = client.new.user1.find()
    resp = dumps(hello)
    return resp


if __name__ == "__main__":
    app.run(debug=True)



