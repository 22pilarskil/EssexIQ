from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
import smtplib
import os
import getpass

# Create your views here.

def homeView(request):
	 print("HomeView")
	 try:
	 	x = request.GET['submit']
	 	return render(request, 'home.html', {"submitted": True})
	 except KeyError:
	 	return render(request, 'home.html', {"submitted": False})

def sendEmail(request):
	data = request.POST
	email = str(data["username"])
	message = str(data["message"])
	fromaddr = "millburnvexrobotics@gmail.com"
	toaddrs = "millburnvexrobotics@gmail.com"
	username = "millburnvexrobotics@gmail.com"
	password = "millburn123"
	msg = "\nEmail: "+email+", Message: "+message
	print(msg)
	os.chdir("/Users/"+getpass.getuser())
	file = open("messages.txt", 'a+')
	file.write(msg)
	file.close()
	'''
	server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
	server.login(username, password)
	server.sendmail(fromaddr, toaddrs, str(msg))
	server.quit()
	'''
	return HttpResponseRedirect("/?submit=True")
