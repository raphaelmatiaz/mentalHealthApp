from urllib.parse import quote_plus
from django.conf import settings
from mongo.models import Comment
from pymongo import MongoClient
<<<<<<< HEAD
=======
from datetime import datetime
>>>>>>> 1eb884ecd59cb322da732a9059630959933c0d33


class Mongo:
    def __init__(
        self,
        database: str = settings.MONGO_DB,
        host: str = settings.MONGO_HOST,
        password: str = settings.MONGO_PASSWORD,
        port: int = settings.MONGO_PORT,
        user: str = settings.MONGO_USERNAME,
    ):
        self.default_database = database
        self.uri = "mongodb://%s:%s@%s:%i/" % (
            quote_plus(user),
            quote_plus(password),
            host,
            port,
        )
<<<<<<< HEAD

def get_comments(self, category_id: int) -> list[Comment]:
        with MongoClient(self.uri) as client:
            db = client.get_database(self.default_database)
            collection = db.get_collection("comments")
            comments = collection.find({"category_id": category_id})

            return [Comment(**comment) for comment in comments]
=======
     
    def db_add_comment(self, phrase_id: int, user_name: str, content: str) -> bool:
        with MongoClient(self.uri) as client:
            db = client.get_database(self.default_database)
            collection = db.get_collection("Comments")
            
            comment = {
                "phrase": phrase_id,
                "author": author,
                "content": content,
            }
            
            result = collection.insert_one(comment)
            return bool(result.inserted_id)
        
    def db_get_comment(self, phrase_id: int) -> list[Comment]:
        with MongoClient(self.uri) as client:
            db = client.get_database(self.default_database)
            collection = db.get_collection("Comments")
            comments = collection.find({"phrase_id": phrase_id})

            return [Comment(**comment) for comment in comments]
            
    
>>>>>>> 1eb884ecd59cb322da732a9059630959933c0d33
