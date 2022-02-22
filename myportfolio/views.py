from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import *


def home(request):
    posts = Post.objects.all()[:3]
    personal = Personal.objects.first()
    skills = Skills.objects.all()
    exp = Experience.objects.all()
    ss =SoftSkills.objects.all()

    form = ContactForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {
        'posts' : posts,
        'personal' : personal,
        'skills' : skills,
        'exp' : exp,
        'form' : form,
        'ss' : ss,
    }
    return render(request, "index.html", context)


def post(request, pk):
    post = get_object_or_404(Post,pk=pk)
    return render(request, "post.html", {'post' : post})

