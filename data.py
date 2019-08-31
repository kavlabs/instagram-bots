import json
import random
def same_data():
	m = 'data4.json'
	for i in range(5000):
		if i%2 == 0:
			t = random.randint(1,100)
			# k = "{"+'"input"'+":"+"["+"{}".format(t)+","+"{}".format(t)+","+"{}".format(t)+"]"+","+'"output"'+":"+"{"+'"same"'+":1}"+"}"+","
			k = "{"+'"input"'+":"+"["+"{}".format(t)+","+"{}".format(t)+","+"{}".format(t)+"]"+","+'"output"'+":"+"["+"1"+"]"+"}"+","
			print(k)
			# m = 'same_data.json'
			with open(m,'a+') as file:
				# json.dump(k,file)
				file.write(k)
		else:
			t = random.randint(1,100)
			q = random.randint(1,100)
			r = random.randint(1,100)
			# k = "{"+'"input"'+":"+"["+"{}".format(t)+","+"{}".format(q)+","+"{}".format(r)+"]"+","+'"output"'+":"+"{"+'"different"'+":1}"+"}"+","
			k = "{"+'"input"'+":"+"["+"{}".format(t)+","+"{}".format(q)+","+"{}".format(r)+"]"+","+'"output"'+":"+"["+"0"+"]"+"}"+","
			# m = 'different_data.json'
			with open(m,'a+') as file:
				# json.dump(k,file)
				file.write(k)
			# kk.append(k)
	# print(kk)
same_data()