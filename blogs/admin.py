from django.contrib import admin
from .models import Category, Blog, Comment

# prepopulated fields for generating slug sutomatically
class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('title',)}
    list_display = ('title', 'category', 'author', 'status', 'is_featured')  # display additional info about the models specified in the tuple
    search_fields = ('id', 'title', 'category__category_name', 'status')  # what all parameters we can seach by, we cannot use a foreign field for search
    
    # to use foreign key as a seach parameter you must tell it which field of the related model to search.  category --> category__category_name

    list_editable = ('is_featured',)  # makes the is_feature option editable from top without opening

# by default the models created are not visible in the admin panel, we have first register the model in the admin.py
admin.site.register(Category)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Comment)

