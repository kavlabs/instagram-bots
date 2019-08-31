import pymysql
import json
import os
for file in os.listdir(r"C:\Users\Shashank\Desktop\hotel"):
    if file.endswith(".json"):
        filename = str(os.path.join(r"C:\Users\Shashank\Desktop\hotel", file))
        shortcode = '"'+str(file.split('.')[0])+'"'
        with open(filename,"r+") as f:
        	js = json.load(f)
        	for j in range(len(js[0])):
        		k1 = '"'+str(js[0][j]["username"])+'"'
        		db = pymysql.connect("localhost","root","testbot123456","insta2" )
        		cursor = db.cursor()
        		sql = "INSERT INTO postdata1 (shortcode,username) VALUES ("+"{}".format(shortcode)+","+"{}".format(k1)+")"
        		try:
        			cursor.execute(sql)
        			db.commit()
        		except:
        			db.rollback()
        		db.close()