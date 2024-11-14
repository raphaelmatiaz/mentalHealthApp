db.comments.drop()

db.createCollection("comments", {
   validator: {
      $jsonSchema: {
         bsonType: "object",
         required: [ "phrase_id", "user_name", "content", "created_at" ],
         properties: {
            phrase_id: {
               bsonType: "int",
               description: "must be an integer and is required"
            },
            author: {
               bsonType: "string",
               description: "must be a string and is required"
            },
            content: {
               bsonType: "string",
               description: "must be a string and is required"
            },
            created_at: {
               bsonType: "date",
               description: "must be a date and is required"
            },
         }
      }
   }
});