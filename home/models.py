from django.db import models
import smtplib
import matplotlib.pyplot as plt #plt.rcdefaults()
import numpy as np
import pyrebase
import requests as request

def send_email(username, message):
	fromaddr = "7405nitro@gmail.com"
	toaddrs = "7405nitro@gmail.com"
	msg = "Mailer:"+username+"\n"+"Message"+message
	username = "7405nitro@gmail.com"
	password = "KittyCat123"

	server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
	#server.helo()
	#server.starttls()
	server.login(username, password)
	server.sendmail(fromaddr, toaddrs, msg)
	server.quit()

def set_images():

	config = {
	    "apiKey": "AIzaSyCJhmjij4ABEZrlIP5581ERp9pXcb6anLk",
	    "authDomain": "n-d3a20.firebaseapp.com",
	    "databaseURL": "https://n-d3a20.firebaseio.com",
	    "projectId": "n-d3a20",
	    "storageBucket": "n-d3a20.appspot.com",
	    "messagingSenderId": "626961674461",
	    "appId": "1:626961674461:web:424708683547daae",
	    "serviceAccount": "static/n-d3a20-firebase-adminsdk-4gvqc-7e0b540d4f.json"
	}

	firebase=pyrebase.initialize_app(config)
	auth = firebase.auth()
	user = auth.sign_in_with_email_and_password("liampilarski2@gmail.com", "Liamlukas=11")
	user = auth.refresh(user['refreshToken'])
	db = firebase.database()

	values = {
		"Driver Skills":[],
		"Programming Skills":[],
		"Front-Auton":[],
		"Back-Auton":[],
		"VexDB Data":[]
	}
	keys = []
	filepaths = []
	def get_info(sku):
		payload = {'sku': sku}
		r = request.get('https://api.vexdb.io/v1/get_rankings', params=payload)
		for x in range(r.json()['size']):
			if "7405N" in r.json()['result'][x]['team']:
				team = r.json()['result'][x]
				return {"OPR (Ofensive Power Rating)":team['opr'], "DPR (Defensive Power Rating)":team['dpr'], "CCWM (Calculated Contribution to Winning Margin)":team['ccwm'], "Rank":team['rank']}
	
	data = {
		"2Millburn_12-1-19":
			{
				"Back-Auton":1,
				"Front-Auton":4,
				"Driver Skills":42,
				"Programming Skills":4,
				"VexDB Data":get_info("RE-VRC-19-8669")

			},
		"1Danbury_11-16-19":
			{
				"Back-Auton":1,
				"Front-Auton":1,
				"Driver Skills":30,
				"Programming Skills":1,
				"VexDB Data":get_info("RE-VRC-19-9780")

			},
		"3Sparta_1-11-20":
			{
				"Back-Auton":5,
				"Front-Auton":6,
				"Driver Skills": 80,
				"Programming Skills": 6,
				"VexDB Data":get_info("RE-VRC-19-8355")
			}

	}
	db.child("teamstats").set(data)

	data = db.child("teamstats").get().each()
	x = 1
	while len(keys)<len(data):
		for d in data:
			if int(d.key()[0]) == x:
				keys.append(d.key()[1:])
				x += 1
			for key in values.keys(): values[key].append(d.val()[key])


	for key in values:
		if key=="VexDB Data":
			plt.title(key)
			stat_dict = {
				"Rank":[],
				"OPR (Ofensive Power Rating)":[],
				"DPR (Defensive Power Rating)":[],
				"CCWM (Calculated Contribution to Winning Margin)":[]
			}
			for stat in values[key]:
				for item in stat: stat_dict[item].append(stat[item])
			x = []
			for item in stat_dict:
				plt.plot(keys, stat_dict[item], marker='o', label=stat)
				x.append(item)
			plt.legend(x)
		else:
			plt.title(key)
			plt.plot(keys, values[key], marker='o')
		plt.savefig("static/images/"+key+".png")
		plt.clf()
		filepaths.append("static/images/"+key+".png")
		

	return values

#set_images()


