from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import RegistrationForm
from .models import RegistrationData
#from django.contrib.auth.form import AuthenticationForm


# Create your views here.
def index(request):
    return render(request, "Yatri/home.html") 

def SignUp(request):
     context= {"form":RegistrationForm} 
     return render(request,"Yatri/register.html",context)

def addUser(request):
      form=RegistrationForm(request.POST)
      if form.is_valid():
            register=RegistrationData(username=form.cleaned_data['username'],
                                      password=form.cleaned_data['password'],
                                      email=form.cleaned_data['email'],
                                      phone=form.cleaned_data['phone'],)
            
            register.save()
           

      return redirect('index')   

	#		form.redirect ('/akash')
      #  else:
     #       form=UserCreationForm()
     #       args={'form':form}
     #       return render(request,"Yatri/register.html",args)   
    

          

