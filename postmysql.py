import pymysql
import json
file = 'dubaihotelsguidepost.json'
instausername = '"'+str(file.split('.')[0])+'"'
with open(file,"r+") as f:
	js = json.load(f)
	for i in range(len(js)):
		for j in range(len(js[i])):
			k1 = '"'+str(js[i][j]["url"])+'"'
			k2 = '"'+str(js[i][j]["shortcode"])+'"'
			k3 = '"'+str(js[i][j]["likes"])+'"'
			k4 = '"'+str(js[i][j]["comments"])+'"'
			db = pymysql.connect("localhost","root","testbot123456","insta1" )
			cursor = db.cursor()
			sql = "INSERT INTO postdata (username,img_url,img_shortcode,img_likes,img_comments_no) VALUES ("+"{}".format(instausername)+","+"{}".format(k1)+","+"{}".format(k2)+","+"{}".format(k3)+","+"{}".format(k4)+")"
			try:
				cursor.execute(sql)
				db.commit()
			except:
	 			db.rollback()
			db.close()