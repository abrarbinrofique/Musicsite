from django.shortcuts import render,redirect

from musician.forms import musician_form

from musician.models import Musician
# Create your views here.

def add_musician(request):
    if request.method=='POST':
        print("post method")

        form=musician_form(request.POST)
        if form.is_valid():
             print("valid")
             form.save()
           

        else:
              print("not valid")
    else:
        form=musician_form()

        print("get method")

    return render(request,'musican.html',{'form':form})







def edit_musician(request,id):
    poster=Musician.objects.get(pk=id)
    musicianform=musician_form(instance=poster)
    

    if request.method=='POST':

        form=musician_form(request.POST,instance=poster)
        if form.is_valid():
          form.save()
          print('valid')
          return redirect ('home')
        
    return render(request,'musican.html',{'form': musicianform})



   