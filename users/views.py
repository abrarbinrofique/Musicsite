from django.shortcuts import render,redirect

from users.forms import adduser

from django.contrib import messages 

from django.contrib.auth.views import LoginView,LogoutView

from django.urls import reverse_lazy

# Create your views here.
def signup(request):
    if request.method=='POST':
        forms=adduser(request.POST)
        if forms.is_valid():
            forms.save()
            messages.success(request,'you create an acccount successfull!')
            return redirect('login')
    else:
        forms=adduser()
    return render(request,'sign.html',{'form':forms})



class login(LoginView):
    template_name='login.html'
   

    def form_valid(self, form):
        username=form.cleaned_data.get('username')
        messages.success(self.request,f'Welcome mr.{username}')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.success(self.request,'Logged in information incorrect')
        return super().form_invalid(form)
    

    def get_context_data(self, **kwargs) :
        context=super().get_context_data(**kwargs)
        context['type']='Login'
        return context
    
    def get_success_url(self):
        return reverse_lazy('home')
    

class logout(LogoutView):
     def get_success_url(self):
        messages.success(self.request,'Logout successfully')
        return reverse_lazy('login')

       
       
            
  