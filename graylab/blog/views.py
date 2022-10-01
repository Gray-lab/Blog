from django.shortcuts import render
from django.http import HttpResponse

from .models import Post
from markdown2 import Markdown

# Create your views here.
def index(request):
  
  return render(request, "blog/index.html", {
    "posts": Post.objects.all()
  })


def entry(request, id):
    # check if page exists, and if not, render an error page
    post = Post.objects.filter(id = id).first()
    markdown_content = post.content
    title = post.title
    # parse markdown to HTML before passing it as a variable to the renderer
    markdowner = Markdown()
    content = markdowner.convert(markdown_content)
    return render(request, "blog/post.html", {
        "title": title, # Passes in title to html renderer, to be used in the template
        "content": content
    })
