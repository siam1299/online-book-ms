from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm


from django.contrib.auth.models import auth 
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required 


from . forms import CreateUserForm, LoginForm

from django.contrib.auth.models import User
# Create your views here.

def home(request):
  return render(request, 'home.html')



def signup(request):

  form = CreateUserForm()

  if request.method == 'POST':
    form = CreateUserForm(request.POST)

    if form.is_valid():
      form.save()
      return redirect('login')


  return render(request, 'signup.html', {'signupform':form})



def user_login(request):

  form = LoginForm()

  if request.method == 'POST':
    form =  LoginForm(request, data=request.POST)

    if form.is_valid():

      username = request.POST.get('username')
      password = request.POST.get('password')

      user = authenticate(request, username=username, password=password)

      if user is not None:

        auth.login(request, user)

        return redirect('profile', pk=user.pk)


  return render(request, 'login.html', {'loginform':form})
  

def logout(request):
  auth.logout(request)
  return redirect('home')

@login_required(login_url = 'login')
def profile(request, pk):
  user = User.objects.get(id=pk)
  return  render(request, 'profile.html', {'user':user})


# def signup(request):

#   if request.method == 'POST':
#     form = UserCreationForm(request.POST)
#     if form.is_valid():
#       user = form.save()
#       login(request, user)
#       return redirect('home')

#   else:
#     form = UserCreationForm()
#   return render(request, 'signup.html', {'form':form})