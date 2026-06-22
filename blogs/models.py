from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    # by default django makes the name plural by adding 's' after the name of the model so 'Category' becomes 'Categorys'
    # This behaviur can be fixed by the Meta class
    class Meta:
        verbose_name_plural = 'Categories'
        
        
    # what should be the category actually be represented as in the admin panel
    def __str__(self):
        return self.category_name
    
    
STATUS_CHOICES = (
    ("Draft", "Draft"),
    ("Published", "Published")
)    

class Blog(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)   # models.CASCADE ensures that if the user is deleted all his posts are also deleted
    featured_image = models.ImageField(upload_to='uploads/%Y/%m/%d')
    short_description = models.TextField(max_length=500)
    blog_body = models.TextField(max_length=2000)
    status = models.CharField(max_length=20 ,choices=STATUS_CHOICES, default="Draft")   # to create a dropdown
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
 
 
 
   