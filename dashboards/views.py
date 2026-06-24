from django.shortcuts import get_object_or_404, render, redirect
from blogs.models import Category, Blog
from django.contrib.auth.decorators import login_required

from .forms import CategoryForm, BlogForm
from django.template.defaultfilters import slugify


@login_required(login_url='login')
def dashboard(request):
    category_count = Category.objects.all().count()
    blogs_count = Blog.objects.all().count()
    context = {
        'category_count' : category_count,
        'blogs_count' : blogs_count
    }
    return render(request, "dashboard/dashboard.html", context=context)

def categories(request):
    return render(request, 'dashboard/categories.html')

def posts(request):
    return render(request, "dashboard/posts.html")

def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categories')
        
    form = CategoryForm()
    context = {
        'form' : form
    }
    return render(request, 'dashboard/add_category.html', context=context)


def edit_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('categories')
    
    form = CategoryForm(instance=category)
    context = {
        'form' : form,
        'category' : category
    }
    return render(request, 'dashboard/edit_category.html', context=context)


def delete_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    category.delete()
    return redirect('categories')



def posts(request):
    all_posts = Blog.objects.all()
    context = {
        'posts' : all_posts
    }
    return render(request, 'dashboard/posts.html', context=context)


def add_posts(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        
        if form.is_valid():
            post = form.save(commit=False)  # temporary save and returns object, now we can add custom data
            post.author = request.user
            post.save()
            title = form.cleaned_data['title']
            post.slug = slugify(title) + '-' + str(post.id)  # new post can be repeated so to avoid this we use pk at end of the slug
            post.save()
            return redirect('posts')
        else:
            print("Form Invalid")
            print(form.errors)
    form = BlogForm()
    context = {
        'form' : form
    }
    return render(request, 'dashboard/add_posts.html', context)


def edit_posts(request, pk):
    post = get_object_or_404(Blog, pk=pk)
    
    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save()
            title = form.cleaned_data['title']
            post.slug = slugify(title) + '-' + str(post.id)
            post.save()
            return redirect('posts')
    form = BlogForm(instance=post)
    context = {
        'form' : form,
        'post' : post
    }
    
    return render(request, 'dashboard/edit_posts.html', context=context)


def delete_posts(reuqest, pk):
    post = get_object_or_404(Blog , pk=pk)
    post.delete()
    return redirect('posts')