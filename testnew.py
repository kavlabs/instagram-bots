# import requests
# with requests.Session() as s:
# 	req = s.get("https://api.ipify.org",proxies={'https':'https://94.18.214.122:3128'})
# 	print(req.text)
# t = []
# with open('Proxy List.txt','r+') as f:
# 	for i in f.readlines():
# 		# t.append(str(i).strip("\n"))
# 		print(i)
# import requests
# with requests.Session() as s:
# 	req = s.get("https://api.ipify.org",proxies={'https':'https://1.10.186.250:45307'})
# 	print(req.text)
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
for file in os.listdir(r"C:\Users\Administrator\Desktop\hotel"):
    if file.endswith(".json"):
        filename = str(os.path.join(r"C:\Users\Administrator\Desktop\hotel", file))
hashtags = "https://www.instagram.com/explore/tags/"
usernames = "https://www.instagram.com/"
query_hash = "56066f031e6239f35a904ac20c9f37d9"
#proxies = ['94.240.46.195:23500', '94.247.241.70:53640', '94.79.54.25:3128', '94.253.15.25:61934', '94.74.64.60:49948', '94.242.57.136:1448', '94.242.57.136:10010', '94.70.251.201:8080', '92.51.30.1:8080', '95.105.15.91:8080', '95.104.115.182:33409', '95.0.226.84:56697', '93.185.74.242:36714', '95.111.124.24:60327', '95.105.6.113:53281', '94.45.81.65:42033', '93.126.225.34:8080', '94.41.45.159:53281', '94.177.250.87:3128', '94.45.205.53:8080', '93.87.41.9:43711', '94.254.19.237:58661', '94.62.101.200:8080', '95.131.91.130:33624', '94.158.165.19:45915', '94.75.125.119:8080', '95.140.19.34:53839', '91.222.92.161:53281', '95.137.240.30:55531', '94.24.249.234:59316', '94.45.51.170:34119', '95.140.27.135:33876', '95.107.6.252:30185', '94.45.49.170:8080', '95.107.161.210:51875', '92.38.45.96:55314', '94.18.214.122:8080', '95.130.35.88:33015', '93.190.231.167:39449', '95.135.142.198:8080', '95.154.177.181:36383', '94.240.46.82:51043', '95.140.21.66:53281', '95.158.141.129:57841', '95.158.63.46:48913', '95.129.149.79:50439', '95.141.132.138:47131', '94.187.28.96:8080', '94.180.249.78:50852', '94.18.214.122:3128', '95.161.146.86:8080', '95.154.73.122:37603', '95.0.194.241:9090', '93.43.75.194:39355', '95.161.188.246:45248', '95.154.159.119:44242', '95.143.220.5:45939', '94.75.76.10:8080', '94.73.217.125:40858', '94.45.131.213:32070', '94.43.142.190:58365', '94.18.214.122:443', '95.165.182.18:38950', '95.156.102.34:46583', '94.158.224.150:54820', '92.38.44.182:58436', '95.168.96.42:58414', '92.38.45.68:30907', '95.167.123.54:58664', '95.165.203.222:33805', '95.165.222.90:60776', '94.244.44.67:51312', '94.124.109.115:44100', '95.170.130.46:32722', '95.137.246.232:38787', '94.23.218.85:80', '95.154.72.12:32641', '95.111.134.122:32345', '95.170.220.9:47985', '95.154.70.152:38828', '95.167.241.242:49636', '95.158.6.243:46399', '95.161.181.30:59277', '95.172.58.233:59338', '95.165.131.204:45848', '95.170.113.165:43364', '95.170.202.197:36551', '95.179.162.10:3128', '94.140.253.57:8888', '95.179.171.49:3128', '95.165.172.90:60496', '95.171.198.206:8080', '95.172.52.230:35989', '95.160.17.142:40472', '94.20.21.37:3128', '95.169.95.242:53803', '95.140.19.9:8080', '94.253.14.187:55045', '89.40.115.231:8080', '95.158.44.148:57093', '95.181.37.114:57984', '95.111.131.246:40406', '95.130.10.11:8080', '95.170.203.115:8080', '95.154.82.254:52484', '95.171.1.92:35956', '93.171.241.18:45781', '94.189.138.101:42401', '95.29.102.123:60724', '95.31.130.96:38796', '95.158.62.112:44226', '95.181.130.149:35689', '95.31.245.50:31861', '95.31.3.7:8085', '95.140.30.148:40234', '95.161.9.41:48624', '95.161.189.26:61522', '95.31.197.77:41651', '89.40.115.231:3128', '95.173.194.51:53281', '95.31.90.191:53281', '95.154.137.66:41258', '95.161.157.227:43170', '95.31.252.16:43077', '95.37.196.6:53281', '95.31.32.102:34233', '95.158.47.79:52761', '95.107.9.76:8080', '95.47.1.208:30323', '95.137.240.3:35632', '95.31.4.125:38309', '95.174.125.34:53281', '94.243.140.162:40960', '95.47.116.93:58865', '95.181.56.178:39144', '95.158.40.131:51739', '95.159.106.19:8080', '95.67.100.105:42675', '94.24.233.54:35233', '95.65.1.200:58768', '95.188.74.194:57122', '95.65.73.200:51665', '94.253.15.130:34948', '95.47.116.73:8080', '95.67.45.234:8080', '94.247.62.165:33176', '95.47.116.129:31078', '93.170.135.97:52095', '95.47.212.118:36638', '95.31.2.199:33632', '95.78.160.156:52686', '95.78.177.232:8080', '95.31.1.50:53847', '95.143.220.230:8888', '91.230.154.219:34957', '95.66.140.121:59078', '91.82.255.241:47456', '95.78.120.208:46597', '94.21.118.140:46215', '95.78.245.148:38378', '95.78.228.55:52663', '95.79.54.143:8080', '95.66.142.18:38580', '95.67.114.222:60748', '95.64.253.177:30002', '95.46.140.154:53281', '94.153.223.210:53469', '95.79.36.55:44861', '95.154.73.153:58411', '94.24.233.74:32231', '95.79.28.168:53491', '95.73.62.13:32185', '95.31.5.37:52820', '95.85.50.218:80', '95.47.180.171:53484', '95.158.62.178:51332', '95.80.253.11:60377', '95.80.93.53:37317', '95.84.168.158:58007', '95.84.154.73:57423', '95.210.2.206:55956', '95.175.14.25:8080', '94.153.224.194:58713', '95.188.68.19:30708', '95.79.28.66:58044', '94.240.17.56:36127', '95.87.127.133:37570', '95.67.67.54:53281', '96.87.184.101:43705', '95.47.209.206:54956', '95.84.190.160:37458', '95.48.172.34:51581', '95.175.14.113:8080', '96.80.89.69:8080', '95.47.116.184:60722', '95.175.14.57:8080', '95.79.57.206:53281', '94.26.59.151:53544', '95.210.191.156:59802', '96.30.68.154:8080', '89.207.111.88:41258', '95.67.47.94:53281', '95.42.209.122:39115', '96.9.73.80:39476', '95.80.98.41:8080', '95.84.198.24:51251', '95.80.252.189:52371', '96.9.69.133:50693', '95.82.255.90:42411', '95.87.14.3:34731', '95.87.31.76:51302', '96.9.77.243:8080', '96.9.73.79:44636', '95.80.254.162:53295', '95.80.65.39:43555', '96.9.79.173:38559', '96.9.80.62:31353', '96.9.82.78:38675', '96.9.87.2:8080', '98.190.241.3:59800', '95.71.125.50:49882', '94.154.85.214:8080', '96.9.74.160:38857', '95.9.113.12:52566', '95.80.93.44:41258', '96.9.88.49:39566', '96.9.87.54:33119', '96.9.90.76:39927', '96.9.88.54:33666', '96.9.90.83:45750', '96.9.91.24:59082', '92.222.83.160:80', '96.74.27.161:32784', '96.9.86.70:31728', '96.84.91.82:46916', '95.88.251.241:3128', '96.9.77.89:53281', '95.60.152.139:37995', '98.100.194.171:8080', '95.87.234.190:37342', '95.174.101.64:43954', '94.141.142.23:41258', '95.80.252.122:31898', '96.95.42.201:55252', '99.100.78.207:8080', '98.0.162.70:46282', '95.189.78.2:46184', '96.66.103.123:8080', '95.43.182.13:33651', '96.9.91.27:53523', '95.80.254.119:36097', '95.79.55.196:53281', '94.136.157.73:40201', '96.94.89.157:53281', '95.87.14.47:45522', '95.45.235.178:40056', '81.174.11.227:59455', '96.9.88.47:41901', '95.189.112.214:35508', '95.68.242.38:55255', '92.38.45.102:56712', '95.158.137.254:57477', '95.67.19.3:53281', '95.6.79.2:44438', '96.9.69.230:53281', '96.88.30.253:50673', '95.213.155.28:3128', '95.213.155.29:3128', '95.47.212.44:58042', '95.154.104.39:43687', '95.31.4.100:4550', '94.21.151.191:37560', '95.173.236.118:32426', '95.164.74.27:32231', '95.153.48.2:37490', '94.24.233.70:57800', '98.102.88.158:8080', '98.172.141.125:8080', '95.181.49.154:53637', '95.161.231.10:32189', '94.141.142.106:41258', '93.179.209.216:57520', '95.9.150.33:58204', '95.180.225.7:8080', '95.170.208.250:8080', '95.181.145.93:59503', '85.187.235.137:53412', '98.30.106.254:60942', '95.79.99.148:3128', '83.18.178.186:8080', '97.74.198.168:8080', '95.158.40.181:42135', '82.146.45.193:8888', '98.190.18.187:43162', '94.177.132.6:8080', '97.72.93.26:87', '95.167.20.77:32231', '95.167.20.76:32231', '95.215.95.126:49281', '95.154.73.185:21776', '95.133.186.234:39573', '96.9.69.164:53281', '95.87.38.9:47832', '94.242.58.142:1448', '94.242.58.142:10010', '97.73.190.2:87', '95.215.44.67:3128']

