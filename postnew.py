# https://www.instagram.com/graphql/query/?query_hash=e0f59e4a1c8d78d0161873bc2ee7ec44&variables=%7B%22shortcode%22%3A%22BsXxufRlFJt%22%2C%22include_reel%22%3Atrue%2C%22first%22%3A24%7D
# https://www.instagram.com/graphql/query/?query_hash=e6a78c2942f1370ea50e04c9a45ebc44&variables=%7B%22id%22%3A%227720292518%22%2C%22first%22%3A12%2C%22after%22%3A%22QVFCV3pyOW4wM0xzVXBRNXVQVDFoM0FPeHlpWkpzclpsNDNsSFYtSkRKQmNwV0R1d2NwMlVJMG9sdGtqM0pxRzNQYUl2eE96bnhVTkRtWXFHRmlQdE9ENw%3D%3D%22%7D
# https://www.instagram.com/graphql/query/?query_hash=7c16654f22c819fb63d1183034a5162f&variables=%7B%22user_id%22%3A%227720292518%22%2C%22include_chaining%22%3Atrue%2C%22include_reel%22%3Atrue%2C%22include_suggested_users%22%3Afalse%2C%22include_logged_out_extras%22%3Afalse%2C%22include_highlight_reels%22%3Atrue%7D
# posts - https://www.instagram.com/graphql/query/?query_hash=e6a78c2942f1370ea50e04c9a45ebc44&variables=%7B%22id%22%3A%227720292518%22%2C%22first%22%3A12%2C%22after%22%3A%22QVFCSTl5X2IySGpNSG51aExIMllOdThuNENfRTFLTjRxZm02WEhITVRrak9hbHVxck5iM25HdUVvSWFJYlVhWjBOS3ZSZU02Q1o2V1FIRTFxMUxtTG1XMw%3D%3D%22%7D
# img_people_like - https://www.instagram.com/graphql/query/?query_hash=e0f59e4a1c8d78d0161873bc2ee7ec44&variables=%7B%22shortcode%22%3A%22Bsj9KVGFasd%22%2C%22include_reel%22%3Atrue%2C%22first%22%3A24%7D
import urllib.parse
from urllib.request import urlopen
import urllib.request
import time
import requests
import json
import os
import random
filename = ''
for file in os.listdir(r"C:\Users\Shashank\Desktop\hotel"):
    if file.endswith(".json"):
        filename = str(os.path.join(r"C:\Users\Shashank\Desktop\hotel", file))
hashtags = "https://www.instagram.com/explore/tags/"
usernames = "https://www.instagram.com/"
query_hash = "e6a78c2942f1370ea50e04c9a45ebc44"
usernames_1 = ['mike.chanbro@gmail.com','kaustubh.job999@gmail.com','appdevcorp999@gmail.com']
passwords_1 = ['zxcvnm12345','12345zxcvnm','zxcvnm12345']

def urlencode(str):
  return urllib.parse.quote(str)

def urldecode(str):
  return urllib.parse.unquote(str)

