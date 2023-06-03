from django.shortcuts import render
from django.utils import timezone
from .models import Post, GroupsPosts
from django.views.generic import ListView
from django.db.models import Count


class PostView(ListView):
    model = Post
    template_name = "blog/home.html"
    all_posts = Post.objects.all()
    data_from_groups = [ Post.objects.filter(group = gr)[0:5] for gr in GroupsPosts.objects.all()]
    print(data_from_groups)
    all_groups = GroupsPosts.objects.all()
    top_rating_posts = Post.objects.order_by('-rating')[0:5]
    
    last_posts = Post.objects.order_by('-created_date')[0:5]
    def get_context_data(self, **kwargs):
        context = super(ListView, self).get_context_data(**kwargs)
        context.update({
        'all_posts': self.all_posts, 
        'data_from_groups': self.data_from_groups, 
        'last_posts': self.last_posts, 
        'all_groups': self.all_groups, 
        'top_rating_posts': self.top_rating_posts, 
        })
        return context
