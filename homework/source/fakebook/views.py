from django.shortcuts import render


def home(request):
    return render(request, 'index.html', {})


def friends(request):
    return render(request, 'friends.html', {})


def posts(request):
    return render(request, 'posts.html', {})


def family(request):
    return render(request, 'family.html', {})