# proxy = ''
# for i in range(len(proxies)):
# 	proxy = proxies[i] + "'" + str(ports) + "'"

usernames_1 = ['testbotforinsta@gmail.com','mike.chanbro@gmail.com','shubhabawa123@gmail.com','kaustubh.job999@gmail.com','appdevcorp999@gmail.com']
passwords_1 = ['testbot123456','zxcvnm12345','zxcvnm12345','12345zxcvnm','zxcvnm12345']

def urlencode(str):
  return urllib.parse.quote(str)

def urldecode(str):
  return urllib.parse.unquote(str)

c = 'accounts/login/'
class insta:
	def user_bot(self,k,b):
		url_main = usernames + c + 'ajax/'
		identity = ''
		after = ''
		#t = random.randint(0,4)
		# auth = {'username': usernames_1[b%5], 'password': passwords_1[b%5]}
		# headers = {'referer': "https://www.instagram.com/accounts/login/"}

		with requests.Session() as s:
		    # req = s.get(url_main)
		    # headers['x-csrftoken'] = req.cookies['csrftoken']
		    # s.post(url_main, data=auth, headers=headers)
		    # identity = ''
		    # after = ''
		    q = k[len("https://www.instagram.com/"):]
		    kk1 = "{}".format(str(q))+".txt"
		    urllib.request.urlretrieve(k, kk1)
		    with open(kk1, encoding="utf8") as file:
		    	for line in file.readlines():
		    		if '"has_requested_viewer":false,"id":' in line:
		    			identity = line[line.index('"has_requested_viewer":false,"id":')+35:line.index('","is_business_account"')]
		    			file.close()
		    			print(identity)
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
##		    		t = random.randint(0,100)
##		    		proxy = str('https://' + proxies[t])
##		    		print(proxy)
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
		    			t = urlencode('{"id":'+'"{0}"'.format(identity)+',"include_reel":true,"fetch_mutual":true,"first":50}')
		    			newurl = "https://www.instagram.com/graphql/query/?query_hash="+query_hash+"&variables="+t
		    			p = s.get(newurl)
		    			print(newurl)
		    			tt = "{}".format(str(q))+"{}".format(i+1)+".json"
		    			with open(tt,'a+') as file:
		    				json.dump(json.loads(p.content.decode('utf-8')),file)
		    				print(json.loads(p.content.decode('utf-8')))
		    			with open(tt,"r+") as f:
		    				js = json.load(f)
		    				# print(js)
		    				if js["data"]["user"]["edge_followed_by"]["count"]>0:
		    					for j in range(len(js["data"]["user"]["edge_followed_by"]["edges"])):
		    						user = js["data"]["user"]["edge_followed_by"]["edges"][j]["node"]["username"]
		    						t = {"username":user}
		    						m.append(t)
		    					with open(kk2,"a+") as file:
		    						json.dump(m,file)
		    						print('done')
		    				else:
		    					pass

		    		else:
		    			tt = "{}".format(str(q))+"{}".format(i)+".json"
		    			with open(tt,'r+') as file:
		    				data = json.load(file)
		    				after = data['data']['user']['edge_followed_by']['page_info']['end_cursor']
		    				print(after)
		    			t = urlencode('{"id":'+'"{0}"'.format(identity)+',"include_reel":true,"fetch_mutual":true,"first":50,"after":'+'"{}"'.format(after)+'}')
		    			p = s.get("https://www.instagram.com/graphql/query/?query_hash="+query_hash+"&variables="+t)
		    			tt1 = "{}".format(str(q))+"{}".format(i+1)+".json"
		    			l = tt1
		    			l1 = tt
		    			with open(tt1,'a+') as file:
		    				json.dump(json.loads(p.content.decode('utf-8')),file)
		    				print(json.loads(p.content.decode('utf-8')))
		    			with open(tt1,"r+") as f:
		    				js = json.load(f)
		    				# print(js)
		    				if js["data"]["user"]["edge_followed_by"]["count"]>0:
		    					for j in range(len(js["data"]["user"]["edge_followed_by"]["edges"])):
		    						user = js["data"]["user"]["edge_followed_by"]["edges"][j]["node"]["username"]
		    						t = {"username":user}
		    						m.append(t)
		    					with open(kk2,"a+") as file:
		    						json.dump(m,file)
		    						print('done')
		    				else:
		    					pass
		    			os.remove(tt)
		    		i += 1

		    except Exception as e:
		    	print(e)
		    	time.sleep(60)
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
		q.user_bot(kk,i)
