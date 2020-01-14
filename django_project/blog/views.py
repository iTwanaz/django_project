from django.shortcuts import render     #render also returns an HttpResponse at the back
# from django.http import HttpResponse

#dummy post datas
posts = [
    {
        'title': 'Post 1',
        'author': 'Aayush twayana',
        'date_posted': '27th march, 2000',
        'content': 'anything'
    },
    {
        'title': 'Post 2',
        'author': 'Prayush twayana',
        'date_posted': '27th july, 2004',  
        'content': 'anything'
    }
]


def home(request):
    # return HttpResponse('<h1>Hello World!</h1>')
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    # return HttpResponse('<h1>Hello About!</h1>')
    return render(request, 'blog/about.html', {'title': 'about'})