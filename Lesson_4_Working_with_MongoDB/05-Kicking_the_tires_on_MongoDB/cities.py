"""
Your task is to sucessfully run the exercise to see how pymongo works
and how easy it is to start using it.
You don't actually have to change anything in this exercise,
but you can change the city name in the add_city function if you like.

Your code will be run against a MongoDB instance that we have provided.
If you want to run this code locally on your machine,
you have to install MongoDB (see Instructor comments for link to installation information)
and uncomment the get_db function.

########
To have launchd start mongodb at login:
    ln -sfv /usr/local/opt/mongodb/*.plist ~/Library/LaunchAgents
Then to load mongodb now:
    launchctl load ~/Library/LaunchAgents/homebrew.mxcl.mongodb.plist
Or, if you don't want/need launchctl, you can just run:
    mongod --config /usr/local/etc/mongod.conf
==> Summary
  /usr/local/Cellar/mongodb/2.6.7: 17 files, 332M
Witolds-MacBook-Pro:pwiz witold$ more /usr/local/etc/mongod.conf
systemLog:
  destination: file
  path: /usr/local/var/log/mongodb/mongo.log
  logAppend: true
storage:
  dbPath: /usr/local/var/mongodb
net:
  bindIp: 127.0.0.1
Witolds-MacBook-Pro:pwiz witold$ mongod --config /usr/local/etc/mongod.conf

"""
from pymongo import MongoClient


def get_db():
    client = MongoClient('localhost:27017')
    # 'examples' here is the database name. It will be created if it does not exist.
    db = client.examples
    return db

def add_city(db):
    db.cities.insert({"name" : "Chicago"})
    
def get_city(db):
    return db.cities.find_one()


if __name__ == "__main__":

    db = get_db() # uncomment this line if you want to run this locally
    add_city(db)
    print get_city(db)