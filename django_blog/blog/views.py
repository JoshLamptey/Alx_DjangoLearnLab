from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def register(request):
    if request.POST =='POST':
        form = UserCreationForm()
        if form.is_valid():
            form.save()
        messages.success(request, 'Account created successfully ')
    else:
     form = UserCreationForm()
     context = {
        'form' : form
     }   
     return render(request,'register.html', context)