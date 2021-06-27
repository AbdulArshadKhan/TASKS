from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import info


def register(req):
	if req.method=='POST':
		i1=info(name=req.POST['name'],pno=req.POST['phone-number'])
		i1.save()
		return render(req,'success.html',{'data':i1})
	return render(req,'base.html')

def details(req):
	obj=info.objects.all()
	return render(req,'details.html',{'data':obj})


def view(req,uid):
	obj=info.objects.get(id=uid)
	return HttpResponse(" Your Name is {} and Your Phone Number is {}".format(obj.name,obj.pno))


def update(req,uid):
	obj=info.objects.get(id=uid)

	if req.method=='POST':
		obj.name=req.POST['name']
		obj.pno=req.POST['pno']
		obj.save()
		return redirect('details')

	return render(req,'update.html',{'data':obj})


def delete(req,uid):
	obj=info.objects.get(id=uid)
	obj.delete()
	return redirect('details')