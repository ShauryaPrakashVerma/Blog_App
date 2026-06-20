from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from .models import Blog, Category

# Create your views here.
def posts_by_category(request, category_id):
    
    # Fetch the posts that belong to the category with the id = category_id
    posts = Blog.objects.filter(status='Published', category = category_id)
    # use try/except when we want to do some custom action if the category does not exist
    
    try:
        category = Category.objects.get(pk = category_id)
    except:
        # redirect to user to home page
        return redirect("home")
    # if the user is looking for a category that doesnt exist we use try catch block or get_object_or_404
    # category = get_object_or_404(Category, pk=category_id)
    
    
   
    
    context = {
        'posts': posts,
        'category' : category
    }
    return render(request, "posts_by_category.html", context)



def blogs(request, slug):
    single_blog = get_object_or_404(Blog, slug=slug, status = "Published")
    context = {
        'single_blog' : single_blog,
    }
    return render(request, 'blogs.html', context)


def search(request):
    return render(request, "search.html")