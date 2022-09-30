from django.shortcuts import render, redirect
from .models import Review

# Create your views here.
def index(request):
    reviews = Review.objects.all()
    rangee = range(len(reviews))
    context = {
        'reviews': reviews,
        'range': rangee,
    }
    return render(request, 'movie/index.html', context)

def write(request):
    return render(request, 'movie/write.html')
    
def write_sec(request):
    title = request.GET.get('title')
    content = request.GET.get('content')
    star = request.GET.get('star')
    Review.objects.create(title=title, content=content, star=star)
    return redirect('movie:index')

def content(request, pk):
    review = Review.objects.get(pk=pk)
    review.hits += 1
    review.save()
    context = {
        'review': review,
    }
    return render(request, 'movie/content.html', context)

def edit(request, pk):
    review = Review.objects.get(pk=pk)
    context = {
        'review': review,
    }
    return render(request, 'movie/edit.html', context)

def edit_sec(request, pk):
    review = Review.objects.get(pk=pk)
    title = request.GET.get('title')
    content = request.GET.get('content')
    star = request.GET.get('star')
    review.title = title
    review.content = content
    review.star = star
    review.save()
    return redirect('movie:index')

def delete(request, pk):
    Review.objects.get(pk=pk).delete()
    return redirect('movie:index')