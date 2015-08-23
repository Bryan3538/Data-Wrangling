import json
import requests

BASE_URL = "http://musicbrainz.org/ws/2/"
ARTIST_URL = BASE_URL + "artist/"

query_type = {  "simple": {},
                "atr": {"inc": "aliases+tags+ratings"},
                "aliases": {"inc": "aliases"},
                "releases": {"inc": "releases"}}


def query_site(url, params, uid="", fmt="json"):
    params["fmt"] = fmt
    r = requests.get(url + uid, params=params)
    #print "requesting", r.url

    if r.status_code == requests.codes.ok:
        return r.json()
    else:
        r.raise_for_status()


def query_by_name(url, params, name):
    params["query"] = "artist:" + name
    return query_site(url, params)


def pretty_print(data, indent=4):
    if type(data) == dict:
        print json.dumps(data, indent=indent, sort_keys=True)
    else:
        print data


def question_one():
	name = "First Aid Kit"
	total = 0
	results = query_by_name(ARTIST_URL, query_type["simple"], name)
	for artist in results["artists"]:
		if artist["name"] == name:
			total += 1

	print "How many artists are there named \"First Aid Kit\"? ", total

def question_two():
	results = query_by_name(ARTIST_URL, query_type["simple"], "Queen")
	begin_area = results["artists"][0]["begin-area"]["name"]
	print "What is the begin-area for Queen? ", begin_area

def question_three():
	results = query_by_name(ARTIST_URL, query_type["simple"], "Beatles")
	artist_id = results["artists"][0]["id"]
	results = query_site(ARTIST_URL, query_type["aliases"], artist_id)

	for alias in results["aliases"]:
		if alias["locale"] == "es":
			print "The Spanish alias for The Beatles is: ", alias["name"]
			break

def question_four():
	results = query_by_name(ARTIST_URL, query_type["simple"], "Nirvana")
	disambiguation = results["artists"][0]["disambiguation"]
	print "Nirvana\'s disambiguation is: ", disambiguation
	

def question_five():
	results = query_by_name(ARTIST_URL, query_type["simple"], "One Direction")
	results = query_site(ARTIST_URL, query_type["simple"], results["artists"][0]["id"])
	start_date = results["life-span"]["begin"]
	print "One Direction was formed on: ", start_date

def main():
	question_one()
	question_two()
	question_three()
	question_four()
	question_five()

if __name__ == '__main__':
    main()