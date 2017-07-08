from django.shortcuts import render
from .models import post
from django.utils import timezone

# Create your views here.

def post_list(request):
    posts = post.objects.filter(published_date_lte=timezone.now().order_by('published_date'))
    return render(request, 'blog/post_list.html', {'posts': posts})

