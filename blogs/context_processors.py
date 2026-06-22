from extras.models import Link

from .models import Category


def get_categories(request):
    categories = Category.objects.all()
    return dict(categories = categories)


def get_links(request):
    links = Link.objects.all()
    return dict(links = links)

