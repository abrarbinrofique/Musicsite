from django.shortcuts import render,redirect

from album.forms import  album_form

from album.models import Album

# Create your views here.
def add_album(request):
    if request.method=='POST':
        form=album_form(request.POST)
        form.is_valid()
        form.save()
        print(form.cleaned_data)
    else:
        form=album_form()


    
    return render (request,'albums.html',{'form':form})



def edit_album(request,id):
    poster=Album.objects.get(pk=id)
    former=album_form(instance=poster)
    if request.method=='POST':
        form=album_form(request.POST,instance=poster)
        form.is_valid()
        form.save()
        print(form.cleaned_data)
        return redirect('home')
  

    
    return render (request,'albums.html',{'form':former})




def delete_album(request,id):
    Album.objects.get(pk=id).delete()
    return redirect('home')


    
   