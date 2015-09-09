from pymongo import MongoClient
import pprint

client = MongoClient("mongodb://localhost:27017")
db = client.examples

def highest_ratio():
	result = db.tweets.aggregate([
			{"$match" : {"user.friends_count" : {"$gt" : 0},
						 "user.followers_count" : {"$gt" : 0 } } },
			{"$project" : {"ratio" : {"$divide" : ["$user.followers_count",
													"$user.friends_count"]},
							"screen_name" : "$user.screen_name",  
							"_id" : 0} },
			{"$sort" : {"ratio" : -1}},
			{"$limit" : 1}
		])

	return result

if __name__ == '__main__':
	result = highest_ratio()
	pprint.pprint(result.next())