from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post, GroupsPosts

from django.template import loader
from django.http import HttpResponse
        
 
def main_page(request):
    all_posts = Post.objects.all()
    data_from_groups = [ Post.objects.filter(group = gr)[0:5] for gr in GroupsPosts.objects.all()]

    all_groups = GroupsPosts.objects.all()
    top_rating_posts = Post.objects.order_by('-rating')[0:5]
    
    last_posts = Post.objects.order_by('-created_date')[0:5]
    
    template = loader.get_template('blog/home.html')
    
    context = {
        'all_posts': all_posts.all(),
        'data_from_groups': data_from_groups,
        'last_posts': last_posts.all(),
        'all_groups': all_groups.all(),
        'top_rating_posts': top_rating_posts.all(),
        'active_page': 'home',
    }
    return HttpResponse(template.render(context, request))
    
 
def post_detail(request, pk):
    p = get_object_or_404(Post, pk=pk)
    post = Post.objects.get(id=pk)
    template = loader.get_template('blog/post.html')
    context = {
        'p': p,
        'post' : post
    }
    return HttpResponse(template.render(context, request))

