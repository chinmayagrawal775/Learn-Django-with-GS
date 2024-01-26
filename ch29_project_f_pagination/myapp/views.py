from django.shortcuts import render
from .models import Post
from django.core.paginator import Paginator

# Create your views here.
def home(request):
    posts = Post.objects.all().order_by('id')
    paginator = Paginator(posts, 3, orphans=1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'myapp/home.html', {'posts':page_obj})