from django.shortcuts import render
from .forms import Enter
from .models import reg,log
import os
import re
from django.core.files.storage import FileSystemStorage
fs = FileSystemStorage()
# Create your views here.
def one(request):
	b=Enter()
	if request.method=="POST":
		b=Enter(request.POST,request.FILES)
		if b.is_valid():
			b.save()	
			obj=reg.objects.last()
			#saving to file
			f= open(obj.Choose_file.path,"w+")
			f.write(obj.Value)
			f.close()
			#entering the content into log
			a=log.objects.create(fk=obj,created_update="Created",new_value=obj.Value)
			a.save()
			b=Enter()
	return render(request,'one.html',{'a':b})
def get(request):
	b=Enter()
	print("enteres")
	if request.method=="POST" and request.is_ajax():
		#getting primary key to update
		pk=request.POST.get('a')
		#the value to be updated
		value=request.POST.get('b')
		#openning the filw
		v=reg.objects.get(pk=pk)
		new_value=value
		#reading old values
		f=open(v.Choose_file.path, "r+")
		old_value=f.read()
		#writting new values
		f1=open(v.Choose_file.path, "w+") 
		f1.write(str(value))
		f1.close()
		#entering into log
		LOG=log.objects.create(fk=v,created_update="updated",old_value=old_value,new_value=new_value,file_updated=True)
		LOG.save()

#
		print("success")
		return render(request,'one.html',{'a':b})
def edit(request):
	op=""
	a=""
	#getting the file to edited
	if "edit" in request.POST:
		a=request.POST.get('pk')
		File=reg.objects.get(pk=a)
		b=File.Choose_file.path
		print(b)
		f = open(b, "r")
		op=f.read()
		return render(request,'two.html',{'o':op,"hid":a})

		#saving the edit
	elif "done" in request.POST and request.method=="POST":
		#gettin the value of edits
		get=request.POST.get('input')
		
		hid=request.POST.get('hidden')
		File=reg.objects.get(pk=eval(hid))
		#opening the file 
		f=open(File.Choose_file.path, "r+")
		old_value=f.read()
		#writting the new values
		with open( File.Choose_file.path,'w+') as f1:
		       for line in get.split('\n'):
		                print(line,"s")
		                f1.write(line)

		

	   #entering the content to log
		LOG=log.objects.create(fk=File,created_update="updated",old_value=old_value,new_value=get,file_updated=True)
		a=""
		return render(request,'two.html',{'o':op,"hid":a})
	return render(request,'two.html',{'o':op,"hid":a})

def dash(request):
	LOG=log.objects.all()
	return render(request,"dash.html",{"log":LOG})