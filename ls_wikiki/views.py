from django.shortcuts import render

def home(request):
    return render(request, "ls_wikiki/wikiki.html")

