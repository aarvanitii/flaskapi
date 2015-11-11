# Api Logic
from flask import Flask, render_template, redirect, url_for, request, Response
from pymongo import MongoClient
from bson import json_util, ObjectId
data_base = MongoClient()
mongo = data_base.tedhenat

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
	dictionary = mongo.personi.find()
	pergjigja = Response(response=json_util.dumps(dictionary), status=200, mimetype="application/json")
	return pergjigja

@app.route("/delete/<personi_id>", methods=["GET"])
def delete_record(personi_id):
	mongo.personi.remove({"_id": ObjectId(personi_id)})
	return redirect(url_for('index'))

if __name__ == "__main__":
	app.run(debug=True, host="0.0.0.0", port=5000)