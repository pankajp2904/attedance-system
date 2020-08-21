#Connection created with mongodb

import pymongo
client=''
def connection():
    maxSevSelDelay = 1 
    try:
        client = pymongo.MongoClient("mongodb://localhost:27017/",
                                     serverSelectionTimeoutMS=maxSevSelDelay)
        client.server_info()
        database=client["student_attendance_system"]
        return database
    except pymongo.errors.ServerSelectionTimeoutError as err:
        return False
