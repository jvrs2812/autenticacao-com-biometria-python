from pymongo import MongoClient


def get_database():

    CONNECTION_STRING = "mongodb://APSUNIP:APSUNIP@localhost:27017/?authMechanism=DEFAULT"

    try:
        client = MongoClient(
            CONNECTION_STRING, serverSelectionTimeoutMS=5000)
        return client

    except Exception:
        print("Unable to connect to the server.")
        return
