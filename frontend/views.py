from django.shortcuts import render

# Create your views here.

def index(request, *args, **kwargs):
    return render(request, 'frontend/index.html')

def about(request, *args, **kwargs):
    return render(request, 'frontend/aboutus.html')

def blog(request, *args, **kwargs):
    return render(request, 'frontend/blog.html')

def contact(request, *args, **kwargs):
    return render(request, 'frontend/contact-us.html')

def news_event(request, *args, **kwargs):
    return render(request, 'frontend/news-event.html')

def services(request, *args, **kwargs):
    return render(request, 'frontend/services.html')

def manageexpenses(request, *args, **kwargs):
    return render(request, 'frontend/manage-expenses.html')

def wealth(request, *args, **kwargs):
    return render(request, 'frontend/wealth.html')
