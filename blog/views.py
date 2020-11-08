from django.shortcuts import render


# Create your views here.

def posts_list(request):
    n = ['oleg', 'masha', 'kylym']
    return render(request, 'blog/index.html', context={'names': n})