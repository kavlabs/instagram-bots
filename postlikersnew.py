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
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
import json
import os
import random
import threading
from queue import Queue

hashtags = "https://www.instagram.com/explore/tags/"
usernames = "https://www.instagram.com/"
query_hash = "e0f59e4a1c8d78d0161873bc2ee7ec44"
usernames_1 = ['testbotinstagram2010112@next2cloud.info','kaustubh.job999@gmail.com','appdevcorp999@gmail.com','dimarozoh@22office.com','hisujuzi@utoo.email','botinstagram20@onecitymail.com','testbotinstagram201@next2cloud.info','testbotinstagram2010@next2cloud.info','testbotinstagram20101@next2cloud.info','testbotinstagram201011@next2cloud.info']
passwords_1 = ['zxcvnm12345','12345zxcvnm','zxcvnm12345','zxcvnm12345','zxcvnm12345','zxcvnm12345','zxcvnm12345','zxcvnm12345','zxcvnm12345','zxcvnm12345']

def urlencode(str):
  return urllib.parse.quote(str)

def urldecode(str):
  return urllib.parse.unquote(str)

c = 'accounts/login/'
class insta:
	def user_bot(self,k):
		url_main = usernames + c + 'ajax/'
		identity = ''
		after = ''

		with requests.Session() as s:
		    kk2 = "{}".format(str(k))+".json"
		    l = ''
		    l1 = ''
		    try:
		    	i = 0
		    	auth = {'username': usernames_1[i%10], 'password': passwords_1[i%10]}
		    	headers = {'referer': "https://www.instagram.com/accounts/login/"}
		    	req = s.get(url_main)
		    	headers['x-csrftoken'] = req.cookies['csrftoken']
		    	s.post(url_main, data=auth, headers=headers)
		    	while True:
		    		m = []
		    		if i%1000==0 and i!=0:
		    			print('evading rate limit')
		    			time.sleep(900)
		    		if i%100==0 and i!=0:
		    			auth = {'username': usernames_1[i%10], 'password': passwords_1[i%10]}
		    			headers = {'referer': "https://www.instagram.com/accounts/login/"}
		    			req = s.get(url_main)
		    			headers['x-csrftoken'] = req.cookies['csrftoken']
		    			s.post(url_main, data=auth, headers=headers)
		    		if i==0:
		    			t = urlencode('{"shortcode":'+'"{0}"'.format(k)+',"include_reel":true,"first":50}')
		    			newurl = "https://www.instagram.com/graphql/query/?query_hash="+query_hash+"&variables="+t
		    			p = s.get(newurl)
		    			print(p.status_code)
		    			tt = "{}".format(str(k))+"{}".format(i+1)+".json"
		    			with open(tt,'a+') as file:
		    				json.dump(json.loads(p.content.decode('utf-8')),file)
		    			with open(tt,"r+") as f:
		    				js = json.load(f)
		    				# print(js)
		    				for j in range(len(js["data"]["shortcode_media"]['edge_liked_by']['edges'])):
		    					username = js["data"]["shortcode_media"]['edge_liked_by']['edges'][j]['node']['username']
		    					t = {"username":username}
		    					m.append(t)
		    				with open(kk2,"a+") as file:
		    					json.dump(m,file)
		    					print('done')
		    					# time.sleep(4)

		    		else:
		    			tt = "{}".format(str(k))+"{}".format(i)+".json"
		    			with open(tt,'r+') as file:
		    				data = json.load(file)
		    				after = data['data']['user']['edge_followed_by']['page_info']['end_cursor']
		    				print(after)
		    			t = urlencode('{"shortcode":'+'"{0}"'.format(k)+',"include_reel":true,"first":50,"after":'+'"{}"'.format(after)+'}')
		    			p = s.get("https://www.instagram.com/graphql/query/?query_hash="+query_hash+"&variables="+t)
		    			tt1 = "{}".format(str(k))+"{}".format(i+1)+".json"
		    			l = tt1
		    			l1 = tt
		    			with open(tt1,'a+') as file:
		    				json.dump(json.loads(p.content.decode('utf-8')),file)
		    			with open(tt1,"r+") as f:
		    				js = json.load(f)
		    				# print(js)
		    				for j in range(len(js["data"]["shortcode_media"]['edge_liked_by']['edges'])):
		    					username = js["data"]["shortcode_media"]['edge_liked_by']['edges'][j]['node']['username']
		    					t = {"username":username}
		    					m.append(t)
		    				with open(kk2,"a+") as file:
		    					json.dump(m,file)
		    					print('done')
		    					# time.sleep(4)
		    			os.remove(tt)
		    		i += 1

		    except Exception as e:
		    	print(e)
		    	time.sleep(900)
		    	try: 
		    		os.remove(l)
		    	except:
		    		pass
		    	try:
		    		os.remove(l1)
		    	except:
		    		pass
		    	# os.remove(l1)

k = []
filename = ''
for file in os.listdir(r"C:\Users\Administrator\Desktop\hotel\post"):
    if file.endswith(".json"):
        filename = str(os.path.join(r"C:\Users\Administrator\Desktop\hotel\post", file))
        with open(filename,'r+') as f:
        	t = json.load(f)
        	for i in range(len(t)):
        		for j in range(len(t[i])):
        			k.append(t[i][j]['shortcode'])
for i in range(len(k)):
	kk = k[i]
	q = insta()
	q.user_bot(kk)
