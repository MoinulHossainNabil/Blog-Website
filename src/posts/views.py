from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from posts.models import Posts, Category, Author, Comments, PostViewCount
from marketing.models import SignUp
from django.db.models import Count, Q
from .forms import PostForm
from django.urls import reverse

def count_category():
    total_category = Posts.objects.values('category__category_name').annotate(Count('category'))
    return total_category

def search_for_post(request):
    post = Posts.objects.all()
    searchkey = request.GET.get('q')
    if searchkey:
        post = post.filter(
            Q(title__icontains = searchkey) |
            Q(body__icontains = searchkey)
        ).distinct()
    return render(request, 'searched_post.html', {"post" : post})

def get_author(user):
    author = Author.objects.filter(author=user)
    if author.exists():
        return author[0]
    return None


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
    total_category = count_category()
    posts = Posts.objects.all()
    latest = Posts.objects.order_by('upload_date')[:3]
    paginator = Paginator(posts, 2)
    page = request.GET.get('page')
    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)


    contex = {
        "queryset" : paginated_queryset,
        "latest" : latest,
        "total_category" : total_category
    }
    print(total_category)
    return render(request,'blog.html', contex)
#@login_required
def post(request, id):
    total_category = count_category()
    latest = Posts.objects.order_by('upload_date')[:3]
    posts = get_object_or_404(Posts, pk = id)
    if request.user.is_authenticated:
        author = get_author(request.user)
        PostViewCount.objects.get_or_create(user = author, post=posts)
    #form = CommentForm(request.POST or None)
    if request.method == "POST":
        con = request.GET.get('comment')
        comment = Comments()
        comment.user = request.user
        comment.post = posts
        comment.content = con
        comment.save()
    contex = {
        "posts" : posts,
        "latest" : latest,
        "total_category" : total_category,
        # "form" : form
    }
    return render(request,'post.html', contex)

def post_create(request):
    title = "Create"
    form = PostForm(request.POST or None, request.FILES or None)
    author = get_author(request.user)
    if request.method == 'POST':
        if form.is_valid():
            form.instance.post_aurhor = author
            form.save()
            return redirect(reverse(
                "post_details", kwargs={
                    "id": form.instance.id
                }
            ))
    context = {
        "title": title,
        "form": form
    }
    return render(request, "post_create.html", context)

def post_update(request, id):
    title = "Update"
    post = get_object_or_404(Posts, id=id)
    author = get_author(request.user)
    form = PostForm(request.POST or None, request.FILES or None, instance=post)
    if request.method ==  "POST":
        if form.is_valid():
            form.instance.post_aurhor = author
            form.save()
            return redirect(reverse(
                "post_details", kwargs={
                    "id": form.instance.id
                }
            ))
    context = {
        "title": title,
        "form": form
    }
    return render(request, "post_create.html", context)

def post_delete(request, id):
    post = get_object_or_404(Posts, id=id)
    post.delete()
    return redirect(reverse("blog_details"))

def get_post(request, id):
    pass

