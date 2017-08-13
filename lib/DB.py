from pymongo import MongoClient

class DB(object):
    def __init__(self, host, port, database):
        self.db = Mongoclient(host, port
