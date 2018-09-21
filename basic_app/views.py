from django.shortcuts import render
from basic_app.forms import UserForm, UserProfileForm
from PIL._imagingcms import profile_frombytes

from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout


# Create your views here.


def index(request):
    context_dict = {'title':'Hello world', 'number': 100}
    return render(request, 'basic_app/index.html', context_dict)

@login_required
def other(request):
    return render(request, 'basic_app/other.html')

def relative(request):
    return render(request, 'basic_app/relative_url_template.html')

def basic_app_index(request):
    return render(request, 'basic_app/basic_app_index.html')

def register(request):
    registered = False
    
    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)
        
        if user_form.is_valid() and profile_form.is_valid():
            
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            
            userprofile = profile_form.save(commit=False)
            userprofile.user = user
            
            if 'profile_pic' in request.FILES:
                userprofile.profile_pic = request.FILES['profile_pic']
            
            
            userprofile.save()
            
            registered=True
            
        else:
            print(user_form.errors, profile_form.errors)
            
    else:
        user_form = UserForm()
        profile_form = UserProfileForm
        
    return render(request, "basic_app/register.html", {'user_form':user_form, 'profile_form':profile_form, 'registered': registered})
    return render(request, 'basic_app/register.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def user_login(request):
    print(request.method)
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        print(user)
        if user:
            if user.is_active:
                login(request,user)
                print("attempted to log user in")
                return HttpResponseRedirect(reverse('index'))
            
            else:
                print("User not active")
                return HttpResponse("Account Not Active")
        else:
            print("Someone tried to login and failed")
            print("Username: {} and password {}".format(username, password))
            return HttpResponse("Invalid Login Details Supplied")
    
    else:
        print("Wasn't a post from the login page")
        return render(request, 'basic_app/login.html')









