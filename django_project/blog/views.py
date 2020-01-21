from django.shortcuts import render     #render also returns an HttpResponse at the back
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin       #cant use @login_required decorater so, using mixins
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post
# from django.http import HttpResponse

#dummy post datas
# posts = [
#     {
#         'title': 'Post 1',
#         'author': 'Aayush twayana',
#         'date_posted': '27th march, 2000',
#         'content': 'anything'
#     },
#     {
#         'title': 'Post 2',
#         'author': 'Prayush twayana',
#         'date_posted': '27th july, 2004',  
#         'content': 'anything'
#     }
# ]


#function based views
def home(request):
    # return HttpResponse('<h1>Hello World!</h1>')
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

#class based views--more efficient 
class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'        #<app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']             #changes the order from newsest to oldest

class PostDetailView(DetailView):
    model = Post
    # template_name = 'blog/post_detail.html'

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        
        if self.request.user == post.author:
            return True

        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        
        if self.request.user == post.author:
            return True

        return False

def about(request):
    # return HttpResponse('<h1>Hello About!</h1>')
    return render(request, 'blog/about.html', {'title': 'about'})