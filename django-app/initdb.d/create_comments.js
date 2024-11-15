db.comments.drop()

db.createCollection("comments", {
   validator: {
      $jsonSchema: {
         bsonType: "object",
         required: [ "category_id", "author", "content"],
         properties: {
            category_id: {
               bsonType: "int",
            },
            author: {
               bsonType: "string",
            },
            content: {
               bsonType: "string",
            },
         }
      }
   }
});