db.messages.find({
  "headers.From": "andrew.fastow@enron.com",
  "headers.To": {'$in': ["jeff.skilling@enron.com"]}
}).count();
