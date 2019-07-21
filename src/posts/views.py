from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
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
    posts = Posts.objects.all()
    latest = Posts.objects.order_by('upload_date')[:3]
    paginator = Paginator(posts, 1)
    page = request.GET.get('page')
    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)


    contex = {
        "queryset" : paginated_queryset,
        "latest" : latest
    }
    return render(request,'blog.html', contex)

def post(request, id):
    return render(request,'post.html',{})
