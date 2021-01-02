from django.shortcuts import render,HttpResponseRedirect
from .forms import CoursesDetails
from .models import Courses
# Create your views here.

#add data
def add(request):
    if request.method == "POST":
        cd = CoursesDetails(data=request.POST,files=request.FILES)
        if cd.is_valid():
            cd.save()
    else:
        cd = CoursesDetails()
    return render(request,'add.html',{"form":cd})

#show data
def show(request):
    cd = Courses.objects.all()
    return render(request,'show.html',{"Course":cd})

#data update/edit
def update_data(request, id):
    if request.method == 'POST':
        uc = Courses.objects.get(pk=id)
        cd = CoursesDetails(request.POST,instance = uc)
        if cd.is_valid():
            cd.save()
    else:
        uc = Courses.objects.get(pk=id)
        cd = CoursesDetails(instance = uc)
    return render(request,"update.html",{"form":cd})


#delete data
def delete(request,id):
    if request.method == "POST":
        del_cor = Courses.objects.get(pk=id)
        del_cor.delete()
        return HttpResponseRedirect("/show")

