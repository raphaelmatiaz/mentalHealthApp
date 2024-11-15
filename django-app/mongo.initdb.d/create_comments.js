db.users.drop();

db.createCollection("comments", {
  validator: {
    $jsonSchema: {
      bsonType: "object",
      required: ["author", "category_id", "content"],
      properties: {
        author: {
          bsonType: "string",
        },
        phrase_id : {
          bsonType: "number",
        },
        content: {
          bsonType: "string",
        },
      }
    }
  }
});