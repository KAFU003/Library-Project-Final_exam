from django.shortcuts import render, get_object_or_404
from mysite.models import Post, Episode
from datetime import datetime
from django.shortcuts import redirect, HttpResponse
from .filters import BookFilter
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.
def change_theme(request, **kwargs):
    if 'is_dark_theme' in request.session:
        request.session["is_dark_theme"] = not request.session.get('is_dark_theme')
    else:
        request.session["is_dark_theme"] = True
    return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))

def homepage(request):
    posts = Post.objects.all()
    now = datetime.now()
    return render(request, 'index.html', {'posts': posts})

def intro(request, post_slug):
    post = get_object_or_404(Post, slug=post_slug)
    episodes = Episode.objects.filter(post=post)
    return render(request, 'intro.html', {'post': post, 'episodes': episodes})

def showepisode(request, episode_id):
    episode = get_object_or_404(Episode, id=episode_id)
    return render(request, 'post.html', {'episode': episode})

def filter(request):
    book = Post.objects.all()
 
    bookFilter = BookFilter(queryset=book)
 
    if request.method == "POST":
        bookFilter = BookFilter(request.POST, queryset=book)
 
    context = {
        'bookFilter': bookFilter
    }
 
    return render(request, 'filter.html', context)

@login_required(login_url = '/user_login')
def profile(request):
    return render(request, "profile.html")

@login_required(login_url = '/user_login')
def edit_profile(request):
    u = User.objects.get(id=request.user.id)
    if request.method == "POST":
        email = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']

        u.email = email
        u.first_name = first_name
        u.last_name = last_name

        if 'image' in request.FILES:
            u.image = request.FILES['image']

        u.save()
        alert = True
        return render(request, "edit_profile.html", {'alert':alert})
    return render(request, "edit_profile.html")

@login_required(login_url = '/user_login')
def edit_account(request):

    if request.method == "POST":
        current_password = request.POST['current_password']
        new_password = request.POST['new_password']
        try:
            u = User.objects.get(id=request.user.id)
            if u.check_password(current_password):
                u.set_password(new_password)
                u.save()
                alert = True
                return render(request, "edit_account.html", {'alert':alert})
            else:
                currpasswrong = True
                return render(request, "edit_account.html", {'currpasswrong':currpasswrong})
        except:
            pass
    return render(request, "edit_account.html")

def user_registration(request):
    if request.method == "POST":
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password != confirm_password:
            passnotmatch = True
            return render(request, "student_registration.html", {'passnotmatch':passnotmatch})

        user = User.objects.create_user(username=username, email=email, password=password,first_name=first_name, last_name=last_name)
        user.save()
        alert = True
        return render(request, "user_registration.html", {'alert':alert})
    return render(request, "user_registration.html")

def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            if request.user.is_superuser:
                return HttpResponse("你不是使用者，是管理員!!")
            else:
                return redirect("/profile")
        else:
            alert = True
            return render(request, "user_login.html", {'alert':alert})
    return render(request, "user_login.html")


'''
def homepage(request):
    posts = Post.objects.all() #select * from post
    post_lists = list()
    for counter, post in enumerate(posts):
        post_lists.append(f'No. {counter}-{post} <br>')
    return HttpResponse(post_lists)
'''