from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
	return HttpResponse('Welcome to my Page')

def ht(request):
	return HttpResponse("<h1 style='text-align:center;margin-top:20%'>This is HTML PAGE</h1>")

def par1(request,uname):
	return HttpResponse("<script>alert('Good Morning !')</script><h2 style='text-align:center;margin-top:20%;text-transform:capitalize'>One parameter is used . It is {}</h2>".format(uname))

def ren(request):
	return render(request,'first.html')

def rend(request):
	return render(request,'html/second.html')

def bif(request,name,age):
	return render(request,'html/second.html',{'name':name,'age':age,'min':18,'r':[1,2,3,4,5,6,7]})

def form(request):
	return render(request,'form.html')

def task1(request):
	return render(request,'html/task1.html')

def result(request):
	fname=request.GET['first name']
	lname=request.GET['last name']
	email=request.GET['email']
	pno=request.GET['phone number']
	dob=request.GET['date of birth']
	uname=request.GET['username']
	pwd=request.GET['password']
	gen=request.GET['gender']
	lan=request.GET.getlist('language')
	str1=','.join(lan)
	adr=request.GET['address']

	return render(request,'html/result.html',{
			'fname':fname,
			'lname':lname,
			'email':email,
			'pno':pno,
			'dob':dob,
			'uname':uname,
			'pwd':pwd,
			'gen':gen,
			'lan':str1,
			'adr':adr
		})

# def data(request):
# 	obj=student(name='Abdul',phone='9999988888')
# 	obj.save()
# 	return HttpResponse("{} Created Successfully".format(obj.name))

# def data1(req):
# 	obj1=student.objects.create(name='khan',phone=1111122222)
# 	return HttpResponse("{} Created ".format(obj1.name))
