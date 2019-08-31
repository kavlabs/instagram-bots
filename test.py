# import urllib.parse
# from urllib.request import urlopen
# import urllib.request
# def urlencode(str):
#   return urllib.parse.quote(str)
# t = urlencode('{"id":"263765230","include_reel":true,"fetch_mutual":true,"first":24}')
# k = "https://www.instagram.com/graphql/query/?query_hash=56066f031e6239f35a904ac20c9f37d9&variables="+t
# p = urllib.request.urlopen(k).read()
# JSON_object = json.loads(p.decode('utf-8'))
# print(JSON_object)

# k = "https://www.instagram.com/dubaihoteloffer"
# t = k[len("https://www.instagram.com/"):]
# print(str(t))

# import os
# os.remove("gwalior.json")

import json 
with open("dubaihotelsguide1.json","r+") as f:
	js = json.load(f)
	for i in range(24):
		print(len(js["data"]["user"]["edge_followed_by"]["edges"]))