from django.shortcuts import render
from posts.models import Posts, Category
from marketing.models import SignUp

def index(request):
    posts = Posts.objects.filter(featured = True)
    latest = Posts.objects.order_by('upload_date')[0:3]
    if request.method == "POST":
        email = request.POST.get("email")
        new_signup = SignUp()
        new_signup.email = email
        new_signup.save()
    contex = {
        "posts" : posts,
        "latest" : latest
    }
    return render(request,'index.html', contex)
    
def blog(request):
    return render(request,'blog.html',{})

def post(request):
    return render(request,'post.html',{})
