import os

from flask import Flask, jsonify
from pymongo import MongoClient
from pymongo.errors import PyMongoError

app = Flask(__name__)

MONGO_URI = os.environ.get("MONGO_URI", "mongodb://mongo:27017/")
DB_NAME = os.environ.get("MONGO_DB", "appdb")

client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=3000)
db = client[DB_NAME]


@app.route("/")
def hello():
    return "Hello, World!"


@app.route("/health")
def health():
    try:
        client.admin.command("ping")
        db.visits.insert_one({"source": "health"})
        count = db.visits.count_documents({})
        return jsonify(status="ok", mongo="connected", database=DB_NAME, visits=count)
    except PyMongoError as exc:
        return jsonify(status="error", mongo="unreachable", detail=str(exc)), 503


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)