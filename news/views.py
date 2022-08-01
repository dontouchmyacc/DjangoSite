from django.shortcuts import render, redirect


# from .serializer import ArticlesSerialize
from .models import Articles
from .forms import ArticlesForm
from django.views.generic import DetailView, UpdateView, DeleteView
# from rest_framework import generics

def news_home(request):
    news= Articles.objects.order_by('-date')
    return render(request, 'news/news1.html', {'news':news})

class NewsDetailView(DetailView):
    model = Articles
    template_name = 'news/details_view.html'
    context_object_name = 'article'

class NewsUpdateView(UpdateView):
    model = Articles
    template_name = 'news/create.html'
    form = ArticlesForm
    fields = ['title','anons', 'full_text', 'date']

class NewsDeleteView(DeleteView):
    model = Articles
    success_url = '/news/'
    template_name = 'news/news_delete.html'
    

def create(request):
    error = ''
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return  redirect('news')
        else:
            error= 'Форма не верная'
    form = ArticlesForm()
    data = {
        'form':form,
        'error':error
    }
    return render(request, 'news/create.html',data)

# class ArticlesAPIView(generics.ListApiView):
#     queryset = Articles.objects.all()
#     serializer_class = ArticlesSerialize