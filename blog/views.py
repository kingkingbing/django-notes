from django.shortcuts import render

# Create your views here.
from django.views.generic import DetailView, ListView
from .models import Tag, Member, Post

'''
def index(request):
    post_list = Post.objects.all().order_by('-deadline')
    return render(request, 'blog/index.html', context={'post_list': post_list})

'''

class TagListView(ListView):
    model = Tag

class TagDetailView(DetailView):
    model = Tag

class MemberListView(ListView):
    model = Member

class MemberDetailView(DetailView):
    model = Member

class PostListView(ListView):
    model = Post

class PostDetailView(DetailView):
    model = Post
