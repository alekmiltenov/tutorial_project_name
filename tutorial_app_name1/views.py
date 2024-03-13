from django.shortcuts import render
from django.views.generic import (ListView ,
                                  DetailView, 
                                  CreateView)
from . models import Post #the class name post from the same folder

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'tutorial_app_name1/home.html',context)
class PostListView(ListView): #default finction 
    model =Post
    template_name = 'tutorial_app_name1/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted'] # sort and display latest(by date)


class PostDetailView(DetailView):#default finction 
    model =Post
    
class PostCreateView(CreateView):#default finction 
    model =Post
    fields = ['title','content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


def about(request):
    return render(request, 'tutorial_app_name1/about.html',{'title':' '})
