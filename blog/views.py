from django.shortcuts import render, redirect
from.models import Post,PostAuthor
from.forms import CreatePostForm
# Create your views here.

def blog_home(request):
    blogs=Post.objects.all()
    context={
        'objects':blogs
    }
    return render(request,'blog/blog_home.html',context)


def createPost(request):
    user=request.user
    author_=PostAuthor.objects.get(user=user)
    form=CreatePostForm()
    if request.method=="POST":
        form=CreatePostForm(request.POST or None,request.FILES or None)
        if form.is_valid():
            new_post=form.save(commit=False)
            new_post.author=author_
            new_post.save()
            # return redirect('post',id)
