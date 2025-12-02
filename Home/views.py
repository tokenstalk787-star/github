from django.shortcuts import render, HttpResponse

# Create your views here.
# Home page view
def index(request):
    return render(request, 'index.html')
  #  return HttpResponse("Hello, this is the Home page.")

# About page view
def about(request):
    return render(request, 'about.html')

# Services page view
def services(request):
    return render(request, 'services.html')

# Contact page view
def contact(request):
    return render(request, 'contact.html')

# News page view
def news(request):
    return render(request, 'news.html')

# Airdrops page view
def airdrops(request):
    return render(request, 'airdrop.html')

# Coin Data page view
def coindata(request):
    return render(request, 'coin_data.html')

# Nodes page view
def nodes(request):
    return render(request, 'nodes.html')

def node1(request):
    return render(request, 'node1.html')

def node2(request):
    return render(request, 'node2.html')

def node3(request):
    return render(request, 'node3.html')

def node4(request):
    return render(request, 'node4.html')

# Login page view
def login(request):
    return render(request, 'login.html')

# Register page view
def register(request):
    return render(request, 'register.html')