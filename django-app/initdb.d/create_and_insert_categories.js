db.categories.drop();

db.createCollection("categories", {
   validator: {
      $jsonSchema: {
         bsonType: "object",
         required: [ "_id", "name" ],
         properties: {
            _id: {
               bsonType: "int",
               description: "must be an integer and is required"
            },
            name: {
               bsonType: "string",
               description: "must be a string and is required"
            }
         }
      }
   }
});

db.categories.insertMany([
  { "_id": 1, "name": "Sadness" },
  { "_id": 2, "name": "Stress at Work" },
  { "_id": 3, "name": "Guilt" },
  { "_id": 4, "name": "Body Image" },
  { "_id": 5, "name": "Social Anxiety" },
  { "_id": 6, "name": "Loneliness" },
  { "_id": 7, "name": "Self-Doubt" },
  { "_id": 8, "name": "Anxiety" },
  { "_id": 9, "name": "Anger Management" },
  { "_id": 10, "name": "Procrastination" },
  { "_id": 11, "name": "Imposter Syndrome" }
])