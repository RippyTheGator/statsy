from django.shortcuts import render
from .models import Update


def home_posts(request):
    context = Update.objects.all().order_by("-update_published")[:5]
    return render(request, 'blog/home.html', {"context": context})