c = 'accounts/login/'
class insta:
	def user_bot(self,k):
		identity = ''
		after = ''
		url_main = usernames + c + 'ajax/'

		with requests.Session() as s:
		    q = k[len("https://www.instagram.com/"):]
		    kk1 = "{}".format(str(q))+".txt"
		    urllib.request.urlretrieve(k, kk1)
		    with open(kk1, encoding="utf8") as file:
		    	for line in file.readlines():
		    		if '"has_requested_viewer":false,"id":' in line:
		    			identity = line[line.index('"has_requested_viewer":false,"id":')+35:line.index('","is_business_account"')]
		    			file.close()
		    			os.remove(kk1)
		    kk2 = "{}".format(str(q))+".json"
		    l = ''
		    l1 = ''
		with requests.Session() as s:
		    try:
		    	i = 0
		    	auth = {'username': usernames_1[i%3], 'password': passwords_1[i%3]}
		    	headers = {'referer': "https://www.instagram.com/accounts/login/"}
		    	req = s.get(url_main)
		    	headers['x-csrftoken'] = req.cookies['csrftoken']
		    	s.post(url_main, data=auth, headers=headers)
		    	while True:
		    		proxy = str('http://' + proxies[random.randint(1,100)] + ":" + str(random.randint(1,100)))
		    		print(proxy)
		    		m = []
		    		if i%300==0 and i!=0:
		    			print('evading rate limit')
		    			time.sleep(900)
		    		if i%100==0 and i!=0:
		    			auth = {'username': usernames_1[i%3], 'password': passwords_1[i%3]}
		    			headers = {'referer': "https://www.instagram.com/accounts/login/"}
		    			req = s.get(url_main)
		    			headers['x-csrftoken'] = req.cookies['csrftoken']
		    			s.post(url_main, data=auth, headers=headers)
		    		if i==0:
		    			t = urlencode('{"id":'+'"{0}"'.format(identity)+',"first":50'+'}')
		    			newurl = "https://www.instagram.com/graphql/query/?query_hash="+query_hash+"&variables="+t
		    			p = s.get(newurl)
		    			tt = "{}".format(str(q))+"{}".format(i+1)+".json"
		    			with open(tt,'a+') as file:
		    				json.dump(json.loads(p.content.decode('utf-8')),file)
		    			with open(tt,"r+") as f:
		    				js = json.load(f)
		    				# print(js)
		    				for j in range(len(js["data"]["user"]['edge_owner_to_timeline_media']['edges'])):
		    					url = js["data"]["user"]['edge_owner_to_timeline_media']['edges'][j]['node']['display_url']
		    					shortcode = js["data"]["user"]['edge_owner_to_timeline_media']['edges'][j]['node']['shortcode']
		    					likes = js["data"]["user"]['edge_owner_to_timeline_media']['edges'][j]['node']['edge_media_preview_like']['count']
		    					comments = js["data"]["user"]['edge_owner_to_timeline_media']['edges'][j]['node']['edge_media_to_comment']['count']
		    					t = {"url":url,"shortcode":shortcode,"likes":likes,"comments":comments}
		    					m.append(t)
		    				with open(kk2,"a+") as file:
		    					json.dump(m,file)
		    					print('done')
		    					# time.sleep(4)

		    		else:
		    			tt = "{}".format(str(q))+"{}".format(i)+".json"
		    			with open(tt,'r+') as file:
		    				data = json.load(file)
		    				after = data['data']['user']['edge_followed_by']['page_info']['end_cursor']
		    				print(after)
		    			t = urlencode('{"id":'+'"{0}"'.format(identity)+',"first":12,"after":'+'"{}"'.format(after)+'}')
		    			p = s.get("https://www.instagram.com/graphql/query/?query_hash="+query_hash+"&variables="+t)
		    			tt1 = "{}".format(str(q))+"{}".format(i+1)+".json"
		    			l = tt1
		    			l1 = tt
		    			with open(tt1,'a+') as file:
		    				json.dump(json.loads(p.content.decode('utf-8')),file)
		    			with open(tt1,"r+") as f:
		    				js = json.load(f)
		    				# print(js)
		    				for j in range(len(js["data"]["user"]['edge_owner_to_timeline_media']['edges'])):
		    					url = js["data"]["user"]['edge_owner_to_timeline_media']['edges'][j]['node']['display_url']
		    					shortcode = js["data"]["user"]['edge_owner_to_timeline_media']['edges'][j]['node']['shortcode']
		    					likes = js["data"]["user"]['edge_owner_to_timeline_media']['edges'][j]['node']['edge_media_preview_like']['count']
		    					comments = js["data"]["user"]['edge_owner_to_timeline_media']['edges'][j]['node']['edge_media_to_comment']['count']
		    					t = {"url":url,"shortcode":shortcode,"likes":likes,"comments":comments}
		    					m.append(t)
		    				with open(kk2,"a+") as file:
		    					json.dump(m,file)
		    					print('done')
		    					# time.sleep(4)
		    			os.remove(tt)
		    		i += 1

		    except Exception as e:
		    	print(e)
		    	try: 
		    		os.remove(l)
		    		os.remove(l1)
		    	except:
		    		pass
		    	# os.remove(l1)

k = []
with open(filename,'r+') as f:
	t = json.load(f)
	for i in range(len(t[0])):
		k.append(usernames + t[0][i]["username"])
	for i in range(len(k)):
		kk = k[i]
		q = insta()
		q.user_bot(kk)