from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth import authenticate
from . models import Post

# Create your views here.
def index(request):
    return render(request, "index.html")

def login(request):
    if request.method == 'POST': 
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request, 'Invalid credentials')
            return redirect('login')
    else:
        return render(request, "login.html")

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        repassword = request.POST['repassword']

        if password==repassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username taken')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username,password=password)
                user.save()
                print('user created')
                messages.info(request, 'User created')
        else:
            messages.info(request, 'Password is not matching')
            return redirect('signup')
        return redirect('login')

    else:
        return render(request, "signup.html")

def logout(request):
    auth.logout(request)
    return redirect('/')

def word(request):
    return render(request, "word.html")

def tips(request):
    return render(request, "tips.html")

def forum(request):
    post = Post.objects.all()
    context = {
    'post':post
    }

    return render(request,"forum.html",context)

def newdiscuss(request):
    return render(request, "newdiscuss.html")

def addnewdiscuss(request):
    print("form is submitted")
    user = request.user
    judulpost = request.POST["judulpost"]
    isipost = request.POST["isipost"]
    
    post = Post(user=user, judulpost=judulpost, isipost=isipost)
    post.save()
    messages.info(request, 'Post has been made')

    return render(request, "newdiscuss.html")