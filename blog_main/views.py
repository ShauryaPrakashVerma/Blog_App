from django.http import HttpResponse
from django.shortcuts import render
from extras.models import About, Link

from blogs.models import Blog, Category

def home(request):
    featured_posts = Blog.objects.filter(is_featured = True, status="Published")
    posts = Blog.objects.filter(is_featured = False, status = 'Published')
    
     # Fetch about us
    try:
        about = About.objects.first()
    except:
        about = None
    
    context ={
        'featured_posts' : featured_posts,
        'posts' : posts,
        'about' : about,
    }
    return render(request, 'home.html', context)