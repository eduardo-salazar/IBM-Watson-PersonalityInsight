# IBM Watson Personal Insight
This project returns a personality insight from a document.


# Mongo Db Run
mongod --dbpath /Volumes/DB/Tweeter/
db.tweets_en.createIndex( { 'user.id': 1 } )

mongodump --collection tweets_en --db geo_tweets --out /Volumes/Edward/DB/Backup/